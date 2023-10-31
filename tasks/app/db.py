import logging

from invoke import task


log = logging.getLogger(__name__)


@task
def revision(context, message=None):
    """
    Make migrations
    """
    log.info("Make migrations...")
    context.run(f'alembic revision --autogenerate -m "{message}"')
    log.info("Finished migrating.")


@task
def migrate(context):
    """
    Migrate
    """
    log.info("Migrate...")
    context.run(f'alembic upgrade head')
    log.info("Finished migrate.")