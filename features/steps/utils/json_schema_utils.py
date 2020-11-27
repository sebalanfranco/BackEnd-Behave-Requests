"""
JSon Schemas utils.

Aiming at keeping the step definitions as simple as possible, the modules under "utils/" 
folders contain the logic to interact with different entities and tools.
"""

from jsonschema import validate

# This method validates {json_response} against {schema_file}.
def validate_response(json_response, schema_file , schema_resolver):
    try: 
        validate(instance = json_response, schema = schema_file, resolver = schema_resolver)
        return True
    except ValidationError:
        return False
