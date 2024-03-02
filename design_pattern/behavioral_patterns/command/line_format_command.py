from .abstract_command import AbstractCommand
from .receiver import Receiver


class LineFormatCommand(AbstractCommand):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.write_text()
        print('Lines formatted')
