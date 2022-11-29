"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 5  # Number of rows of bricks
BRICK_COLS = 5  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 2  # Initial vertical speed for the ball
MAX_X_SPEED = 1  # Maximum initial horizontal speed for the ball


class BreakoutGraphicsExtension:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.start_ball = False                                 # if it clicks the mouse
        self.count = 0                                          # count the times that clicking the mouse
        self.bricks_total = brick_cols * brick_rows             # total amounts of bricks
        self.score = 0                                          # count the numbers of removing the bricks
        self.top_space = brick_offset

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2,
                        y=window_height - paddle_offset - paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius * 2) / 2, y=(window_height - ball_radius * 2) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # self.set_ball_velocity()                                  # at function get_dx(), get_dy()

        # Initialize our mouse listeners
        onmousemoved(self.move_mouse)
        onmouseclicked(self.move_ball)

        # Draw bricks
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        y = brick_offset
        for i in range(5):
            for j in range(brick_rows // 5):
                x = 0
                for k in range(brick_cols):
                    self.brick = GRect(brick_width, brick_rows)
                    self.brick.filled = True
                    self.brick.fill_color = colors[i]
                    self.window.add(self.brick, x=x, y=y)
                    x += brick_spacing + brick_width
                y += brick_height

        # set the label
        self.word = "Scores:", self.score
        self.label = GLabel(self.word, x=0, y=self.top_space)
        self.label.font = '-20'
        self.window.add(self.label)

    # the ball is in the initial statement, dx,dy=0, ball at the middle of the window
    def initial_statement(self):
        self.start_ball = False
        self.count = 0
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self.__dx = 0
        self.__dy = 0

    # move paddle
    def move_mouse(self, mouse):
        if mouse.x + self.paddle.width / 2 <= self.paddle.width:
            self.paddle.x = 0
        elif mouse.x - self.paddle.width / 2 >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
        self.window.add(self.paddle)

    # click mouse and start ball moving
    def move_ball(self, mouse):
        self.count += 1
        self.start_ball = True
        if self.start_ball and self.count == 1:                 # if only clicking the first time will go this line
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def show_scores(self):
        self.label.text = "Scores:", self.score
        self.window.add(self.label)

    def win_the_game(self):
        pass_game = GLabel("You Win!")
        pass_game.font = '-40'
        pass_game.color = "red"
        self.window.add(pass_game, x=(self.window.width-pass_game.width) // 2, y=self.window.height // 2)

    def lose_the_game(self):
        lose_game = GLabel("You lose!")
        lose_game.font = '-40'
        lose_game.color = "red"
        self.window.add(lose_game, x=(self.window.width - lose_game.width) // 2, y=self.window.height // 2)

    # Getter
    def get_dx(self):
        # if the ball hitting the leftmost and rightmost side of the window, bounce the ball.
        if (self.ball.x <= 0 and self.__dx < 0) or (
                self.ball.x >= self.window.width - self.ball.width and self.__dx > 0):
            self.__dx = -self.__dx
        return self.__dx

    def get_dy(self):
        if self.ball.y <= 0 and self.__dy < 0:                          # if the ball hitting the top of the window
            self.__dy = -self.__dy                                      # bounce the ball
        if self.ball.y >= self.window.height:                           # if the ball hitting the bottom of the window
            self.initial_statement()                                    # go to the initial statement
        repeat = 0                            # if hitting two bricks in the same times, repeat == 1, if no, repeat == 0
        for i in range(0, self.ball.width + 1, self.ball.width):        # check the four vertexes if hitting the object
            for j in range(0, self.ball.height + 1, self.ball.height):
                what_object = self.window.get_object_at(self.ball.x + i, self.ball.y + j)
                if what_object is not None:
                    if self.__dy != 0:
                        if self.top_space < self.ball.y < self.window.height // 2 and repeat == 0:
                            self.window.remove(what_object)
                            self.__dy = -self.__dy
                            self.score += 1
                        elif self.top_space < self.ball.y < self.window.height // 2 and repeat == 1:
                            self.window.remove(what_object)
                            self.score += 1
                        elif self.ball.y > self.window.height // 2 and self.__dy > 0:
                            self.__dy = -self.__dy
                        repeat += 1
                    if self.score == self.bricks_total:                # if the amounts of moving bricks == total bricks
                        self.initial_statement()                   # pass the game, the ball go to the initial statement
        return self.__dy
