from mlflow_mcp_server.utils.mlflow_client import client
from pydantic import Field
from typing import Annotated, Optional


def get_registered_models(
    model_name: Annotated[
        Optional[str],
        Field(description="The name of the registered model to search for"),
    ] = None,
    token: Annotated[
        Optional[str], Field(description="The token to use for pagination")
    ] = None,
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


def create_registered_model(
    name: Annotated[
        str,
        Field(description="The name of the registered model to create"),
    ],
    description: Annotated[
        Optional[str],
        Field(description="A description for the registered model"),
    ] = None,
    tags: Annotated[
        Optional[dict],
        Field(description="A dictionary of key-value tags to associate with the model"),
    ] = None,
):
    """Create a new registered model in the MLflow Model Registry."""
    model = client.create_registered_model(
        name=name,
        description=description,
        tags=tags,
    )
    return {"registered_model": model}


def create_model_version(
    name: Annotated[
        str,
        Field(description="The name of the registered model to create a version for"),
    ],
    source: Annotated[
        str,
        Field(
            description="The source URI of the model artifacts, e.g. 'runs:/<run_id>/model' or an absolute path"
        ),
    ],
    run_id: Annotated[
        Optional[str],
        Field(description="The ID of the run that generated this model version"),
    ] = None,
    description: Annotated[
        Optional[str],
        Field(description="A description for the model version"),
    ] = None,
    tags: Annotated[
        Optional[dict],
        Field(description="A dictionary of key-value tags to associate with the model version"),
    ] = None,
):
    """Create a new model version for an existing registered model."""
    model_version = client.create_model_version(
        name=name,
        source=source,
        run_id=run_id,
        description=description,
        tags=tags,
    )
    return {"model_version": model_version}


def rename_registered_model(
    name: Annotated[
        str,
        Field(description="The current name of the registered model"),
    ],
    new_name: Annotated[
        str,
        Field(description="The new name for the registered model"),
    ],
):
    """Rename an existing registered model."""
    model = client.rename_registered_model(
        name=name,
        new_name=new_name,
    )
    return {"registered_model": model}


def set_registered_model_alias(
    name: Annotated[
        str,
        Field(description="The name of the registered model"),
    ],
    alias: Annotated[
        str,
        Field(description="The alias to set, e.g. 'champion', 'challenger'"),
    ],
    version: Annotated[
        str,
        Field(description="The model version number to associate with the alias"),
    ],
):
    """Set an alias for a specific version of a registered model."""
    client.set_registered_model_alias(
        name=name,
        alias=alias,
        version=version,
    )
    return {
        "message": f"Alias '{alias}' set for model '{name}' version {version}",
    }


def delete_registered_model(
    name: Annotated[
        str,
        Field(description="The name of the registered model to delete"),
    ],
):
    """Delete a registered model and all its versions. This action is irrevocable."""
    client.delete_registered_model(name=name)
    return {"message": f"Registered model '{name}' has been deleted"}


def delete_model_version(
    name: Annotated[
        str,
        Field(description="The name of the registered model"),
    ],
    version: Annotated[
        str,
        Field(description="The version number to delete"),
    ],
):
    """Delete a specific version of a registered model. This action is irrevocable."""
    client.delete_model_version(name=name, version=version)
    return {"message": f"Version {version} of model '{name}' has been deleted"}
