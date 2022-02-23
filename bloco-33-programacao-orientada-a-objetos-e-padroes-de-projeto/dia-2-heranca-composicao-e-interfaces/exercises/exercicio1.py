class TV:
    def __init__(self, size):
        self.__volume = 50
        self.__channel = 1
        self.__size = size
        self.__isOn = False

    def increase_volume(self):
        if self.__volume <= 99:

            self.__volume += 1
            print(self.__volume)

    def decrease_volume(self):
        if self.__volume > 0:

            self.__volume -= 1
            print(self.__volume)

    def change_channel(self, channel):
        if channel > 99 or channel < 1:
            raise ValueError

        self.__channel = channel
        print(self.__channel)

    def onOff(self):
        self.__isOn = not self.__isOn
        print(self.__isOn)


instancia_tv = TV(size=25)
instancia_tv.onOff()
instancia_tv.increase_volume()
instancia_tv.decrease_volume()
instancia_tv.change_channel(5)
