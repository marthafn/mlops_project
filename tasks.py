from invoke import task
import os

@task
def python(ctx):
    """ """
    ctx.run("which python" if os.name != "nt" else "where python")
    ctx.run("which python" if os.name != "nt" else "where python")
    
@task
def git(ctx, m):
    ctx.run(f"git add .")
    ctx.run(f"git commit -m '{m}'")
    ctx.run(f"git push")