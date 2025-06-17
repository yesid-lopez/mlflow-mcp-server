from mlflow_mcp_server.utils.mlflow_client import client


def get_experiment_runs(
    experiment_id: str = "226",
    token: str | None = None,
) -> list:
    """Get all runs for an experiment"""
    runs = client.search_runs(
        experiment_ids=[experiment_id],
        max_results=20,
        page_token=token,
    )
    return [
        {
            "run_id": run.info.run_id,
            "run_name": run.info.run_name,
            "status": run.info.status,
            "start_time": run.info.start_time,
            "end_time": run.info.end_time,
            "run_type": identify_run_type(run.info.run_id),
            "token": runs.token,
        }
        for run in runs
    ]


def get_run(run_id: str) -> dict:
    """Get a run by ID"""
    run = client.get_run(run_id)
    return {
        "run_id": run.info.run_id,
        "run_name": run.info.run_name,
        "status": run.info.status,
        "metrics": run.data.metrics,
        "params": run.data.params,
        "tags": run.data.tags,
        "run_type": identify_run_type(run_id),
    }


def identify_run_type(run_id):
    # Get the run
    run = client.get_run(run_id)

    # Check if it's a child run
    parent_run = client.get_parent_run(run_id)
    if parent_run is not None:
        return "child"

    # Check if it has child runs (making it a parent)
    experiment_id = run.info.experiment_id
    filter_string = f"tags.mlflow.parentRunId = '{run_id}'"

    child_runs = client.search_runs(
        experiment_ids=[experiment_id],
        filter_string=filter_string,
        max_results=2,
    )

    if len(child_runs) > 0:
        return "parent"
    else:
        return "standalone"


# print(identify_run_type("3d80f6266d554cc7b6739030932bb1b8"))
