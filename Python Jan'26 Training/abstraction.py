from abc import ABC, abstractmethod


class ACRemote(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    def increase_speed(self):
        pass

    def decrease_speed(self):
        pass

    @abstractmethod
    def set_mode(self, type):
        pass

    def set_time(self):
        pass

    def unset_time(self):
        pass

    def switch_hot_mode(self):
        pass

    def switch_cold_mode(self):
        pass


class HaierACRemote(ACRemote):
    def on(self):
        print("Turning On the AC")

    def off(self):
        print("Turing off the AC")

    def set_mode(self, type):
        print(f"AC Setted to {type}")

obj1 = HaierACRemote()
obj1.on()
obj1.off()
obj1.set_mode("Test")