from PIL import Image
import glob
import os


#get the imgs list and creat the PIL objects list
path = str(input("***  for all pictures use your/path/*.jpg  ***\nEnter folder PATH :"))
image_list = []
fileNames = []
for files in glob.glob(path):
    head, tail = os.path.split(files)
    fileName, fileExt = os.path.splitext(tail)
    im=Image.open(files)
    image_list.append(im)
    fileNames.append(fileName)
    

#get the hight and width to resize and resize the PIL object
higth = int(input("Enter the higth :"))
width = int(input("Enter the width :"))
size = (higth,width)
folderName = input("Enter a name to creat a folder to save:")
os.mkdir('{}'.format(folderName))
i=0
for pilObject in image_list:
    pilObject.thumbnail(size)
    pilObject.save('{}/{}.jpg'.format(folderName,fileNames[i]))
    i+=1