class ParserMessage:
    """
    in parser message we can get messages
    and by command_type we can parse data to compute and OS commands
    """

    @staticmethod
    def __parse_os_command(msg):
        """
        :param msg:  message come from client
        :return: command + parameters
        """
        return f'{msg.get("command_name")} {" ".join(msg.get("parameters"))}'.strip()

    @staticmethod
    def __parse_compute_expression(msg):
        """
        :param msg: message come from client
        :return: expression
        """
        return msg.get("expression")

    @classmethod
    def parse(cls, msg):
        """
        we give msg to parsers by command type
        :param msg: message which come from client
        :return: if command type is os return command and parameters in one string and if command type is compute
        return expression
        """
        command_type = msg.get('command_type')
        if command_type == 'os':
            return command_type, cls.__parse_os_command(msg)
        return command_type, cls.__parse_compute_expression(msg)
