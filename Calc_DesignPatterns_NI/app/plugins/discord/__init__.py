import sys
from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        print(f'Sending something to discord')