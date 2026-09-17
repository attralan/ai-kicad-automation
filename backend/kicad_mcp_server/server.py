from mcp.server.fastmcp import FastMCP

from kicad_mcp_server.tools import register_tools

print(
    "MCP SERVER LOADED"
)

mcp = FastMCP(
    "AI KiCad MCP Server"
)

register_tools(mcp)

print(
    "MCP SERVER STARTING"
)

if __name__ == "__main__":
    mcp.run(
        transport="stdio"
    )
