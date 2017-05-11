# ============================================================================
# Function: decode
# By: Dennis Wu
# Input: modifiedImage.png
# Output: [text on screen]
# ============================================================================
# Summary: reads the encoded image file and begins decoding the secret message
#          by reading the last 11 pixel's r,g,b values for the message length.
#          the remaining pixel's r,g,b least significant bit/btye gets combined
#          and is outputted to the screen to reveal the hidden message.
# 
# ============================================================================
from PIL import Image

import binascii, sys

im = Image.open("modifiedImage.png") 

# height & width of image
width = im.width
height = im.height

#container for binary
binaryArray = []

counter = 0
size_of_byte = 8

# scan through image to get message length
for row in range((height-1), -1, -1):

    for col in range((width-1), -1, -1):
    
        # get the r, g, b values from each pixel
        red_value, green_value, blue_value = im.getpixel((col,row))
        
        # grab the lsb of each color value
        binary_r = (red_value & 1)
        binary_g = (green_value & 1)
        binary_b = (blue_value & 1)       
        
        # last 0-10 pixels reserved for message length       
        if (counter < 10):

	       # only grab the least significant bit
           binaryArray.append(str(binary_r))
           binaryArray.append(str(binary_g))
           binaryArray.append(str(binary_b))

           binString = ''.join(binaryArray)

        # grabbing only RG values for pixel 10
        if (counter == 10):
                   		
	       # only grab the least significant bit
           binaryArray.append(str(binary_r))
           binaryArray.append(str(binary_g))

           binString = ''.join(binaryArray)

        # increment counter        
        counter = counter + 1
           
# combine all the values & convert to integer               
binString = ''.join(binaryArray)
binToint = int(binString, 2)
binCounter = binToint*size_of_byte

textArray = []
pixelCounter = 0
pointer = 0

# repeat process again to get secret message
for row in range((height-1), -1, -1):

    for col in range((width-1), -1, -1):
    
        # get the r, g, b values from each pixel
        red_value, green_value, blue_value = im.getpixel((col,row))
        
        # grab the lsb of each color value
        binary_r = (red_value & 1)
        binary_g = (green_value & 1)
        binary_b = (blue_value & 1)           
        
        # skip 0-10 pixels and decode        
        if ((pixelCounter > 10)): # and (pointer < binCounter)):    

            if (pointer < binToint):                  
               textArray.append(str(binary_r))
               pointer = pointer + 1
               
            if (pointer < binToint):                  
               textArray.append(str(binary_g))
               pointer = pointer + 1
               
            if (pointer < binToint):                  
               textArray.append(str(binary_b))
               pointer = pointer + 1

        # increment counter
        pixelCounter = pixelCounter + 1   

# combine all the values & convert to string               
binMessage = ''.join(textArray)
   
# convert binary to actual text
message = ''.join(chr(int(binMessage[i*size_of_byte: i*size_of_byte + size_of_byte], 2)) for i in range(len(binMessage) // size_of_byte))

print("")
print("Decoding Sucessful!")
print("Message:")
print(message)
