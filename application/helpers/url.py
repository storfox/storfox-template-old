from typing import Optional
from urllib.parse import urlparse, parse_qsl, ParseResult
from .params import Params


class URL(object):
    url: ParseResult

    def __init__(self, url: str):
        self.url = urlparse(url)

    def get_protocol(self) -> str:
        return self.url.scheme

    def get_username(self) -> Optional[str]:
        return self.url.username

    def get_password(self) -> Optional[str]:
        return self.url.password

    def get_hostname(self) -> Optional[str]:
        return self.url.hostname

    def get_port(self) -> Optional[int]:
        return self.url.port

    def get_query(self) -> str:
        return self.url.query

    def get_params(self) -> Params:
        query = self.get_query()
        qsl = dict(parse_qsl(query))

        return Params(qsl)
