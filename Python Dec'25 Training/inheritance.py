class GrandFather():
    def land(self):
        print("2 Acres of Land")

class Father(GrandFather):
    def land(self):
        print("4 Acres of Land")

    def gold(self):
        print("200 grams of Gold")

class Son(Father):
    def car(self):
        print("Tata Punch")

son1 = GrandFather()
son1.land()
son1.gold()
son1.car()

