from cs1media import *

# The code below get a reversed color from "original_image" and modify "image"

threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)

original_image = load_picture('./images/minion.jpg')
image = load_picture('./images/minion.jpg')
width, height = image.size()

for y in range(height):
    for x in range(width):
        rnew , gnew, bnew = original_image.get((x+width/2)%width, y)
        new_color = (rnew,gnew,bnew)
        image.set(x, y, new_color)

            
image.show()