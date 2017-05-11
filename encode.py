# ============================================================================
# Function: encode
# By: Dennis Wu
# Input: Image.jpeg & secret.txt
# Output: modifiedImage.png
# ============================================================================
# Summary: reads text file and replaces the last 11 pixels with the length
#          of the text file. the remaining pixels's r,g,b least significant
#          bit/byte gets replaced with the binary of the actual message from
#          the secret.txt file.
# 
# ============================================================================
from PIL import Image

import string

size_of_byte = 8

# === following code from guide: interactivepython.org ===
def setbit(oldbyte, newbit):
   if newbit:
      return oldbyte | newbit
   else:
      return oldbyte & 0b11111110
# ======== end code from guide: interactivepython.org ====

im = Image.open("Image.jpeg") 

# Create copy of the original image
pix = im.load() 

# height & width of image
width = im.width
height = im.height

# grab secret message to encode
message = open('secret.txt', 'r').read()

# Output text/message information
print("")
print("The size of the Image is:", width, "x", height)
print("length of secret.txt :", len(message))

# note: check for length of the message to the image height x image length
#       output error message if the length of the message is > image (length x height)
if (width*height < (len(message)*size_of_byte)):
    print("")
    print("FAILED")
    print("Sorry, image size is too small to fit all the secret message")
    print("FAILED")
    print("")
    exit()

# format the binary: length * size of byte
binLength = '{:08b}'.format(len(message)*size_of_byte)

# fill in extra 0s
paddedLength = binLength.zfill(32)

# combine everything
binArray = []

binArray.append(str(paddedLength))
binStringLength = ''.join(binArray)

# convert each char into binary, store into binMessage
binMessageLength = []

for ch in message:
    ascii = ord(ch)
    binary = '{:08b}'.format(ascii)
    binMessageLength.append(str(binary))   
    
binMessage = ''.join(binMessageLength)

# counters
binaryCounter = len(binMessage)
pixeCounter = 0
pointer = 0

# loop through image pixels
for row in range((height-1), -1, -1):

    for col in range((width-1), -1, -1):
    
        red_value, green_value, blue_value = im.getpixel((col, row))
        
        # grab the lsb of each color value
        binary_r = (red_value & 1)
        binary_g = (green_value & 1)
        binary_b = (blue_value & 1) 
		    
	    # reserve the last 0-10 pixels to store the text/message length in binary
        if (pixeCounter < 10):

           binary_r = int(binStringLength[pointer])
           red_value = setbit(red_value, binary_r)
           pointer = pointer + 1         

           binary_g = int(binStringLength[pointer])
           green_value = setbit(green_value, binary_g)
           pointer = pointer + 1
           
           binary_b = int(binStringLength[pointer])
           blue_value = setbit(blue_value, binary_b)
           pointer = pointer + 1

	       # save new lsb back into pixel
           pix[col, row] = red_value, green_value, blue_value

        if (pixeCounter == 10):

           binary_r = int(binStringLength[pointer])
           red_value = setbit(red_value, binary_r)
           pointer = pointer + 1         

           binary_g = int(binStringLength[pointer])
           green_value = setbit(green_value, binary_g)
           pointer = pointer + 1

	       # save new lsb back into pixel
           pix[col, row] = red_value, green_value, blue_value
           
           # reset pointer
           pointer = 0
              
        # start to encode secret.txt content into image    
        if (pixeCounter > 10):
        
           if (pointer < binaryCounter):

               binary_r = int(binMessage[pointer])
               red_value = setbit(red_value, binary_r)
               pointer = pointer + 1      

           if (pointer < binaryCounter):

               binary_g = int(binMessage[pointer])
               green_value = setbit(green_value, binary_g)
               pointer = pointer + 1     

           if (pointer < binaryCounter):

              binary_b = int(binMessage[pointer])
              blue_value = setbit(blue_value, binary_b)
              pointer = pointer + 1  
    
           # save values into pixel
           pix[col, row] = red_value, green_value, blue_value
                       
        # increment counter
        pixeCounter = pixeCounter + 1              
                          
# it automatically saves?
im.save("modifiedImage.png")

print("")
print("Encoding Sucessful!")
print("Contents of secret.txt encoded into 'modifiedImage.png'")
print("")
