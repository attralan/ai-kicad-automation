import asyncio
import os
import sys

from mcp import ClientSession

from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


SERVER_PATH = os.path.join(
    BASE_DIR,
    "kicad_mcp_server",
    "server.py"
)


async def main():

    params = StdioServerParameters(

        command=sys.executable,

        args=[
            SERVER_PATH
        ],

        env={
            **os.environ
        }

    )


    print(
        "Starting MCP Server:"
    )

    print(
        SERVER_PATH
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
                "Initializing..."
            )


            await session.initialize()


            print(
                "MCP Connected"
            )


            tools = await session.list_tools()


            print(
                "\nAvailable Tools:"
            )


            for tool in tools.tools:

                print(
                    "-",
                    tool.name
                )


            print(
                "\nTesting create project..."
            )


            result = await session.call_tool(

                "create_kicad_project",

                {
                    "project_name":
                    "v11_test_board"
                }

            )


            print(result)



if __name__ == "__main__":

    asyncio.run(main())