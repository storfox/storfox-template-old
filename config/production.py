from .development import *

ENV = "production"

SENTRY_CONFIG = {
    "DSN": os.environ.get("SENTRY_DSN"),
    'TRACES_SAMPLE_RATE': 1.0,
}

assert SENTRY_CONFIG.get('DSN'), 'Add sentry dsn'
