import pytest
import logging
import requests
from testConstants import *

response = requests.get(f"{FUNCAPP_BASE_URL}/api/HttpExample", params={"name": "Francis"})
print(response.content)