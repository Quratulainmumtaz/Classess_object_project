from inheritance_example import polygon
class triangle(polygon):
    def area_of_triangle(self):
        return self.get_width() * self.get_height() / 2