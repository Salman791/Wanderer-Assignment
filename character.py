from random import *
from floor import Floor
from resource import Resource


Wall = [[3, 0], [3, 1],
        [3, 2], [2, 2],
        [2, 2], [1, 2],
        [5, 1], [5, 2],
        [5, 3], [5, 4],
        [6, 4], [7, 4],
        [8, 4], [7, 1],
        [8, 1], [7, 2],
        [8, 2], [0, 4],
        [1, 4], [2, 4],
        [3, 4], [1, 5],
        [1, 6], [3, 5],
        [3, 6], [5, 6],
        [6, 7], [6, 6],
        [5, 7], [8, 6],
        [8, 7], [8, 8],
        [1, 8], [2, 8],
        [3, 8], [3, 9],
        [5, 9], [6, 9]]



image_size = 72
board_size = 10


class Character(object):

    def __init__(self, X, Y, canvas, resource):

        self.canvas = canvas
        self.resource = resource
        self.attack = False

        self.fighting = False

        self.X = X
        self.Y = Y
        self.direction = "Hero-down"
        self.turn = 0

        self.HP = 20 + 3 * randint(1, 6)
        self.max_HP = self.HP
        self.DP = 2 * randint(1, 6)
        self.SP = 5 + randint(1, 6)

        if self.turn == 0:
            floor = Floor(board_size, self)
            floor.draw(self.canvas, self.resource, image_size)
            self.show_stat()

    def show_stat(self):

        self.canvas.create_text(image_size * (board_size - 1.9), image_size * (board_size - 1 / 2),
                                font=("Arial", 19), text=f"HP:{round(self.HP, 1)} SP:{self.SP} DP:{self.DP}")

        if self.fighting:
            self.canvas.create_text(image_size * 3, image_size * (board_size - 1 / 2), font=("Arial", 19), \
                                    text=f"{self.villain_stat.villain_type.title()} level {self.villain_stat.level} HP:{self.villain_stat.HP} SP:{self.villain_stat.SP} DP:{self.villain_stat.DP}",
                                    fill="red")

    def get_monster_stat(self, villain):

        self.villain_stat = villain


    def level_up(self):

        self.max_HP = self.max_HP + randint(1, 6)
        self.DP = self.DP + randint(1, 6)
        self.SP = self.SP + randint(1, 6)

    def movement(self, e):


        if not self.fighting:

            if e.keycode == 38:


                self.Y = self.Y - 1
                self.direction = "Hero-up"


                self.turn = self.turn + 1


                if self.Y == -1 or [self.X, self.Y] in Wall:
                    self.Y = self.Y + 1



            elif e.keycode == 40:

                self.Y = self.Y + 1
                self.direction = "Hero-down"


                self.turn = self.turn + 1

                if self.Y == 10 or [self.X, self.Y] in Wall:
                    self.Y = self.Y - 1



            elif e.keycode == 37:


                self.X = self.X - 1
                self.direction = "Hero-left"


                self.turn = self.turn + 1


                if self.X == -1 or [self.X, self.Y] in Wall:
                    self.X = self.X + 1



            elif e.keycode == 39:

                self.X = self.X + 1
                self.direction = "Hero-right"


                self.turn = self.turn + 1

                if self.X == 10 or [self.X, self.Y] in Wall:
                    self.X = self.X - 1


        else:


            if e.keycode == 32:
                self.attack = True


        if self.turn % 2 == 0:

            villain_move = True



        else:

            villain_move = False

        floor = Floor(board_size, self, self.direction)

        if villain_move and not self.fighting:

            floor = Floor(board_size, self, self.direction, villain_move)
            floor.draw(self.canvas, self.resource, image_size)
            self.show_stat()



        else:
            floor.draw(self.canvas, self.resource, image_size)
            self.show_stat()

    def dead(self):

        self.__init__(0, 0, self.canvas, self.resource)
        print("Better luck next time!")

    def next_level(self):

        self.X = 0
        self.Y = 0
        self.direction = "Hero-down"
        self.turn = 0

        chance = randint(1, 10)


        if chance < 6:
            self.HP = self.HP + (self.max_HP / 10)


        elif chance == 6:
            self.HP = self.max_HP

        else:
            self.HP = self.HP + (self.max_HP / 3)

        grid = Floor(board_size, self)
        grid.draw(self.canvas, self.resource, image_size)
        print("Level Up!")

    def draw(self, canvas, resource, image_size):

        canvas.create_image(self.X * image_size + (image_size / 2), self.Y * image_size + (image_size / 2),
                            image=resource.get_image(self.direction))