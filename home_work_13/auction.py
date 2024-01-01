class Auction:
    def __init__(self, name, lot):
        self.lot = lot
        self.name = name

    def __ge__(self, other):
        if isinstance(other, Auction):
            if self.lot >= other.lot:
                return f"{person_1.name} donat more than {person_2.name}"
            else:
                return f"{person_2.name} donat more than {person_1.name}"
        raise TypeError


person_1 = Auction("Ivan", 5000)
person_2 = Auction("Luka", 800)
print(person_1 >= person_2)
