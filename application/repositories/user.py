from storfox import Repository
from sqlalchemy import select  # type: ignore


class LocationRepository(Repository):
    async def all(self):
        query = 'select(notes)'
        return await self.fetch_all(query)
