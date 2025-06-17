from mlflow_mcp_server.server import mcp

def main():
    print("Starting MLFlow MCP Server")
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        import traceback
        print("Failed to run MCP server:", e)
        traceback.print_exc()

if __name__ == "__main__":
    main()
