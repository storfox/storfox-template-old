import os

ENV = "development"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    "HOST": os.environ.get("DATABASE_HOST", "localhost"),
    "PORT": os.environ.get("DATABASE_PORT", "5432"),
    "USER": os.environ.get("DATABASE_USER", "storfox"),
    "PASSWORD": os.environ.get("DATABASE_PASSWORD", "storfox"),
    "NAME": os.environ.get("DATABASE_NAME", "storfox"),
    "CA_CERT": os.environ.get("DATABASE_CA_CERT"),
    "SSL": os.environ.get("DATABASE_SSL", False),
}

KAFKA = {
    "HOST": os.environ.get("KAFKA_HOST", "localhost"),
    "PORT": os.environ.get("KAFKA_PORT", "9092"),
    'GROUP_ID': 'warehouse',
}

assert KAFKA.get('GROUP_ID'), 'Add kafka GROUP_ID to kafka config'
