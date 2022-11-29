"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphicsExtension

FRAME_RATE = 3         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphicsExtension()
    num_lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        dx = graphics.get_dx()                                          # get dx from breakoutgraphics.py
        dy = graphics.get_dy()                                          # get dy from breakoutgraphics.py
        graphics.ball.move(dx, dy)
        graphics.show_scores()
        pause(FRAME_RATE)
        if num_lives > 0:                                               # if the ball hitting the bottom of the window
            if graphics.ball.y >= graphics.window.height:
                num_lives -= 1
        else:                                                           # if the lives equals to 0
            graphics.lose_the_game()
            break                                                         # end the while loop
        if graphics.bricks_total == graphics.score:                       # if pass the game
            graphics.win_the_game()
            break                                                         # end the while loop


if __name__ == '__main__':
    main()
