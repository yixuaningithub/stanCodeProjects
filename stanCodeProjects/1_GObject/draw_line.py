"""
File: draw_line.py
Name: Yi-Syuan Chung
-------------------------
If clicking the mouse for the first time, the window shows a hollow circle.
If clicking the mouse for the next time, the window first removes the circle then shows a line which the starting point
is the center of the hollow circle and the end point is the point where the mouse is pressed.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10
window = GWindow()
count = 0                                                               # count whether is clicking odd or even times
point_x = 0                                                             # x value of the center of the hollow circle
point_y = 0                                                             # y value of the center of the hollow circle


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(mouse):
    global count, point_x, point_y
    if count == 0:                                                          # if clicking odd times
        point = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)       # circle
        window.add(point)
        point_x = mouse.x
        point_y = mouse.y
        count += 1
    else:                                                                   # if clicking even times
        a_point = window.get_object_at(point_x, point_y)                    # find the circle
        window.remove(a_point)                                              # remove the circle
        line = GLine(point_x, point_y, mouse.x, mouse.y)                    # line
        window.add(line)
        count = 0


if __name__ == "__main__":
    main()
