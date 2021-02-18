from storfox_framework import Repository
from sqlalchemy import select


class LocationRepository(Repository):
    async def all(self):
        query = 'select(notes)'
        return await self.fetch_all(query)
