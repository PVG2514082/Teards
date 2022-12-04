import sys
import os

import form_of_login
import choice_of_board


def main():
    sys.path.append(os.curdir)
    cx, em = form_of_login.start()
    if em:
        choice_of_board.start(cx[0])


if __name__ == '__main__':
    main()
