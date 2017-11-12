# coding=utf-8

"""
RPN calculator for CLI
"""

import argparse
import decimal
import sys

import six
import zenhan

__author__ = 'Masaya SUZUKI'
__version__ = '1.2.1.1'


class RPNCalculator:
    """
    RPN Calculator
    """

    def __init__(self):
        self._clear_buffer()
        self._stack = list()
        self._operators = {
            ' ': lambda: self._push(),
            '+': lambda: self._calculate(lambda x, y: x + y),
            '-': lambda: self._calculate(lambda x, y: x - y),
            '*': lambda: self._calculate(lambda x, y: x * y),
            '/': lambda: self._calculate(lambda x, y: x / y),
            '%': lambda: self._calculate(lambda x, y: x % y),
            '^': lambda: self._calculate(lambda x, y: x ** y)
        }

    def start(self, formula=None):
        """
        start to calculate
        :param formula: formula
        """
        if formula:
            self._execute(str_to_unicode_python2(formula))
        else:
            try:
                while True:
                    self._execute(str_to_unicode_python2(six.moves.input('> ')))
            except EOFError:  # exit when the input ended
                exit(0)

    def _clear_buffer(self):
        """
        clear the buffer
        """
        self._buffer = ''

    def _push(self, value=None):
        """
        push the stack
        :param value: value
        """
        if self._buffer or value:
            self._check_push(value)
            self._do_push(value)

    def _check_push(self, value):
        """
        check if push is possible
        :param value: value
        """
        if self._buffer and value:
            raise AttributeError('Duplicate Value')

    def _do_push(self, value):
        """
        push the stack
        :param value: value
        """
        if self._buffer:
            try:
                value = decimal.Decimal(self._buffer)
            except decimal.InvalidOperation:
                raise AttributeError(str(self._buffer))

            self._clear_buffer()

        self._stack.append(value)

    def _calculate(self, method):
        """
        calculate
        :param method: calculate method
        """
        self._push()
        y = self._stack.pop()
        x = self._stack.pop()
        try:
            self._push(method(x, y))
        except decimal.DivisionByZero:
            raise ZeroDivisionError()

    def _execute(self, line):
        """
        execute a line
        :param line: line
        """
        for s in zenhan.z2h(line).strip() + ' ':
            if s in self._operators:
                self._operators[s]()
            else:
                self._buffer += s

        print(self._stack[-1])


def str_to_unicode_python2(s):
    """
    in Python 2.x, convert str to unicode
    :param s: str
    :return: unicode
    """
    if six.PY2 and isinstance(s, str):
        s = s.decode(sys.getfilesystemencoding())

    return s


def main():
    """
    main function
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     prog='RPN Calculator')
    parser.add_argument('-e', '--execute', type=str, help='calculation formula')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {0}'.format(__version__))
    args = parser.parse_args()

    RPNCalculator().start(args.execute)


# main process
if __name__ == '__main__':
    main()
