from .development import *

ENV = "testing"

DATABASE = {
    "HOST": os.environ.get("DATABASE_HOST", "localhost"),
    "PORT": os.environ.get("DATABASE_PORT", "5432"),
    "USER": os.environ.get("DATABASE_USER", "test"),
    "PASSWORD": os.environ.get("DATABASE_PASSWORD", "test"),
    "NAME": os.environ.get("DATABASE_NAME", "test"),
}
