"""
API requests utils.

Aiming at keeping the step definitions as simple as possible, the modules under "utils/" 
folders contain the logic to interact with different entities and tools.
"""

# This method make a request to the API.
"""
Note that context is passed: this is because the requests module is imported from environment.py
and stored in "context.rest_client".
Default method is GET. A dict is used to match the passed method and execute the proper request.

TODO: handle error when wrong method name is passed. 
"""
def call_rest_api(context, endpoint, body, headers={}, method='GET'):
    headers = set_default_headers(headers)
    methods = {
        'get': context.rest_client.get(context.config.userdata['url'] + endpoint, headers = headers),
        'post': context.rest_client.post(context.config.userdata['url'] + endpoint, data = body, headers = headers),
        'put': context.rest_client.put(context.config.userdata['url'] + endpoint, data = body, headers = headers),
        'delete': context.rest_client.delete(context.config.userdata['url'] + endpoint, headers = headers),
        'head': context.rest_client.head(context.config.userdata['url'] + endpoint, headers = headers),
        'options': context.rest_client.options(context.config.userdata['url'] + endpoint, headers = headers)
    }
    response = methods[method.lower()]
    context.api_response_body = response.json()
    context.api_response_status_code = response.status_code
    
# This method set the default headers for the resquest to be executed.
def set_default_headers(headers):
    default_headers = {}
    default_headers['content-type'] = 'application/json'
    default_headers['x-mock-match-request-body'] = 'true' # Header to force Postman mocks to check request body.
    if len(headers) > 0:
        default_headers + headers
    return default_headers

# This method searches in {response_body} dict based on {value_path} and returns the value found or False.
def get_response_value(response_body, value_path):
    search_values = value_path.split('/')
    value_found = response_body
    for value in search_values:
        # Check if found last iterable item in the JSon path
        try:
            if value in value_found:
                value_found = value_found[value]
                continue
            return False
        except TypeError:
            return False
    return value_found
