from mlflow_mcp_server.server import mcp

if __name__ == "__main__":
    print("Starting MLFlow MCP Server")
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        import traceback

        print("Failed to run MCP server:", e)
        traceback.print_exc()
