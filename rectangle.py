from inheritance_example import polygon
class rangular(polygon):
    def area_of_rectangular(self):
        return self.get_width() * self.get_height()