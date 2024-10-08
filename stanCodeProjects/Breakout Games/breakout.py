"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

graphics = BreakoutGraphics()
dx = graphics.get_dx()
dy = graphics.get_dy()
first_v = False                             # first assign velocity of dx and dy
live_remain = NUM_LIVES
hit_bricks = 0                              # numbers of bricks are hit


def main():
    global dx, dy, first_v, live_remain
    # Add the animation loop here!
    while live_remain > 0 and hit_bricks < graphics.total_bricks:
        if graphics.start:                  # if click start
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            ball_move()
        pause(FRAME_RATE)


def ball_move():
    global dx, dy, first_v, live_remain, hit_bricks
    graphics.ball.move(dx, dy)
    if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
        dx = -dx
        graphics.set_dx(dx)
    if graphics.ball.y <= 0:
        dy = -dy
        graphics.set_dy(dy)
    elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
        first_v = False
        graphics.initial_statement()
        live_remain -= 1
    hit_once = False

    for i in range(0, graphics.ball.width + 1, graphics.ball.width):
        for j in range(0, graphics.ball.height + 1, graphics.ball.height):
            what_object = graphics.window.get_object_at(graphics.ball.x + i, graphics.ball.y + j)
            if what_object is not None:
                if what_object is not graphics.paddle:          # hit bricks
                    if not hit_once:
                        graphics.window.remove(what_object)
                        hit_bricks += 1
                        hit_once = True
                        dy = -dy
                        graphics.set_dy(dy)
                else:                                           # hit paddle
                    if dy > 0:
                        dy = -dy
                        graphics.set_dy(dy)
    if hit_bricks == graphics.total_bricks:
        graphics.initial_statement()


if __name__ == '__main__':
    main()
