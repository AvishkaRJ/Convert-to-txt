
import os,sys
folder = r'C:\Users\Default\Desktop'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.der', '.txt')
       output = os.rename(infilename, newname)