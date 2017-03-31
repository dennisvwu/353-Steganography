from PIL import Image

im = Image.open("Lenna.png") 

# Create copy of the original image
pix = im.load() 

# Split the bands R,G,B values
red_template = im.split()[0]
green_template = im.split()[1]
blue_template = im.split()[2]

# height & width of image
x_size = im.size[0]
y_size = im.size[1]


print "The size of the Image is:", (im.size[0]), " x ", (im.size[1])

# loop through image
for i in range(5):
    for j in range(1):
    
        # capture r,g,b values
        r, g, b = im.getpixel((i, j))
        
        # output to screen binary value
        print "Red:", bin(r), " Green:", bin(g), "Blue: ", bin(b)
    



# pix[x,y] = value # Set the RGBA Value of the image (tuple)
# im.save("modifiedLenna.jpeg") # Save the modified pixels as png
