from mlflow_mcp_server.utils.mlflow_client import client


def get_experiment(experiment_id: str) -> dict:
    """Get experiment details"""
    experiment = client.get_experiment(experiment_id)
    return {
        "name": experiment.name,
        "experiment_id": experiment.experiment_id,
        "lifecycle_stage": experiment.lifecycle_stage,
    }


def get_experiment_by_name(experiment_name: str) -> dict:
    """Get experiment details by name"""
    experiment = client.get_experiment_by_name(experiment_name)
    return {
        "name": experiment.name,
        "experiment_id": experiment.experiment_id,
        "lifecycle_stage": experiment.lifecycle_stage,
    }


def search_experiments(
    name: str | None = None,
    token: str | None = None,
) -> list:
    """List all experiments"""
    filter_string = None
    if name:
        filter_string = f"name LIKE '%{name}%'"

    experiments_response = client.search_experiments(
        filter_string=filter_string,
        max_results=20,
        page_token=token,
    )

    experiments = {
        "experiments": [
            {
                "name": experiment.name,
                "experiment_id": experiment.experiment_id,
            }
            for experiment in experiments_response
        ],
        "token": experiments_response.token,
    }
    return experiments


# print(search_experiments(token="eyJvZmZzZXQiOiAyMH0="))
