import os
import sys
import yaml
import json
from jsonschema import validate, ValidationError

def validate_datasets():
    schema_path = "schemas/dataset.schema.json"
    datasets_dir = "datasets"
    
    if not os.path.exists(schema_path):
        print(f"Error: Schema not found at {schema_path}")
        sys.exit(1)
        
    with open(schema_path, "r") as f:
        schema = json.load(f)
        
    failed = False
    count = 0
    
    for root, dirs, files in os.walk(datasets_dir):
        if "dataset.yml" in files:
            count += 1
            file_path = os.path.join(root, "dataset.yml")
            try:
                with open(file_path, "r") as f:
                    data = yaml.safe_load(f)
                validate(instance=data, schema=schema)
                print(f"✓ {file_path} is valid.")
            except ValidationError as e:
                print(f"✗ {file_path} is invalid: {e.message}")
                failed = True
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                failed = True
                
    if failed:
        print("\nValidation failed!")
        sys.exit(1)
    else:
        print(f"\nAll {count} dataset metadata files are valid.")
        sys.exit(0)

if __name__ == "__main__":
    validate_datasets()
