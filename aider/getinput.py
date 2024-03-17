import sys


class InputOutputHandler:
    def __init__(self, output=sys.stdout):
        self.output = output

    def display_usage_cost(self, cost):
        message = f"Total usage cost: ${cost:.2f}"
        self.output.write(message + '\n')

def get_input_output_handler(output=sys.stdout):
    return InputOutputHandler(output=output)
