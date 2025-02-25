from Square import Square
from common import SCREEN_SIZE

LEFT = (-20, 0)
RIGHT = (20, 0)
UP = (0, 20)
DOWN = (0, -20)

class Snake:
    def __init__(self):
        self.size = 16
        self.__movement_vector__ = RIGHT
        self.no_walls = True
        body = [Square()]
        for i in range(1, self.size):
            previous_square =  body[i - 1]
            square = Square(previous_square.get_x() - 20, previous_square.get_y())
            body.append(square)

        self.body = body
        self.head = self.body[0]

    def move(self):
        new_head = self.body.pop()
        new_coord = self.__get_new_coord__()
        new_head.set_coord(x_coord=new_coord[0], y_coord=new_coord[1])
        self.body.insert(0, new_head)
        self.head = self.body[0]

    def __get_new_coord__(self):
        x = self.head.get_x() + self.__movement_vector__[0]
        y = self.head.get_y() + self.__movement_vector__[1]

        screen_abs_size = SCREEN_SIZE / 2

        if self.no_walls:
            if x >= screen_abs_size or x <= - screen_abs_size:
                x = x * -1 + 20 * (x / screen_abs_size)
            if y >= screen_abs_size or y <= - screen_abs_size:
                y = y * -1 + 20 * (y / screen_abs_size)
        return x, y

    def right(self):
        if self.__movement_vector__ != LEFT:
            self.__movement_vector__ = RIGHT

    def left(self):
        if self.__movement_vector__ != RIGHT:
            self.__movement_vector__ = LEFT

    def up(self):
        if self.__movement_vector__ != DOWN:
            self.__movement_vector__ = UP

    def down(self):
        if self.__movement_vector__ != UP:
            self.__movement_vector__ = DOWN

    def eat(self):
        last_square = self.body[self.size - 1]
        self.size += 1
        new_square = Square(last_square.get_x(), last_square.get_y())
        self.body.append(new_square)
