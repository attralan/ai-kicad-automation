import os
import sys

from mcp import ClientSession

from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)

from bridge.security import check_tool

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


async def call_tool(

    tool_name,

    arguments
):

    check_tool(tool_name)

    params = StdioServerParameters(

        command=sys.executable,

        args=[

            "-m",

            "kicad_mcp_server.server"

        ],

        cwd=BASE_DIR,

        env={

            **os.environ

        }

    )

    print(
        "Starting MCP package server..."
    )

    async with stdio_client(params) as (

        read,

        write

    ):

        async with ClientSession(

            read,

            write

        ) as session:

            print(
                "Initializing MCP..."
            )

            await session.initialize()

            print(
                "Calling tool:",
                tool_name
            )

            result = await session.call_tool(

                tool_name,

                arguments

            )

            return result
