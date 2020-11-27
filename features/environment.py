from behave import *
import requests

# This hook serves the needed modules to the Context.
def before_all(context):
    context.rest_client = setup_rest_client()

# This method provides the logic to setup the REST client.
"""
In this case, only returns the Requests module.
The main idea is to provide a base logic in case of facing a 
more complex module configuration.
"""
def setup_rest_client():
    return requests
