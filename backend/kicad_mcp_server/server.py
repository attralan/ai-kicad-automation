import sys

from mcp.server.fastmcp import FastMCP

from tools import register_tools


mcp = FastMCP(
    "AI-KiCad-Copilot"
)


register_tools(mcp)


print(
    "MCP SERVER LOADED",
    file=sys.stderr,
    flush=True
)


if __name__ == "__main__":

    print(
        "MCP SERVER STARTING",
        file=sys.stderr,
        flush=True
    )


    mcp.run(
        transport="stdio"
    )