# coding=utf-8

"""
RPN calculator
"""

import argparse

import six

# 作者
__author__ = 'Masaya SUZUKI'

# バージョン
__version__ = '1.1'


class Stack(list):
    """
    Stack
    """

    def push(self, v):
        """
        push the value
        :param v:value
        """
        self.append(v)
        print(v)


# メイン処理
if __name__ == '__main__':
    # コマンドライン引数を解析
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version='%(prog)line {0}'.format(__version__))
    args = parser.parse_args()

    # Stack
    stack = Stack()

    while True:
        try:
            # 入力を取得
            line = six.moves.input('> ').strip()

            # 演算子が入力されたとき、演算を行う
            if line.endswith('+') or line.endswith('-') \
                    or line.endswith('*') or line.endswith('/') or line.endswith('%') or line.endswith('^'):
                # 数値をStackにpush
                if 1 < len(line):
                    stack.push(float(line[:-1]))

                # 一時Stack
                # (このStackからpopすると、演算の順番通りに数値が取り出せる)
                stack_tmp = [stack.pop() for i in range(2)]

                if line.endswith('+'):  # 加算のとき
                    stack.push(stack_tmp.pop() + stack_tmp.pop())
                elif line.endswith('-'):  # 減算のとき
                    stack.push(stack_tmp.pop() - stack_tmp.pop())
                elif line.endswith('*'):  # 乗算のとき
                    stack.push(stack_tmp.pop() * stack_tmp.pop())
                elif line.endswith('/'):  # 除算のとき
                    stack.push(stack_tmp.pop() / stack_tmp.pop())
                elif line.endswith('%'):  # 剰余のとき
                    stack.push(stack_tmp.pop() % stack_tmp.pop())
                elif line.endswith('^'):  # 累乗のとき
                    stack.push(stack_tmp.pop() ** stack_tmp.pop())
            else:  # 数値が入力されたとき、数値をStackにpush
                stack.push(float(line))
        except EOFError:  # 入力が終了したとき、ループを抜ける
            break
