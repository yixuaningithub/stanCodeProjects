"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ori_position = True                                                 # if it's at the start position
ball = GOval(SIZE, SIZE, x=START_X-SIZE/2, y=START_Y-SIZE/2)
window.add(ball)
ball.filled = True
vy, count, at_ground = 0, 0, False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(click)


def click(mouse):
    global ball, ori_position, vy, at_ground, count
    if ori_position and count < 3:                            # if it's at the original position but not the third times
        ori_position = False
        vy = 0
    while not ori_position:
        vy += GRAVITY                                               # vertical velocity
        ball.move(VX, vy)
        if ball.y >= window.height and not at_ground:               # if the ball is out of the lower side of the window
            vy = -vy * REDUCE                                       # bounce back
            at_ground = True                                        # shift the if the condition off
        if vy > 0 and at_ground:                                    # shift at_ground on
            at_ground = False
        if ball.x >= window.width:
            ori_position = True
            ball.x = START_X
            ball.y = START_Y
            count += 1
        pause(DELAY)


if __name__ == "__main__":
    main()
