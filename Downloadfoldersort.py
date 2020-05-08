#sort download folder.

import os 

os.chdir('/Users/anvi/Downloads')

extmap={'doc':'Docs1','docx':'Docs2','pdf':'PDF','jpeg':'Images1','jpg':'Images2','mp4':'MP4','other':'Misc.','no':'Folders'}

for val in extmap.values():
 os.mkdir(val)

directorylist=os.listdir()
#print(directorylist)

for i in directorylist:
    if os.path.isfile(i):
        ext=i.split('.')[-1]
        directory = 'Misc.'
        if ext in extmap:
            directory = extmap[ext]
        with open(i,'rb') as copy, open(directory + '/' + i,'wb') as paste:
            filedata = copy.read()
            paste.write(filedata)
        os.remove(i)
        