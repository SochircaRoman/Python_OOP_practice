class Container:
    def __init__(self, name: str, volume: int, current_volume: int, pour_out: int = 100) -> None:
        self.__name = name
        self.__volume = volume
        self.current_volume = current_volume
        self.pour_out = pour_out

    def pour_out_liquid(self):
        if self.current_volume > 0:
            self.current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f"{self.__name} empty")
            return 0

    def pour_liquid(self, volume: int) -> None:
        if self.current_volume + volume <= self.__volume:
            self.current_volume += volume
        else:
            print(f"{self.__name} full")

    def info(self):
        print(f"{self.__name} = {self.current_volume}")


def main() -> None:
    jug = Container(name="Jug", volume=1000, current_volume=1000)
    cup = Container(name="Cup", volume=200, current_volume=0, pour_out=50)
    i = 0
    while i < 15:
        jug.info()
        cup.info()
        cup.pour_liquid(jug.pour_out_liquid())
        i += 1

if __name__ == '__main__':
    main()