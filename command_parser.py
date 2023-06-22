import re

def parse_command(command):
    protocol, action, *args = command.split(", ")
    parsed_command = {"protocol": protocol, "action": action}

    for arg in args:
        key, value = arg.split("=")
        parsed_command[key] = value

    return parsed_command
