import sys
from app.commands import Command


class EmailCommand(Command):
    def execute(self):
        print(f'An email will be sent to you')