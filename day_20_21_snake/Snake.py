from Square import Square

__vertical__ = ["up", "down"]
__horizontal__ = ["left", "right"]

class Snake:
    def __init__(self):
        self.size = 3
        self.__current_direction__ = 'up'
        self.__movement_vector__ = (20, 0)
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

        if self.no_walls:
            if x > 280 or x < - 280:
                x *= -1
            if y > 280 or y < - 280:
                y *= -1

        return x, y

    def right(self):
        if self.__current_direction__ != "left":
            self.set_direction("right")
            self.__movement_vector__ = (20, 0)

    def left(self):
        if self.__current_direction__ != "right":
            self.set_direction("left")
            self.__movement_vector__ = (-20, 0)

    def up(self):
        if self.__current_direction__ != "down":
            self.set_direction("up")
            self.__movement_vector__ = (0, 20)

    def down(self):
        if self.__current_direction__ != "up":
            self.set_direction("down")
            self.__movement_vector__ = (0, -20)

    def set_direction(self, direction):
        self.__current_direction__ = direction
