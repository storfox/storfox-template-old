# Library
from storfox_framework import Storfox
from storfox_framework import config_vars
from storfox_framework import Container as BaseContainer

from dependency_injector import providers

# Application
from application.controllers.echo import EchoController
from application.repositories.user import LocationRepository


handlers = [
    EchoController()
]


class Container(BaseContainer):
    location_repository = providers.Factory(LocationRepository)
    location_repository = providers.Factory(LocationRepository)


if __name__ == '__main__':
    container = Container()
    container.config.from_dict(config_vars())

    app = Storfox(handlers)
    app.container = container
    app.run()

