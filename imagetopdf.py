# importing required files
from PIL import Image, ImageEnhance
import shutil
import os
import img2pdf
# put all the images in the the images directory
img_list = [x for x in os.listdir('images')] 
 
# Add some post-processing to the image before conversions
i=10000
for img in img_list:
    imgg= Image.open("images/"+img).convert('RGB') 
    # adding sharpness
    enhancer= ImageEnhance.Sharpness(imgg)
    image = enhancer.enhance(2)
    # changing the resolution of the image
    resized_img = image.resize((4098, 2304),Image.BICUBIC)
    # adding contrast    
    enhancer = ImageEnhance.Contrast(resized_img)
    factor = 1.4
    im_output = enhancer.enhance(factor)
    #adding sharpness
    enhancer= ImageEnhance.Sharpness(im_output)
    image = enhancer.enhance(3)  
    #saving the image     
    image.save("temp/"+"image ("+str(i)+").jpg",'JPEG',quality=100)
    i=i+1

# Pdf will be save by the below code.
with open("output.pdf", "wb") as f:
    
    f.write(img2pdf.convert(["temp/"+i for i in os.listdir('temp')]))

# delete the images from the temp directory
mylist = ["temp"]
for dir in mylist:
 for files in os.listdir(dir):
    path = os.path.join(dir, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
        