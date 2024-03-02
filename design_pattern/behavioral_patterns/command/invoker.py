from design_pattern.behavioral_patterns.command.abstract_command import AbstractCommand


class Invoker:
    def write_and_format(self, command: AbstractCommand):
        command.execute()

    def save_document(self, command: AbstractCommand):
        command.execute()
