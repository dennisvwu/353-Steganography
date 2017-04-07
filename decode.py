from PIL import Image
import binascii, sys

im = Image.open("testImage.png") 

# height & width of image
width = im.width
height = im.height

print("The size of the Image is:", width, " x ", height)

#container for binary
binaryArray = []

# scan through image to get message length
for row in range((height-1), -1, -1):
    for col in range((width-1), -1, -1):
    
        # get the r, g, b values from each pixel
        red_value, green_value, blue_value = im.getpixel((col,row))
        
        # grab the lsb of each color value
        binary_r = (red_value & 1)
        binary_g = (green_value & 1)
        binary_b = (blue_value & 1)       
        
        # last 11 pixels reserved for message length       
        if (row == (height-1)):
               
            if col in range(width-10, width-1):
        		
	            # only grab the least significant bit
                binaryArray.append(str(binary_r))
                binaryArray.append(str(binary_g))
                binaryArray.append(str(binary_b))
            
            # only need r & g value on 11th pixel
            if (col == width-11):
      
	           # only grab the least significant bit
               binaryArray.append(str(binary_r))
               binaryArray.append(str(binary_g)) 
           
# combine all the values & convert to integer               
binString = ''.join(binaryArray)
binToint = int(binString, 2)

print("Integer value = ", binToint)

textArray = []
counter = binToint

# repeat process again to get secret message
for row in range((height-1), -1, -1):
    for col in range((width-1), -1, -1):
    
        # get the r, g, b values from each pixel
        red_value, green_value, blue_value = im.getpixel((col,row))
        
        # grab the lsb of each color value
        binary_r = (red_value & 1)
        binary_g = (green_value & 1)
        binary_b = (blue_value & 1)       
        
        # skip 11 pixels reserved for message length       
        if (row == (height-1)):  
                
            if col in range(width-11, width-1):
                # do nothing
                ...
                
            # start from 12th pixel
            if (counter > 0):                  
               textArray.append(str(binary_r))
               counter = counter - 1
            if (counter > 0):
               textArray.append(str(binary_g))
               counter = counter - 1
            if (counter > 0):
               textArray.append(str(binary_b))
               counter = counter - 1
                                      
        else:
        
            # continue to other pixels
            if (counter > 0):                  
               textArray.append(str(binary_r))
               counter = counter - 1
            if (counter > 0):
               textArray.append(str(binary_g))
               counter = counter - 1
            if (counter > 0):
               textArray.append(str(binary_b))
               counter = counter - 1
               
            #print("Counter = ", counter)   

           
# combine all the values & convert to string               
binMessage = ''.join(textArray)

# convert binary to actual text
message = ''.join(chr(int(binMessage[i*8: i*8 + 8], 2)) for i in range(len(binMessage) // 8))
print ("Message = ", message)
print (binMessage)

      

 

	                
                
          
