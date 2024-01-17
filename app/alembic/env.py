"""Alembic enviroment file"""

# pylint: disable=E1101,W0611,W0401

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool  # type: ignore

from app.models import *
from app.database.base.session import metadata
from app.utils.tools import env

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config  # type: ignore

section = config.config_ini_section


def set_config(key: str):
    """Set configuration by key"""
    config.set_section_option(section, key, env(key))


set_config("POSTGRES_USER")
set_config("POSTGRES_PASSWORD")
set_config("POSTGRES_HOST")
set_config("POSTGRES_PORT")
set_config("POSTGRES_DB")

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")  # type: ignore
    context.configure(  # type: ignore
        url=url,
        dialect_opts={"paramstyle": "named"},
        target_metadata=target_metadata,
        include_schemas=True,
        literal_binds=True,
    )
    with context.begin_transaction():  # type: ignore
        context.run_migrations()  # type: ignore


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),  # type: ignore
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(  # noqa
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():  # type: ignore
            context.run_migrations()  # type: ignore


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
