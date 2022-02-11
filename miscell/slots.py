
class SlotsExample:
    __slots__ = ('x', 'y')

    def __init__(self):
        self.x = 10
        self.y = 20
        # self.z = 30


c = SlotsExample()

print(c.__dict__)
