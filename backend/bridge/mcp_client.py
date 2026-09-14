import os
import sys

from mcp import ClientSession

from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)



BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


SERVER_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "kicad_mcp_server",
        "server.py"
    )
)



async def call_tool(
    tool_name,
    arguments
):


    params = StdioServerParameters(

        command=sys.executable,

        args=[
            SERVER_PATH
        ],

        env={
            **os.environ
        }

    )


    async with stdio_client(params) as (

        read,

        write

    ):


        async with ClientSession(

            read,

            write

        ) as session:


            await session.initialize()


            result = await session.call_tool(

                tool_name,

                arguments

            )


            return result