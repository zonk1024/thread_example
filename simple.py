#!/usr/bin/env python

from logging import getLogger, StreamHandler, INFO
from random import randint
from sys import argv, stdout
from termcolor import colored
from threading import Thread
from time import sleep

TICK_COUNT_DEFAULT = 10

DELAY_MIN = 250
DELAY_MAX= 2500

COLORS = [
    # 'grey',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
]

logger = getLogger(__name__)
logger.addHandler(StreamHandler(stdout))
logger.setLevel(INFO)


if len(argv) >= 2:
    try:
        thread_count = int(argv[1])
    except ValueError:
        thread_count = len(COLORS)
else:
    thread_count = len(COLORS)


if len(argv) >= 3:
    try:
        tick_count = int(argv[2])
    except ValueError:
        tick_count = TICK_COUNT_DEFAULT
else:
    tick_count = TICK_COUNT_DEFAULT


def print_this_every(i, delay=10):
    cnt = 0
    while cnt < tick_count:
        logger.info(colored('Thread {} tick {} with delay {}'.format(i, cnt, delay), COLORS[i % len(COLORS)]))
        cnt += 1
        sleep(delay/1000.0)


pool = [None for _ in range(thread_count)]

for i, _ in enumerate(pool):
    delay = randint(DELAY_MIN, DELAY_MAX)
    pool[i] = Thread(target=print_this_every, args=(i, delay))
    pool[i].daemon = True
    pool[i].start()

for i, _ in enumerate(pool):
    pool[i].join()
