# JSon Schemas utils.

# Aiming at keeping the step definitions as simple as possible, the modules under "utils/" 
# folders contain the logic to interact with different entities and tools.

from jsonschema import validate, ValidationError

# This method validates {json_response} against {schema_file}.
# Returns a dictionary with 'result' field True if schema validation passes, or False and
# 'message' with validation error.
def validate_response(json_response, schema_file , schema_resolver):
    try: 
        validate(instance = json_response, schema = schema_file, resolver = schema_resolver)
        return { 'result': True }
    except ValidationError as ve:
        return { 'result': False, 'message':  ve}
