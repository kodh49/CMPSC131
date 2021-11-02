# Python manim codes would look like this.
from manim import * # import everything from manim library
import numpy as np

class MySimpleClass(Scene):
    def construct(self):
        # Define objects
        circle = Circle()
	circle.set_fill(PINK, opacity=0.5)
	square = Square()
	square.rotate(np.pi/4)
	# Animate objects
	self.play(Create(square))
	self.play(Transform(square, circle))
	self.play(FadeOut(square))


class CreatingMobjects(Scene):
    def construct(self):
        # Create and display mobjects
        circle = Circle()
        self.add(circle)
        self.wait(1) # Measured in millisec/sec?
        self.remove(circle)
        self.wait(1)

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # Place the circle two units left from the origin
        circle.shift(LEFT*2)
        # Place the square to the left of the circle
        circle.next_to(circle, LEFT)
        # Align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)

class 
