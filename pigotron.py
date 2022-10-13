"""
This code to animate a neopixel ring with a poor Raspberry Pi Zero W

Install the following libraries:
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka

If you see the following message:
RuntimeError: ws2811_init failed with code -13 (Unable to initialize SPI)

Please run raspi-config and enable SPI : Interfacing Options -> SPI -> Yes
sudo raspi-config

"""
import board
import neopixel
import time

# Define the Digital pin connected to the NeoPixels
# Number of NeoPixels
# Starts with a little brightness to avoid burning the Raspberry Pi Zero W
pixels = neopixel.NeoPixel(board.D18, 16, brightness=0.1, auto_write=True)

print("hello neopixelring!")

pixels[0] = (0, 0, 100)
pixels.show()
time.sleep(2)


# GPIO  
pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 16


class PIGOTRON:
    """
    This class to Manage neopixel ring
    
    """
    def __init__(self, pixelPin, pixelNum: int):
        self.__version__ = "v0.0.1"
        self.pixelNum = pixelNum
        self.pixels = neopixel.NeoPixel(pixelPin, pixelNum, brightness=0.2, auto_write=True)
        print("initialized")
        self.white()
        time.sleep(3)

    def white(self):
        """
        All LCDs White
        """
        self.pixels.fill((125, 125, 125)) # BRIGHT WHITE    
        print("white")
    
    def flashColor(self, color: str):
        """
        All LCDs Flashing the same color.
        color: str in "red" or "blue" or "green"
        
        """
        for i in range(125): 
            if color == "red":
                self.pixels.fill((i, 0, 0))
            elif color == "green":
                self.pixels.fill((0, i, 0))
            elif color == "blue":
                self.pixels.fill((0, 0, i))
            
            time.sleep(0.02)

        for i in range(125): 
            if color == "red":
                self.pixels.fill((125-i, 0, 0))
            elif color == "green":
                self.pixels.fill((0, 125-i, 0))
            elif color == "blue":
                self.pixels.fill((0, 0, 125-i))
            
            time.sleep(0.02)

    def turningOneColor(self, colorMix: list): 
        """
        colorMix: list of int R V B values between 0-255, ie [20,40,60] or [60,40,20]
        """
        for i in range(self.pixelNum):
            pixels[i] = (colorMix[0], colorMix[1], colorMix[1])
            time.sleep(0.1)

    def showMeTheLight(self):
        print("Showing the light")
        self.white()
        time.sleep(5)
        while True:
            
            self.turningOneColor([20,40,60])
            self.turningOneColor([60,40,20])
            self.turningOneColor([20,40,60])
            print("Flashing some color")
            self.flashColor("red")
            self.flashColor("green")
            self.flashColor("blue")
            time.sleep(0.02)

if __name__ == "__main__":
    print("Pigotron!")
    myPig = PIGOTRON(pixel_pin, num_pixels)
    print("and now, show me the light!")
    myPig.showMeTheLight()
