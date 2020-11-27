"""
File utils.

Aiming at keeping the step definitions as simple as possible, the modules under "utils/" 
folders contain the logic to interact with different entities and tools.
"""

import json

# This method opens {schema_file} as json.
def get_json_file(schema_file):
    file = open(schema_file, 'r')
    return json.loads(file.read().replace('\n', ''))
