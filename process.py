from PIL import Image
import wavio
import numpy as np
img = Image.open("puzzle18.png")


width, height = img.size
stream=np.array([])

for columns in range(0,width):
    white = 0
    black = 0
    for pixel in range(0,height):
        x = img.getpixel((columns,pixel))
        if (x==1):
            white += 1
        else:
            black += 1
    #print(black-126)
    stream = np.append(stream,black-126)
#print(stream)
## create wav file

rate = 10000
wavio.write("18.wav", stream,rate, sampwidth =3)
