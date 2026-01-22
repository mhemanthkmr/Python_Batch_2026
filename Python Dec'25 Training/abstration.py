from abc import ABC, abstractmethod


class MobilePhone(ABC):
    @abstractmethod
    def switch_on(self):
        pass

    @abstractmethod
    def switch_off(self):
        pass

    @abstractmethod
    def make_a_call(self):
        pass

    @abstractmethod
    def open_camera(self):
        pass

    @abstractmethod
    def gallery(self):
        pass

    @abstractmethod
    def file_manager(self):
        pass

    @abstractmethod
    def contact_manager(self):
        pass

    def ir_blaster(self):
        print("Utilizing IR Blaster")

class Vivo(MobilePhone):
    def switch_on(self):
        print("Switching On....")

    def make_a_call(self):
        print("Making a Call....")

    def open_camera(self):
        print("Opening Camera ...")

    def gallery(self):
        print("Opening Gallery...")

    def file_manager(self):
        print("Opening FileMangaer...")

    def contact_manager(self):
        print("Opening Contact Manager...")  

    def switch_off(self):
        print("Switching Off...")


obj1 = Vivo()
obj1.switch_on()
obj1.open_camera()
obj1.contact_manager()
obj1.ir_blaster()
obj1.switch_off()