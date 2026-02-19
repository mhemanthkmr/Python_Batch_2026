class GrandFather:
    def __land(self):
        print("5 Acres of Land")

    def use_land(self):
        self.__land()

class Father():
    def gold(self):
        print("200 grms of Gold")

class Son(Father, GrandFather):
    def car(self):
        print("Tata Nexon")

son = Son()
son.car()
son.gold()

grndfthr1 = GrandFather()
grndfthr1.use_land()