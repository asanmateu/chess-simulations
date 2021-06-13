class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def move(self, delta_x, delta_y):
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist_from(self, other):
        ox = other.x
        oy = other.y
        x_dist = self.x - ox
        y_dist = self.y - oy
        return (x_dist**2 + y_dist**2)**0.5
