"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 7         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        dx = graphics.get_dx()                                          # get dx from breakoutgraphics.py
        dy = graphics.get_dy()                                          # get dy from breakoutgraphics.py
        graphics.ball.move(dx, dy)
        pause(FRAME_RATE)
        if num_lives > 0:
            if graphics.ball.y >= graphics.window.height:   # if the ball hitting the bottom of the window
                num_lives -= 1
        else:                                                             # if the lives equals to 0
            break                                                         # end the while loop
        if graphics.bricks_total == graphics.score:                       # if pass the game
            break                                                         # end the while loop


if __name__ == '__main__':
    main()
