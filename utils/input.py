import json

from utils.colors import *


class InputManager:
    """
    InputManager give us ability to get input from users
    """

    @classmethod
    def __get_command_type(cls):
        """
        in this method we get type of commands which user just can input compute and os.
        :return: commands type
        """
        command_type_input = str(input(f'{BOLD}{YELLOW}Chose your command type(os or compute):'))
        if command_type_input not in ('os', 'compute'):
            print(f'{RED}Your chose incorrect!')
            return cls.__get_command_type()
        return command_type_input

    @classmethod
    def __get_os_command(cls):
        """
        here we have command type which we now get command from user and user can't input None.
        :return: command
        """
        user_command_input = str(input(f'{BOLD}{YELLOW}Input your command:')).split(' ')
        if '' in user_command_input:
            print(f'{RED}Your command incorrect!')
            return cls.__get_os_command()
        return user_command_input

    @classmethod
    def __get_compute_expression(cls):
        """
        here we have command type which we now get expression from user and check it's correct input.
        :return: expression like: 19 * 5 - 4
        """
        user_command_input = str(input(f'{BOLD}{YELLOW}Input your math expression:'))
        try:
            eval(user_command_input)
        except SyntaxError:
            print(f'{RED}Your expression incorrect!')
            return cls.__get_compute_expression()
        return user_command_input

    @staticmethod
    def __generate_os_data(command_type, command):
        """
        here we have command type and command which we create it's json data
        :param command_type: os
        :param command: command like: ls -r -l
        :return: json data
        """
        return json.dumps(dict(command_type=command_type, command_name=command.pop(0), parameters=command))

    @staticmethod
    def __generate_compute_data(command_type, math):
        """
        here we have command type and expression which we create it's json data
        :param command_type: compute
        :param math: expression which user input like: 19 * 5 - 4
        :return: json data
        """
        return json.dumps(dict(command_type=command_type, expression=math))

    @classmethod
    def create_data(cls):
        """
        we get command type from user and by that we choose what user should give to us
        :return: command type and user input
        """
        command_type = cls.__get_command_type()

        if command_type == 'os':
            command = cls.__get_os_command()
            data = cls.__generate_os_data(command_type, command)
        else:
            command = cls.__get_compute_expression()
            data = cls.__generate_compute_data(command_type, command)

        return command_type, command, data
