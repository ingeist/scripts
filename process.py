from PIL import Image
img = Image.open("puzzle18.png")


width, height = img.size


for columns in range(0,width):
    white = 0
    black = 0
    for pixel in range(0,height):
        x = img.getpixel((columns,pixel))
        if (x==1):
            white += 1
        else:
            black += 1
    print(black-126)
