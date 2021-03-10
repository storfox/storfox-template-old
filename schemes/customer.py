import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

from .metadata import metadata


customer = sqlalchemy.Table(
    "customer",
    metadata,
    sqlalchemy.Column("guid", UUID, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=255)),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=255)),
    sqlalchemy.Column("birth_date", sqlalchemy.Date),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("is_deleted", sqlalchemy.Boolean),
)


customer_address = sqlalchemy.Table(
    "customer_address",
    metadata,
    sqlalchemy.Column("guid", UUID, primary_key=True),
    sqlalchemy.Column("customer_guid", UUID, sqlalchemy.ForeignKey("customer.guid")),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=255)),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=255)),
    sqlalchemy.Column("phone_number", sqlalchemy.String(length=255)),
    sqlalchemy.Column("address", sqlalchemy.String(length=255)),
    sqlalchemy.Column("zip_code", sqlalchemy.String(length=255)),
    sqlalchemy.Column("city", sqlalchemy.String(length=255)),
    sqlalchemy.Column("country", sqlalchemy.String(length=255)),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("is_deleted", sqlalchemy.Boolean)
)
