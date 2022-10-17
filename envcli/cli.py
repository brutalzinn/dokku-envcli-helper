import os
from typing import Optional

import typer

from envcli import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True),
) -> None:
    return

@app.command(name="generate")
def generate_env(app: str, execute: bool = False, env_file: str = '.env'):
        with open(env_file) as f:
            envs = ''
            for line in f.readlines():
                line = line.replace('\n', '').split('=')
                key = line[0]
                value = line[1]
                envs += f'{key}="{value}" '
            envs = envs[:-1]
            dokku_command = f'dokku config:set {app} {envs}'
            print(dokku_command)
        #JÁ PENSOU SE EU DOU UM rmdir recursivo aqui?
        if(execute):
             os.system(dokku_command)