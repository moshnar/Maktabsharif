import logging


def log_generator(name, filename):
    log_book = logging.Logger(name, level=logging.INFO)
    file_handler = logging.FileHandler(filename)
    FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    file_handler.setFormatter(FORMATTER)
    log_book.addHandler(file_handler)
    return log_book


calculator_exception_log = log_generator('calc_exception', './logs/calc_exceptions.log')
operand_exception_log = log_generator('oerand_exception', './logs/invalid_operand_exception.log')
operator_exception_log = log_generator('operator_exception', './logs/invalid_operation_exception.log')
format_exception_log = log_generator('format_exception', './logs/invalid_format_exception.log')


class CalcException(Exception):
    def __init__(self):
        calculator_exception_log.error(self.__str__(), exc_info=True)


class InvalidFormatException(CalcException):
    def __init__(self):
        format_exception_log.error(self.__str__(), exc_info=True)
        super().__init__()

    def __str__(self):
        return "Invalid format"


class InvalidNumberException(CalcException):
    def __init__(self):
        operand_exception_log.error(self.__str__(), exc_info=True)
        super().__init__()

    def __str__(self):
        return "number should be int/float"


class InvalidOperatorException(CalcException):
    def __init__(self):
        operator_exception_log.error(self.__str__(), exc_info=True)
        super().__init__()

    def __str__(self):
        return "Invalid operator"
