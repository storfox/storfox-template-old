from genproto.echo import EchoBase, EchoResponse


class EchoController(EchoBase):
    async def echo(self, value: str, extra_times: int) -> EchoResponse:
        return EchoResponse(
            values=["My name is Bekhzod"],
        )
