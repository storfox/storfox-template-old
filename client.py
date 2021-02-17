import asyncio

from grpclib.client import Channel
from genproto.echo import EchoStub


async def main():
    async with Channel("127.0.0.1", 50051) as channel:
        echo = EchoStub(channel)

        reply = await echo.echo(value="10", extra_times=10)
        print(reply)


if __name__ == "__main__":
    asyncio.run(main())
