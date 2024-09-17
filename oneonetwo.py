import turtle as trtl
color: str = input('what color is a diamond?')

painter = trtl.Turtle()
painter.color(color)

painter.left(45)
painter.forward(100)
painter.left(100)
painter.forward(20) 
painter.left(35)
painter.forward(90)
painter.left(35)
painter.forward(20)
painter.left(90)
painter.forward(100)



wn = trtl.Screen()
wn.mainloop()
