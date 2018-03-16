import os
import click

from pittl import Server


NAME = 'push-it-to-the-limit'
IMG_PATH = os.path.join(os.path.expanduser('~'), 'Pictures/Wedding')


@click.group()
@click.pass_context
def cli(ctx):
    print(f'Started {NAME} CLI')


@cli.command(help='Start server')
@click.option('--host', default='0.0.0.0', help='Host IP')
@click.option('--port', default=5000, help='Port', type=int)
@click.pass_context
def start(ctx, host, port):
    print('Starting server')
    server = Server(host, port)
    server.start()
    print(f'Scan image dir: {IMG_PATH}')





def main():
    cli()
