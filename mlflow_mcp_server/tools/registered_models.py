from mlflow_mcp_server.utils.mlflow_client import client
from pydantic import Field
from typing import Annotated
from pprint import pprint


def get_registered_models(
    model_name: Annotated[
        str,
        Field(description="The name of the registered model to search for"),
    ] = None,
    token: Annotated[str, Field(description="The token to use for pagination")] = None,
):
    filter_string = None
    if model_name:
        filter_string = f"name LIKE '%{model_name}%'"

    models = client.search_registered_models(
        filter_string=filter_string,
        page_token=token,
        max_results=20,
    )
    return {
        "models": models,
        "token": models.token,
    }


def get_model_versions(model_name=None, token=None):
    filter_string = None
    if model_name:
        filter_string = f"name LIKE '%{model_name}%'"

    model_versions = client.search_model_versions(
        filter_string=filter_string,
        page_token=token,
        max_results=20,
    )

    return {
        "model_versions": model_versions,
        "token": model_versions.token,
    }


# rm = get_registered_models()

# for rm in client.search_registered_models():
#     pprint(dict(rm), indent=4)
