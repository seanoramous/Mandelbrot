# Mandelbrot fractal 
# FB - 201003254 
from PIL import Image 

# drawing area 
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5

# max iterations allowed 
maxIt = 255

# image size
multiple = 10
imgx = 512 * multiple
imgy = 512 * multiple
image = Image.new("RGB", (imgx, imgy)) 

for y in range(imgy):
    print("%.2f %%" % (y / imgy * 100.0)) 
    zy = y * (yb - ya) / (imgy - 1) + ya 
    for x in range(imgx):
        #print("%.2f %%" % (x / imgx * 100.0)) 
        zx = x * (xb - xa) / (imgx - 1) + xa 
        z = zx + zy * 1j
        c = z 
        for i in range(maxIt): 
            if abs(z) > 2.0: break
            z = z * z + c 
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16)) 

image.save("test.jpg")
image.show() 
