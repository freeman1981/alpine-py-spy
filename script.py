# just dummy example
import time


def fast():
    time.sleep(.01)


def middle():
    time.sleep(.05)


def slow():
    time.sleep(.1)


if __name__ == '__main__':
    while True:
        fast()
        middle()
        slow()
