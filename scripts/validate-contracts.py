import os
import sys
import json
from jsonschema import Draft202012Validator, validate, ValidationError

# Sample shapes for validation
SAMPLE_SHAPES = {
    "stations-metadata": [
        [],
        {"stations": []},
        {"estacions": []}
    ],
    "variables-metadata": [
        [],
        {"variables": []},
        {"variables_auxiliars": []}
    ],
    "measured-variable": [
        [],
        {"data": []},
        {"dades": []},
        {"observations": []},
        {"observacions": []}
    ]
}

def validate_contracts():
    datasets_dir = "datasets"
    overall_failed = False
    count = 0
    
    required_fields = [
        "contract_id", "dataset_id", "source", "resource", "layer",
        "status", "validation_level", "schema_ref", "description",
        "allowed_evolution", "known_limitations"
    ]
    
    for root, dirs, files in os.walk(datasets_dir):
        for file in files:
            if file.endswith(".contract.json"):
                count += 1
                file_path = os.path.join(root, file)
                contract_failed = False
                try:
                    with open(file_path, "r") as f:
                        contract = json.load(f)
                    
                    # Verify required fields
                    missing_fields = [field for field in required_fields if field not in contract]
                    if missing_fields:
                        print(f"✗ {file_path} is missing fields: {', '.join(missing_fields)}")
                        contract_failed = True
                        
                    # Verify specific values
                    if contract.get("dataset_id") != "meteocat-weather":
                        print(f"✗ {file_path} has invalid dataset_id: {contract.get('dataset_id')}")
                        contract_failed = True
                        
                    if contract.get("status") != "draft":
                        print(f"✗ {file_path} status must be 'draft', got: {contract.get('status')}")
                        contract_failed = True
                    
                    # Verify schema reference
                    schema_ref = contract.get("schema_ref")
                    if not schema_ref:
                         schema_path = None
                    else:
                        schema_path = os.path.normpath(os.path.join(os.path.dirname(file_path), schema_ref))
                    
                    if schema_path and not os.path.exists(schema_path):
                        print(f"✗ {file_path} references non-existent schema: {schema_ref} (resolved to {schema_path})")
                        contract_failed = True
                    elif schema_path:
                        try:
                            with open(schema_path, "r") as sf:
                                schema = json.load(sf)
                            
                            # Structural validation
                            try:
                                Draft202012Validator.check_schema(schema)
                            except Exception as e:
                                print(f"✗ Schema {schema_path} is not a valid JSON Schema: {e}")
                                contract_failed = True
                            
                            if "$schema" not in schema:
                                print(f"✗ Schema {schema_path} is missing '$schema'")
                                contract_failed = True
                            if "title" not in schema:
                                print(f"✗ Schema {schema_path} is missing 'title'")
                                contract_failed = True
                                
                            # Validate sample shapes
                            resource = contract.get("resource")
                            if resource in SAMPLE_SHAPES:
                                for sample in SAMPLE_SHAPES[resource]:
                                    try:
                                        validate(instance=sample, schema=schema)
                                    except ValidationError as e:
                                        print(f"✗ Schema {schema_path} failed to validate sample shape {sample}: {e.message}")
                                        contract_failed = True

                        except json.JSONDecodeError:
                            print(f"✗ Schema {schema_path} is not valid JSON")
                            contract_failed = True

                    if not contract_failed:
                        print(f"✓ {file_path} is valid.")
                    else:
                        overall_failed = True

                except json.JSONDecodeError:
                    print(f"✗ {file_path} is not valid JSON")
                    overall_failed = True
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    overall_failed = True
                    
    if count == 0:
        print("No contracts found to validate.")
                
    if overall_failed:
        print("\nContract validation failed!")
        sys.exit(1)
    else:
        print(f"\nAll {count} contract files are valid.")
        sys.exit(0)

if __name__ == "__main__":
    validate_contracts()
