from PIL import Image

import string
import random

# ===================================================
# Function: setbit
# Input: oldbyte, newbit
# Output: updated bit value
# ===================================================
# Summary: 
# function replaces the lsb of the byte and returns 
# the new byte
# ===================================================

# === following code from guide: interactivepython.org ===

def setbit(oldbyte, newbit):
	if newbit:
		return oldbyte | newbit
	else:
		return oldbyte & 0b11111110

# ======== end code from guide: interactivepython.org ====



im = Image.open("Image.jpeg") 

# height & width of image
width = im.width
height = im.height

# grab secret message to encode
message = open('secret.txt', 'r').read()

# Output text/message information
print("The size of the Image is:", width, " x ", height, " = ", (width*height), "pixels")
print("Secret text length:", len(message))
print("Pixels needed to encode (including reserved last 11):", ((len(message)*8)//3 + 12), "pixels")

# note: check for length of the message to the image height x image length
#       output error message if the length of the message is > image (length x height)
if (width*height < (len(message)*8)):
    print("Sorry, image size is too small to fit all the secret message")
    # need to figure out how to exit program

binArray = []

# format the binary
binLength = '{:08b}'.format(len(message)*8)

# fill in extra 0s
extraZeros = '000000000000000000000000'

# combine everything
binArray.append(extraZeros)
binArray.append(str(binLength))
binStringLength = ''.join(binArray)

print("Binary of ", len(message)*8, "=", binStringLength)


# convert each char into binary, store into binMessage
binMessageLength = []

for ch in message:
    ascii = ord(ch)
    binary = '{:08b}'.format(ascii)
    binMessageLength.append(str(binary))   
    
binMessage = ''.join(binMessageLength)

print("Length of Binary Message:", len(binMessage))
print("Binary of Secret Message:", binMessage)

# counters
binaryCounter = len(binMessage)
pixeCounter = 0
pointer = 0

# Create copy of the original image
pix = im.load() 

# loop through image pixels
for row in range((height-1), -1, -1):

    for col in range((width-1), -1, -1):
    
        red_value, green_value, blue_value = im.getpixel((col, row))
        
        # grab the lsb of each color value
        binary_r = (red_value & 1)
        binary_g = (green_value & 1)
        binary_b = (blue_value & 1) 
	
        pixeCounter = pixeCounter + 1
	    
	    # reserve the last 11 pixels to store the text/message length in binary
        if (pixeCounter <= 10):
           
           binary_r = int(binMessage[pointer])
           red_value = setbit(red_value, binary_r)
           pointer = pointer + 1
           
           print("Binary R value:", binary_r)

           binary_g = int(binMessage[pointer])
           green_value = setbit(green_value, binary_g)
           pointer = pointer + 1
           
           print("Binary G value:", binary_g)

           binary_b = int(binMessage[pointer])
           blue_value = setbit(blue_value, binary_b)
           pointer = pointer + 1
           
           print("Binary B value:", binary_b)

	       # save new lsb back into pixel
           pix[col, row] = red_value, green_value, blue_value
        
        # 11th pixel only stores the Red and Green value
        if (pixeCounter == 11):
           
           binary_r = int(binMessage[pointer])
           red_value = setbit(red_value, binary_r)
           pointer = pointer + 1
           
           print("Binary R value:", binary_r)

           binary_g = int(binMessage[pointer])
           green_value = setbit(green_value, binary_g)
           pointer = pointer + 1
           
           print("Binary G value:", binary_g)

	       # save new lsb back into pixel
           pix[col, row] = red_value, green_value, binary_b
              
        # start on 12th pixel to encode secret text      
        else:
        
           if (pointer < binaryCounter):
           
               binary_r = int(binMessage[pointer])
               red_value = setbit(red_value, binary_r)
               pointer = pointer + 1
           
               print("Binary R value:", binary_r)


               if (pointer < binaryCounter):
                           
                   binary_g = int(binMessage[pointer])
                   green_value = setbit(green_value, binary_g)
                   pointer = pointer + 1
           
                   print("Binary G value:", binary_g)
                   
               else:
               	   
               	   # save new lsb back into pixel
                   pix[col, row] = red_value, binary_g, binary_b
                   
                   print("No more, saving from Green")
                   
               if (pointer < binaryCounter):

                   binary_b = int(binMessage[pointer])
                   blue_value = setbit(blue_value, binary_b)
                   pointer = pointer + 1
                   
                   print("Binary B value:", binary_b)
                   
               else:

               	   # save new lsb back into pixel
                   pix[col, row] = red_value, green_value, binary_b
                   
                   print("No more, saving from BLUE")
                

            
# it automatically saves?
im.save("modifiedImage.png")


