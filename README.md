# MLflow MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes MLflow experiment tracking and model registry operations as tools for AI assistants.

## Quickstart

The fastest way to get started is to add the server to your MCP client config. No local clone required.

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "mlflow": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/yesid-lopez/mlflow-mcp-server", "mlflow_mcp_server"],
      "env": {
        "MLFLOW_TRACKING_URI": "http://localhost:5000"
      }
    }
  }
}
```

### Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "mlflow": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/yesid-lopez/mlflow-mcp-server", "mlflow_mcp_server"],
      "env": {
        "MLFLOW_TRACKING_URI": "http://localhost:5000"
      }
    }
  }
}
```

### OpenCode

Add to your `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "mlflow": {
      "type": "local",
      "command": ["uvx", "--from", "git+https://github.com/yesid-lopez/mlflow-mcp-server", "mlflow_mcp_server"],
      "environment": {
        "MLFLOW_TRACKING_URI": "http://localhost:5000"
      }
    }
  }
}
```

Replace `http://localhost:5000` with the URL of your MLflow tracking server.

## Tools

### Experiment Management

| Tool | Description |
|------|-------------|
| `get_experiment` | Get experiment details by ID |
| `get_experiment_by_name` | Get experiment details by name |
| `search_experiments` | List and filter experiments with optional name matching and pagination |

### Run Management

| Tool | Description |
|------|-------------|
| `get_run` | Get full run details including metrics, parameters, tags, and run type (parent/child/standalone) |
| `get_experiment_runs` | List runs for an experiment with pagination |

### Model Registry

| Tool | Description |
|------|-------------|
| `get_registered_models` | Search and list registered models |
| `get_model_versions` | Browse model versions with filtering |
| `create_registered_model` | Create a new registered model with optional description and tags |
| `create_model_version` | Create a new model version from a run's artifacts |
| `rename_registered_model` | Rename an existing registered model |
| `set_registered_model_alias` | Assign an alias (e.g. `champion`, `challenger`) to a model version |
| `delete_registered_model` | Delete a registered model and all its versions |
| `delete_model_version` | Delete a specific model version |

## Configuration

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `MLFLOW_TRACKING_URI` | `http://localhost:5000` | URL of the MLflow tracking server |

## Installation (Development)

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- An MLflow tracking server

### Setup

```bash
git clone https://github.com/yesid-lopez/mlflow-mcp-server.git
cd mlflow-mcp-server
uv sync
```

### Running Locally

```bash
export MLFLOW_TRACKING_URI="http://localhost:5000"
uv run -m mlflow_mcp_server
```

The server communicates over **stdio**, which is the standard MCP transport for local tool servers.

## Project Structure

```
mlflow_mcp_server/
├── __main__.py              # Entry point
├── server.py                # MCP server setup and tool registration
├── tools/
│   ├── experiment_tools.py  # Experiment search and retrieval
│   ├── run_tools.py         # Run details and listing
│   └── registered_models.py # Model registry CRUD operations
└── utils/
    └── mlflow_client.py     # MLflow client singleton
```

### Adding New Tools

1. Create a function in the appropriate file under `tools/`.
2. Register it in `server.py`:

```python
from mlflow_mcp_server.tools.your_module import your_function
mcp.add_tool(your_function)
```

### Linting

```bash
uv run ruff check .
uv run ruff format --check .
```

## License

MIT
