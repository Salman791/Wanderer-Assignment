


class Floor:



    def __init__(self, size, hero, villains_move=False):

        global occupied_by_hero, occupied_by_villains, villain
        self.pause = False

        self.grid = []



        self.wall = [[3, 0], [3, 1],
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


        if villains_move:
            villains.moving()




        for i in range(0, size):

            row = []
            for j in range(0, size):


                if hero.X == i and hero.Y == j:

                    if [i, j] in villains.positions:

                        fight(hero, villains.villains[villains.positions.index([i, j])], villains, villains_move)

                    occupied_by_hero = True


                elif [i, j] in villains.positions:

                    occupied_by_villains = True


                    villain = villains.positions.index([i, j])

                else:
                    occupied_by_hero = False
                    occupied_by_villains = False


                if [i, j] in self.wall:

                    wall_type = "Wall"

                else:

                    wall_type = "Floor"

                if occupied_by_hero:

                    row.append(hero)

                elif occupied_by_villains:

                    row.append(villains.villains[villain])


                else:

                    wall = Wall(i, j, wall_type)
                    row.append(wall)

            if not self.pause:
                self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        if not self.pause:
            for i in range(0, len(self.grid)):

                for j in range(0, len(self.grid)):

                    self.grid[i][j].draw(canvas, resource, image_size)

class Wall:

    def __init__(self, row, column, wall_type):

        self.row = row
        self.column = column
        self.wall_type = wall_type

    def draw(self, canvas, resource, image_size):
        canvas.create_image(self.row * image_size + (image_size/2), self.column * image_size + (image_size/2), image = resource.get_image(self.wall_type))