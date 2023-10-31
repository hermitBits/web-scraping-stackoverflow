import logging

from invoke import task


log = logging.getLogger(__name__)


@task
def install_python_dependencies(context, force=False):
    """
    Install Python dependencies listed in requirements.txt.
    """
    log.info("Installing project dependencies...")
    context.run(f"pip install -r requirements.txt {'--upgrade' if force else ''}")
    log.info("Project dependencies are installed.")