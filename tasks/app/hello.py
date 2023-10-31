from invoke import task

@task(default=True)
def run(context):
    print("HELLO!")