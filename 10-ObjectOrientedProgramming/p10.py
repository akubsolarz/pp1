class TV():
    def __init__(self,channels):
        self.channels = channels
        self.current_channel = 1
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f'TV is on {tel.current_channel}')
        else:
            print('TV is off')
    def change_channel(self,channel):
        self.current_channel=channel
tel=TV(
    23
)
tel.show_status()
tel.turn_on()
tel.show_status()
tel.change_channel(5)
tel.show_status()
tel.turn_off()
tel.show_status()

