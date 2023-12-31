import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            logging.error("Error: No name passed")
            return func.HttpResponse("Error: no name passed", status_code=400)
        else:
            name = req_body.get('name')

    return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.", status_code=200)
