from random import *

board_size = 10

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


class Villain():

    def __init__(self, monster_number, monster_x, monster_y, level):

        self.villain_number = monster_number
        self.villain_x = monster_x
        self.villain_y = monster_y
        self.villain_type = "Skeleton"
        self.key_bearer = False
        self.alive = True


        self.level = level
        level_chance = randint(1, 10)

        if 5 < level_chance:

            self.level = self.level + 1

        elif level_chance == 5:

            self.level = self.level + 2


        if self.villain_number == 0:

            self.villain_type = "Boss"


        elif self.villain_number == 1:
            key_bearer = True


        if self.villain_type == "Boss":

            self.HP = 2 * self.level * randint(1, 6) + randint(1, 6)
            self.DP = self.level / 2 * randint(1, 6) + randint(1, 6) / 2
            self.SP = self.level * randint(1, 6) + self.level


        else:
            self.HP = 2 * self.level * randint(1, 6)
            self.DP = self.level / 2 * randint(1, 6)
            self.SP = self.level * randint(1, 6)



    def dead(self):



        self.villain_x = 100
        self.villain_y = 100
        self.alive = False


    def move(self):

        if self.alive:

            moved = False
            directions = [0, 1, 2, 3]

            while not moved:


                direction = choice(directions)

                if direction == 0:
                    self.villain_y = self.villain_y - 1


                    if [self.villain_x, self.villain_y] in Wall or [self.villain_x,
                                                                    self.villain_y] in villains.positions or self.villain_y == -1:
                        self.villain_y = self.villain_y + 1
                        directions.remove(0)


                    else:
                        moved = True


                elif direction == 1:
                    self.villain_y = self.villain_y + 1


                    if [self.villain_x, self.villain_y] in Wall or [self.villain_x,
                                                                    self.villain_y] in villains.positions or self.villain_y == 10:
                        self.villain_y = self.villain_y - 1
                        directions.remove(1)


                    else:
                        moved = True


                elif direction == 2:
                    self.villain_x = self.villain_x + 1


                    if [self.villain_x, self.villain_y] in Wall or [self.villain_x,
                                                                    self.villain_y] in villains.positions or self.villain_x == 10:
                        self.villain_x = self.villain_x - 1
                        directions.remove(2)


                    else:
                        moved = True


                elif direction == 3:

                    self.villain_x = self.villain_x - 1


                    if [self.villain_x, self.villain_y] in Wall or [self.villain_x,
                                                                    self.villain_y] in villains.positions or self.villain_x == -1:
                        self.villain_x = self.villain_x + 1
                        directions.remove(3)


                    else:
                        moved = True


                if len(directions) == 0:
                    moved = True

        villains.positions[self.villain_number] = [self.villain_x, self.villain_y]

    def draw(self, canvas, resource, image_size):

        canvas.create_image(self.villain_x * image_size + (image_size / 2),
                            self.villain_y * image_size + (image_size / 2), image=resource.get_image(self.villain_type))


class Villains():

    def __init__(self, level):

        villain_count = randint(3, 6)

        self.villains = []
        self.positions = []
        self.level = level

        while len(self.positions) < villain_count:


            position = [randint(3, board_size - 1), randint(3, board_size - 1)]


            if position not in Wall and position not in self.positions:
                self.positions.append(position)

        for i in range(len(self.positions)):
            villain = Villain(i, self.positions[i][0], self.positions[i][1], self.level)
            self.villains.append(villain)

    def moving(self):
        for i in range(len(self.villains)):
            self.villains[i].move()

    def next_level(self, restart=False):

        self.level = self.level + 1

        if restart:
            self.level = 1
        self.__init__(self.level)


villains = Villains(1)
