"""
JSon Schemas utils.

Aiming at keeping the step definitions as simple as possible, the modules under "utils/" 
folders contain the logic to interact with different entities and tools.
"""
import json

# This method searchs json files in {schema_files_path} by the {schema_name} and returns the schema.
def get_json_schema(schema_files_path, schema_name):
    file = open(schema_files_path + schema_name + '.json', 'r')
    return json.loads(file.read().replace('\n', ''))
