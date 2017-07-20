import os

os.system("wget https://ktu.edu.in/eu/core/announcements.htm")

f=open("announcements.htm")
os.remove("announcements.htm")

class announcements:
    def __init__(self):
        self.title=''
        

count=0
l=[]
while(True):
    line=f.readline()
    if '<!-- <a target="_blank">' in line:
        l.append(line)
        if count>=5:
            break
        count+=1


def stripper(a):
	return a[a.find('<b>')+3:a.find('</b>')]


list=[]
for i in range(len(l)):
	list.append(stripper(l[i]))


import pickle
f=open("ktudata.bin","wb")
pickle.dump(list,f)

