from PIL import Image

im = Image.open("testImage.png") 

# height & width of image
x_size = im.size[0]
y_size = im.size[1]

print("The size of the Image is:", im.size[0], " x ", im.size[1])

#container for binary
binaryArray = []

# scan through image
for row in range((x_size-1), 0, -1):
    for col in range((y_size-1), 0, -1):
    
        red_value, green_value, blue_value = im.getpixel((row,col))
    
        # last 11 pixels reserved for message length
        if (row == (x_size-1)): 
		# try: if (y_size-11 <= col <= y_size-1):
            if ((col == (y_size-1)) | (col == (y_size-2)) | (col == (y_size-3))):
            
       
                print()
                print("Row:", row, "& Col:", col)
                print("red binary:", bin(red_value))
                print("green binary:", bin(green_value))
                print("blue binary:", bin(blue_value))
                print("lsb values:", red_value & 1, green_value & 1, blue_value & 1)
		
		# only grab the least significant bit
		binaryArray.append(str(red_value & 1))
		binaryArray.append(str(green_value & 1))
		binaryArray.append(str(blue_value & 1))
		
		
            
            
 #           if ((col == (y_size-4)) | (col == (y_size-5)) | (col == (y_size-6))):
 #            
 #               print("Row:", row, "& Col:", col)
 #               print(red_template & 1, green_template & 1, blue_template & 1)
 #           
 #           if ((col == (y_size-7)) | (col == (y_size-8)) | (col == (y_size-9))):
 #           
 #               print("Row:", row, "& Col:", col)
 #               print(red_template & 1, green_template & 1, blue_template & 1)
 #               
 #           if ((col == (y_size-10)) | (col == (y_size-11))):
 #           
 #               print("Row:", row, "& Col:", col)
 #               print(red_template & 1, green_template & 1, blue_template & 1)
 #	
 #           if (col == (y_size-12)):
 #               
 #               #save only the R and G value for the last 11th pixel
	
 #  # save all appended values to string using binString = ''.join(binaryArray)
 #  # convert the string to integer with base 2 using int(binString, 2)
 #  # use the integer value as a counter to decode the rest of the image
	                
                
          
