from PIL import Image

im = Image.open("Lenna.jpeg") 

# Create copy of the original image
pix = im.load() 

# height & width of image
x_size = im.size[0]
y_size = im.size[1]


print "The size of the Image is:", (im.size[0]), " x ", (im.size[1])
print

# loop through image starting from bottom right corner pixel
#for row in xrange((x_size-1), 0, -1):
#    for col in xrange((y_size-1), 0, -1):      
#
#       # capture r,g,b values
#       red_template, green_template, blue_template = im.getpixel((row, col))
#
#       # note: remember to reserve last 11 pixels for text length (binary)
#       # loop only 8 times to record binary of text length
#
#       # check if at last 11 pixels
#       # if (row == x_size-1) && (col == (y_size-1..y_size-12))
#           # check text length (binary counter)
#           # if (text_length_counter > 0)
#           #   modify red value & decrease text_length_counter
#           # if (text_length_counter > 0)
#           #   modify green value & decrease text_length_counter
#           # if (text_length_counter > 0)
#           #   modify blue value & decrease text_length_counter
#           # note: nothing happens once counter == 0
#       # else
#           # start lsb modification starting on bottom right 12th pixel
#
#           # check text length (text_binary_counter)
#           # modify red value & decrease text_binary_counter
#
#           # check text length (text_binary_counter)
#           # modify green value & descrease text_binary_counter
#
#           # check text length (text_binary_counter)
#           # modify blue value & text_binary_counter
#
#           # note: nothing gets modified if binary counter == 0


# testing last 11 pixels
for row in xrange((x_size-1), (x_size-2), -1):
    for col in xrange((y_size-1), (y_size-12), -1):
        red_template, green_template, blue_template = im.getpixel((row,col))
    
        # test: output individual pixel r,g,b values
        print "Pixel locaiton:", (row), " x ", (col)
        print
        print "R value:", (red_template), "| R binary:", (bin(red_template))
        print "G value:" , (green_template), "| G binary:", (bin(green_template))
        print "B value:", (blue_template), "| B binary:", (bin(blue_template))
        print


# save encoded image
im.save("modifiedLenna.png")
