import curses
from curses import wrapper
import time

'''
moving_word = 0
while moving_word < 100:
    moving_word += 1
    time.sleep(1)
'''

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)

    stdscr.clear()
    stdscr.addstr(10, 10, 'hello world', curses.color_pair(1))

    stdscr.refresh()
    stdscr.getch()

wrapper(main)