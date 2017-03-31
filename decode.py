from PIL import Image

im = Image.open("testImage.png") 

# height & width of image
x_size = im.size[0]
y_size = im.size[1]

print("The size of the Image is:", im.size[0], " x ", im.size[1])

# scan through image
for row in range((x_size-1), 0, -1):
    for col in range((y_size-1), 0, -1):
    
        red_template, green_template, blue_template = im.getpixel((row,col))
    
        # last 11 pixels reserved for message length
        if (row == (x_size-1)): 
            if ((col == (y_size-1)) | (col == (y_size-2)) | (col == (y_size-3))):
            
       
                print()
                print("Row:", row, "& Col:", col)
                print("red binary:", bin(red_template))
                print("green binary:", bin(green_template))
                print("blue binary:", bin(blue_template))
                print("lsb values:", red_template & 1, green_template & 1, blue_template & 1)
            
            
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
 #           if ((col == (y_size-10)) | (col == (y_size-11)) | (col == (y_size-12))):
 #           
 #               print("Row:", row, "& Col:", col)
 #               print(red_template & 1, green_template & 1, blue_template & 1)
            
	                
                
          
