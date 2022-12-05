import pyfiglet
import click

def print_banner():
    banner = pyfiglet.figlet_format("solscan")
    print(banner)
    click.echo('''smart contracts vulnerability scanner \n

Tool is avaliable under MIT license.
Authors:
    @riczardo
    @BartekM101
    @florkie


    ''')
