
DEBUG = True

TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "Pup",
        # Not used with sqlite3.
        "USER": "phil4485",
        # Not used with sqlite3.
        "PASSWORD": "dp|$ea1",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
