'''simple CLI to control the colors of the LED strip'''
import logging
import time

import rpi_ws281x as led

logging.basicConfig(level=logging.DEBUG)

LED_COUNT = 30
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)

strip = led.Adafruit_NeoPixel(num=LED_COUNT, pin=LED_PIN, freq_hz=LED_FREQ_HZ, dma=LED_DMA,
                              invvert=LED_INVERT, brightness=LED_BRIGHTNESS)
strip.begin()


def color(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


if __name__ == '__main__':
    try:
        while True:
            color(strip, led.Color(255, 0, 0))
            color(strip, led.Color(0, 255, 0))
            color(strip, led.Color(0, 0, 255))
    except KeyboardInterrupt:
        color(strip, led.Color(0, 0, 0), 10)
