from .abstract_command import AbstractCommand


class SaveCommand(AbstractCommand):
    def execute(self):
        print("Saving")
