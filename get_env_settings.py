import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

SECRET_KEY = env("SC_SECRET_KEY")
DEBUG = eval(env("SC_DEBBUG"))
SC_DB_NAME = env('SC_DB_DATABASE')
SC_DB_USER = env('SC_DB_USER')
SC_DB_PASSWORD = env('SC_DB_PASSWORD')
SC_DB_HOST = env('SC_DB_ADDR')
SC_DB_PORT = env('SC_DB_PORT')
SC_DB_SCHEME = env("SC_DB_SCHEME")
DJANGO_SUPERUSER_USERNAME = env("DJANGO_SUPERUSER_USERNAME")
ENGINE = env('SC_DB_ENGINE')
CHARSET = env('SC_DB_CHARSET')
TIME_ZONE = env('SC_DB_TIME_ZONE')
