from PIL import Image

im = Image.open("Image.jpeg") 

# height & width of image
x_size = im.size[0]
y_size = im.size[1]

print("The size of the Image is:", im.size[0], " x ", im.size[1])

# # convert length integer into binary [8], 
# # create string with leading 24 zeros and then 8 binary values into binLength[]
# # loop into last 11 pixels to insert the 32 binary values
# # check each char, if char == '1' then insert 1, if char == '0' then insert 0

# # convert each char into binary, store into binMessage[]
# # store binMessage length and create a pointer starting at 0

# loop through image starting from bottom right corner pixel
#for row in xrange((x_size-1), 0, -1):
#    for col in xrange((y_size-1), 0, -1):      
#
#       # capture r,g,b values
#       red_value, green_value, blue_value = im.getpixel((row, col))
#
#       # note: remember to reserve last 11 pixels for text length (binary)
#       # loop only 8 times to record binary of text length
#
#       # check if at last 11 pixels
#       # if (row == x_size-1) && (col == (y_size-1..y_size-11))
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

import random

# note: figure out how to read from a text file instead of terminal
# message = open("text.txt")
message = input('what is the message? ')

# Output text/message information
# note: check for length of the message to the image height x image length
#       output error message if the length of the message is > image (length x height)

print("Text length = ", len(message), "* 8-bits = " , (len(message) * 8))
print("Binary: ", bin(len(message) * 8))
print("Pixels needed to encode (not including reserved last 11): ", ((len(message)*8)/3 + 1))

# hold array of binary, keep track with a pointer
# increment pointer every time binary is used

# === following code from guide: interactivepython.org ===

# ===================================================
# Function: bit_generator
# Input: string
# Output: 1 bit
# ===================================================
# Summary: 
# returns the bits needed for the message
# return 7 x 0's to indicate end of message
# returns random 0 & 1 to fill up remaining pixels
# ===================================================
def bit_generator(message):
    for ch in message:
        ascii = ord(ch)
        count = 0
        while count < 7:
            yield ascii & 1
            ascii = ascii >> 1
            count += 1
    for i in range(7):
        yield 0
    while True:
        yield random.randrange(1)

bitstream = bit_generator(message)

# ===================================================
# Function: setbit
# Input: oldbyte, newbit
# Output: updated bit value
# ===================================================
# Summary: 
# function replaces the lsb of the byte and returns 
# the new byte
# ===================================================

def setbit(oldbyte, newbit):
	if newbit:
		return oldbyte | newbit
	else:
		return oldbyte & 0b11111110

# ======== end code from guide: interactivepython.org ====

# Create copy of the original image
pix = im.load() 

# testing last 11 pixels
for row in range((x_size-1), 0, -1):
    for col in range((y_size-1), 0, -1):
	
	# reserve the last 11 pixels to store the text/message length in binary
	# convert length of text/message to integer -> binary 
	# append twenty-four 0s and then binary of the text/message length
	
	# check for the last 11 pixels
	
	# start on 12th pixel and insert the message using the pixel RGB lsb
	# loop length of text/message times

        red_value, green_value, blue_value = im.getpixel((row, col))

        redbit = next(bitstream)
        red_value = setbit(red_value, redbit)

        greenbit = next(bitstream)
        green_value = setbit(green_value, greenbit)

        bluebit = next(bitstream)
        blue_value = setbit(blue_value, bluebit)

	# save new lsb back into pixel
        pix[row, col] = red_value, green_value, blue_value

# it automatically saves?
im.save("modifiedImage.png")

