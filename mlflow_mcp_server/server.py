from mcp.server.fastmcp import FastMCP

from mlflow_mcp_server.tools.experiment_tools import (
    get_experiment,
    get_experiment_by_name,
    search_experiments,
)
from mlflow_mcp_server.tools.registered_models import (
    create_model_version,
    create_registered_model,
    delete_model_version,
    delete_registered_model,
    get_model_versions,
    get_registered_models,
    rename_registered_model,
    set_registered_model_alias,
)
from mlflow_mcp_server.tools.run_tools import (
    get_experiment_runs,
    get_run,
)

mcp = FastMCP(
    name="MLFlow MCP Server",
    dependencies=["mlflow", "pydantic"],
)

mcp.add_tool(get_experiment)
mcp.add_tool(get_experiment_by_name)
mcp.add_tool(search_experiments)

mcp.add_tool(get_run)
mcp.add_tool(get_experiment_runs)


mcp.add_tool(get_registered_models)
mcp.add_tool(get_model_versions)
mcp.add_tool(create_registered_model)
mcp.add_tool(create_model_version)
mcp.add_tool(rename_registered_model)
mcp.add_tool(set_registered_model_alias)
mcp.add_tool(delete_registered_model)
mcp.add_tool(delete_model_version)
