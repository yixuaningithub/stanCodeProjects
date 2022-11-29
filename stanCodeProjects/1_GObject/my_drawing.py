"""
File: my_drawing.py
Name: Yi-Syuan Chung
----------------------
Title: The GOAT

Roger Federer，永遠的傳奇。他的logo取自名字開頭"RF"，看起來只有"F"字，但左側加入了"R"的弧線，很有巧思。
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow
window = GWindow(600, 600, title='The GOAT')


def main():
    """
    TODO:
    """
    rect_1 = GRect(600, 600)
    window.add(rect_1)
    rect_1.filled = True
    rect_1.fill_color = 'white'

    rect_2 = GRect(150, 60, x=300, y=120)
    window.add(rect_2)
    rect_2.filled = True
    rect_2.fill_color = 'black'

    oval_1 = GOval(300, 120, x=150, y=120)
    window.add(oval_1)
    oval_1.filled = True
    oval_1.fill_color = 'white'
    oval_1.color = 'white'

    rect_3 = GRect(90, 120, x=300, y=180)
    window.add(rect_3)
    rect_3.filled = True
    rect_3.fill_color = 'black'

    oval_2 = GOval(180, 120, x=210, y=120)
    window.add(oval_2)
    oval_2.filled = True
    oval_2.fill_color = 'white'
    oval_2.color = 'white'

    oval_3 = GOval(180, 120, x=210, y=240)
    window.add(oval_3)
    oval_3.filled = True
    oval_3.fill_color = 'white'
    oval_3.color = 'white'

    oval_4 = GOval(240, 120, x=60, y=120)
    window.add(oval_4)
    oval_4.filled = True
    oval_4.fill_color = 'black'
    oval_4.color = 'black'

    oval_5 = GOval(150, 108, x=105, y=126)
    window.add(oval_5)
    oval_5.filled = True
    oval_5.fill_color = 'white'
    oval_5.color = 'white'

    rect_4 = GRect(120, 120, x=60, y=120)
    window.add(rect_4)
    rect_4.filled = True
    rect_4.fill_color = 'white'
    rect_4.color = 'white'

    oval_6 = GOval(300, 210, x=30, y=234)
    window.add(oval_6)
    oval_6.filled = True
    oval_6.fill_color = 'black'
    oval_6.color = 'black'

    rect_5 = GRect(150, 210, x=30, y=234)
    window.add(rect_5)
    rect_5.filled = True
    rect_5.fill_color = 'white'
    rect_5.color = 'white'

    rect_6 = GRect(150, 105, x=180, y=339)
    window.add(rect_6)
    rect_6.filled = True
    rect_6.fill_color = 'white'
    rect_6.color = 'white'

    oval_7 = GOval(210, 210, x=75, y=240)
    window.add(oval_7)
    oval_7.filled = True
    oval_7.fill_color = 'white'
    oval_7.color = 'white'

    oval_8 = GOval(105, 105, x=292, y=333)
    window.add(oval_8)
    oval_8.filled = True
    oval_8.fill_color = 'black'
    oval_8.color = 'black'

    oval_9 = GOval(84, 120, x=327, y=300)
    window.add(oval_9)
    oval_9.filled = True
    oval_9.fill_color = 'white'
    oval_9.color = 'white'

    poly = GPolygon()
    poly.add_vertex((287, 339))
    poly.add_vertex((330, 339))
    poly.add_vertex((336, 396))
    poly.add_vertex((292, 385))
    poly.add_vertex((290, 360))
    poly.filled = True
    poly.fill_color = 'black'
    window.add(poly)


if __name__ == '__main__':
    main()
