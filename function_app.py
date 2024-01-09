import azure.functions as func
from azure.data.tables import TableClient
import logging
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    table_conn_str = os.environ["TABLE_CONN_STR"]
    table_client = TableClient.from_connection_string(conn_str=table_conn_str, table_name="visitorCount")

    entity = table_client.get_entity(partition_key="VisitorCount", row_key="CurrentCount")

    count = entity["count"] + 1
    entity["count"] = count
    table_client.update_entity(mode="merge", entity=entity)

    return func.HttpResponse(f"{count}", status_code=200)
