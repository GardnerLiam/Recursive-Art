from PIL import Image, ImageDraw
import numpy as np

WIDTH, HEIGHT = (3480,2160)

alpha = 10

WHITE = (255,255,255, alpha)

radiusLimit = 1

def recurse(x, y, r, col):
    if (x < 0 or x > WIDTH or y < 0 or y > HEIGHT or r < radiusLimit):
        return

    if (np.random.random() < 0.5):
        draw.ellipse([(x-r, y-r), (x+r, y+r)], outline=col)
    else:
        draw.rectangle([(x-r, y-r), (x+r, y+r)], outline=col)
    
    recurse(x-r, y, r/(2 if np.random.random() < 0.75 else 4), col)
    recurse(x+r, y, r/(2 if np.random.random() < 0.75 else 4), col)
    recurse(x, y-r, r/(2 if np.random.random() < 0.5 else 4), col)
    recurse(x, y+r, r/(2 if np.random.random() < 0.5 else 4), col)

    recurse(x+r, y+r, r/(2 if np.random.random() < 0.125 else 4), col)
    recurse(x-r, y-r, r/(2 if np.random.random() < 0.125 else 4), col)
    recurse(x+r, y-r, r/(2 if np.random.random() < 0.125 else 4), col)
    recurse(x-r, y+r, r/(2 if np.random.random() < 0.125 else 4), col)


im = Image.new("RGB", (WIDTH, HEIGHT), (0,0,0))

draw = ImageDraw.Draw(im, 'RGBA')


#multicolored image

recurse(WIDTH/2, HEIGHT/2, 600, (255,0,0,5))
recurse(WIDTH/2, HEIGHT/2, 600, (0,255,0,5))
recurse(WIDTH/2, HEIGHT/2, 600, (0,0,255,5))

#single-colored image
#recurse(WIDTH/2, HEIGHT/2, 600, WHITE)

im.save("out.png")
