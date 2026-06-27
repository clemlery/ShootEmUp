class Player:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def moove(self, movement: tuple[int]):
        try:
            self.x += movement[0]
            self.y += movement[1]
        except TypeError:
            raise TypeError("The parameter you entered is not a tuple or contain less than 2 elements.")
        
    def draw(self):
        # TODO
        pass