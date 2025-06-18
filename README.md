# MLflow MCP Server

A Model Context Protocol (MCP) server that provides seamless integration with MLflow, enabling AI assistants to interact with MLflow experiments, runs, and registered models.

## Overview

This MCP server exposes MLflow functionality through a standardized protocol, allowing AI assistants like Claude to:
- Browse and search MLflow experiments
- Retrieve experiment runs and their details
- Query registered models and model versions
- Access metrics, parameters, and metadata

## Features

### Experiment Management
- **Get Experiment**: Retrieve experiment details by ID
- **Get Experiment by Name**: Find experiments by name
- **Search Experiments**: List and filter experiments with pagination support

### Run Management
- **Get Run**: Retrieve detailed run information including metrics, parameters, and tags
- **Get Experiment Runs**: List all runs for a specific experiment
- **Run Type Detection**: Automatically identifies parent, child, or standalone runs

### Model Registry
- **Get Registered Models**: Search and list registered models
- **Get Model Versions**: Browse model versions with filtering capabilities

## Installation

### Prerequisites
- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd mlflow-mcp-server
```

2. Install dependencies:
```bash
uv sync
```

## Configuration

### MLflow Connection
The server is pre-configured to connect to your internal MLflow instance:
- **Tracking URI**: `YOUR URI`

To use with a different MLflow instance, modify `mlflow_mcp_server/utils/mlflow_client.py`:

```python
import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("your-mlflow-tracking-uri")
client = MlflowClient()
```

### MCP Configuration

Add the following configuration to your MCP client (e.g., `~/.cursor/mcp.json` for Cursor):

```json
{
  "mcpServers": {
    "mlflow": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/yesid-lopez/mlflow-mcp-server", "mlflow_mcp_server"],
      "env": {
        "MLFLOW_TRACKING_URI": "YOUR_TRACKING_URI"
      }
    }
  }
}
```

Replace `/path/to/mlflow-mcp-server` with the actual path to your project directory.

## Usage

### Running the Server

```bash
uv run -m mlflow_mcp_server
```

### Available Tools

Once configured, the following tools become available to your AI assistant:

#### Experiment Tools
- `get_experiment(experiment_id: str)` - Get experiment details by ID
- `get_experiment_by_name(experiment_name: str)` - Get experiment by name
- `search_experiments(name?: str, token?: str)` - Search experiments with optional filtering

#### Run Tools
- `get_run(run_id: str)` - Get detailed run information
- `get_experiment_runs(experiment_id: str, token?: str)` - List runs for an experiment

#### Model Registry Tools
- `get_registered_models(model_name?: str, token?: str)` - Search registered models
- `get_model_versions(model_name?: str, token?: str)` - Browse model versions

### Example Usage with AI Assistant

You can now ask your AI assistant questions like:
- "Show me all experiments containing 'recommendation' in the name"
- "Get the details of run ID abc123 including its metrics and parameters"
- "List all registered models and their latest versions"
- "Find experiments related to customer segmentation"

## Development

### Project Structure

```
mlflow-mcp-server/
├── mlflow_mcp_server/
│   ├── __main__.py          # Server entry point
│   ├── server.py            # Main MCP server configuration
│   ├── tools/               # MLflow integration tools
│   │   ├── experiment_tools.py
│   │   ├── run_tools.py
│   │   └── registered_models.py
│   └── utils/
│       └── mlflow_client.py # MLflow client configuration
├── pyproject.toml           # Project dependencies
└── README.md
```

### Dependencies

- **mcp[cli]**: Model Context Protocol framework
- **mlflow**: MLflow client library
- **pydantic**: Data validation and serialization

### Adding New Tools

To add new MLflow functionality:

1. Create a new function in the appropriate tool file
2. Add the tool to `server.py`:
   ```python
   from mlflow_mcp_server.tools.your_module import your_function
   mcp.add_tool(your_function)
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions:
- Check existing issues in the repository
- Create a new issue with detailed reproduction steps
