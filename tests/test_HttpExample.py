import pytest
import logging
import requests
from testConstants import *

def test_function_app_is_working():
    response = requests.get(FUNCAPP_BASE_URL)
    assert response.status_code == 200

def test_function_app_HttPExample_trigger_is_working():
    response = requests.get(f"{FUNCAPP_BASE_URL}/api/HttpExample")
    assert (response.status_code == 200 and 
            f"{response.content}" == "b'This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.'")

def test_function_app_HttpExample_trigger_nameParams_is_working():
    params = {"name" : "Francis"}
    response = requests.get(f"{FUNCAPP_BASE_URL}/api/HttpExample", params=params)
    assert (response.status_code == 200 and 
            F"{response.content}" == f"b'Hello, {params.get('name')}. This HTTP triggered function executed successfully.'")