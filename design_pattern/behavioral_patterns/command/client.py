from design_pattern.behavioral_patterns.command.invoker import Invoker
from design_pattern.behavioral_patterns.command.line_format_command import LineFormatCommand
from design_pattern.behavioral_patterns.command.receiver import Receiver
from design_pattern.behavioral_patterns.command.save_command import SaveCommand

if '__main__' == __name__:
    invoker = Invoker()
    receiver = Receiver()
    formatter = LineFormatCommand(receiver)
    save_command = SaveCommand()

    invoker.write_and_format(formatter)
    invoker.save_document(save_command)
