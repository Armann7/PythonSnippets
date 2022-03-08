class A:
    def __init__(self):
        super().__init__()
        self.aa = 2


class B:
    def __init__(self):
        # super().__init__()
        self.ab = 3


class C(A, B):
    def __init__(self):
        super().__init__()


c = C()

print(C.mro())
print(c.aa, c.ab)
