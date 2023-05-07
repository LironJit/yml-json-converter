import os
import yaml
import json

# Get the current working directory
cwd = os.getcwd()

# Find all .yml and .yaml files in the root directory
yaml_files = [f for f in os.listdir(cwd) if f.endswith(('.yml', '.yaml'))]

# Convert each YAML file to JSON and save it in the same directory
for file_name in yaml_files:
    # Open the YAML file and load its contents
    with open(file_name, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)

    # Construct the name of the corresponding JSON file
    json_file_name = os.path.splitext(file_name)[0] + '.json'

    # Open the JSON file and write the converted data to it
    with open(json_file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
