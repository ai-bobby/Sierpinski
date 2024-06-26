# -------------------------------------------------------------
# sierpinski.py
# -------------------------------------------------------------
import random
import sys

from module import stddraw
from module.stddraw import RED, GREEN, BLUE
from module import stdrandom
import color

'''
Accept integer n as a command-line argument. Play chaos game on
triangle to produce Sierpinski triangle of n points.
'''


def main():
    n = int(sys.argv[1])

    cx = [0.000, 1.000, 0.500]
    cy = [0.000, 0.000, 0.866]

    x = 0.0
    y = 0.0
    colors = [RED, GREEN, BLUE]

    stddraw.setPenRadius(0.0)
    for i in range(n):
        r = random.randrange(0, 3)
        x = (x + cx[r]) / 2.0
        y = (y + cy[r]) / 2.0
        stddraw.setPenColor(colors[r])
        stddraw.point(x, y)
        stddraw.show(0)

    stddraw.show()


if __name__ == '__main__':
    main()
