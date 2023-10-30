

#APP_ENVIRONMENT = "LOCAL"
APP_ENVIRONMENT = "CLOUD"

if APP_ENVIRONMENT == "LOCAL":
    FUNCAPP_BASE_URL = "http://localhost:7071/"
else:
    FUNCAPP_BASE_URL = "https://helloworld-funcapp.azurewebsites.net/"