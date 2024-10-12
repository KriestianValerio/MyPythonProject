from cs1media import *

# This code converts an image into a black & white poster.

thresholddark = 85
thresholdlight = 170
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255,255,0)
blue = (0,0,255)
green = (0,128,0)

image = load_picture('./images/minion.jpg')
width, height = image.size()

for y in range(height):
    for x in range(width):
        r, g, b = image.get(x, y)
        average_brightness = (r + g + b) // 3
        if average_brightness > thresholdlight:
            image.set(x, y, yellow)
        elif average_brightness < thresholddark:
            image.set(x, y, blue)
        else:
            image.set(x,y,green)
            
image.show()