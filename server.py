# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server with debug enabled
mcp = FastMCP("Character", debug=True)


# Add an addition tool
@mcp.tool()
def ohki_shogun() -> str:
    """王騎将軍の名台詞を返します"""
    print("王騎将軍ツールが呼ばれました。")
    with open(file="lines/ohki.txt", mode="r") as f:
        lines = f.read()
    return lines

# Add this part to run the server
if __name__ == "__main__":
    # stdioトランスポートを使用
    print("Starting MCP server in stdio mode")
    mcp.run(transport="stdio")
