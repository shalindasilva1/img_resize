from PIL import Image
import glob
import os


#get the imgs list and creat the PIL objects list
print(""" 
.S   .S_SsS_S.     sSSSSs         .S_sSSs      sSSs    sSSs   .S   sdSSSSSSSbs    sSSs  
.SS  .SS~S*S~SS.   d%%%%SP        .SS~YS%%b    d%%SP   d%%SP  .SS   YSSSSSSSS%S   d%%SP  
S%S  S%S `Y' S%S  d%S'            S%S   `S%b  d%S'    d%S'    S%S          S%S   d%S'    
S%S  S%S     S%S  S%S             S%S    S%S  S%S     S%|     S%S         S&S    S%S     
S&S  S%S     S%S  S&S             S%S    d*S  S&S     S&S     S&S        S&S     S&S     
S&S  S&S     S&S  S&S             S&S   .S*S  S&S_Ss  Y&Ss    S&S        S&S     S&S_Ss  
S&S  S&S     S&S  S&S             S&S_sdSSS   S&S~SP  `S&&S   S&S       S&S      S&S~SP  
S&S  S&S     S&S  S&S sSSs        S&S~YSY%b   S&S       `S*S  S&S      S*S       S&S     
S*S  S*S     S*S  S*b `S%%        S*S   `S%b  S*b        l*S  S*S     S*S        S*b     
S*S  S*S     S*S  S*S   S%        S*S    S%S  S*S.      .S*P  S*S   .s*S         S*S.    
S*S  S*S     S*S   SS_sSSS        S*S    S&S   SSSbs  sSS*S   S*S   sY*SSSSSSSP   SSSbs  
S*S  SSS     S*S    Y~YSSY        S*S    SSS    YSSP  YSS'    S*S  sY*SSSSSSSSP    YSSP  
SP           SP                   SP                          SP                         
Y            Y                    Y                           Y                          
                                                                                         """)
print("\n\n\n")
path = str(input("***  for all pictures use * eg:>> your/path/*.jpg  ***\nEnter folder PATH :"))
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