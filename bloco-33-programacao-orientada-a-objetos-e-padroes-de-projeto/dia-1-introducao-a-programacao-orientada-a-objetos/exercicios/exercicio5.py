class TV:
    def __init__(self, brand, model, volume):
        self._brand = brand
        self._model = model
        self.volume = volume
        self.channel = 0
        self.up_volume = False
        self.down_volume = False

    def aumentar_volume(self):
        while(self.up_volume or self.volume < 100):
            self.volume += 1

    def diminuir_volume(self):
        while(self.down_volume or self.volume > 0):
            self.volume -= 0

    def next_channel(self):
        self.channel += 1

    def previous_channel(self):
        self.channel -= 1
