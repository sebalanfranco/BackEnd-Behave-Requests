import behave
import requests
import json
from jsonschema import RefResolver

# This hook serves the needed modules to the Context.
def before_all(context):
    context.rest_client = setup_rest_client()
    context.json_schema_resolver = setup_base_json_schema_resolver(context)

# This method provides the logic to setup the REST client.
# In this case, only returns the Requests module.
# The main idea is to provide a base logic in case of facing a 
# more complex module configuration.
# Returns the requests {requests} module.
def setup_rest_client():
    return requests

# This method provides an json schema resolver based on reusable definitions (placed in definitions.json file).
# In order to aviod handling json files around the steps, the resolver is setup once in the before_all hook.
# Returns the schema resolver.
def setup_base_json_schema_resolver(context):
    definitions = json.loads(open(context.config.userdata['json_schemas'] + 'definitions.json', 'r').read().replace('\n', ''))
    
    return RefResolver.from_schema(definitions)