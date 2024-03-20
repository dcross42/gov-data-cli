""" 
Main app script
"""

import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Example Code
    """

@app.command()
def foo():
    """
    First command
    """
    typer.echo("Echoing First Command")

@app.command()
def bar():
    """
    Second Command
    """
    typer.echo("Echoing Second Command")
