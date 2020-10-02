import pandas as pd
import numpy as np
import os

os.chdir("C:\\Users\\user\\Desktop\\kalder")
dataset=pd.read_csv(r'netflix_titles.csv')


####################################column 0
#SHOW_ID, useless

###column 1, MOVIE OR SERIES
a=dataset.iloc[:,1]
temp=[]

for i in range(0,len(a)-1):
    if (a.iloc[i]=='Movie'): 
        temp.append(0)
    else:
        temp.append(1)
        
temp=list(map(int, temp))        
final=pd.DataFrame(temp,columns=['showseries'])

################################################column 2, TITLE
a=dataset.iloc[:,2]
temp=[]

for i in range(0,len(a)-1):
    b = sum([ord(c) for c in a.iloc[i]])
    temp.append(b)

#turn arithmetic to sorted 0,1,2...
templist=[]
sortedlist=np.sort(temp)
counter=0
elementlist=[]
temp2=[]

i=0
elementlist.append(0)
templist.append(sortedlist[0])

for i in range(1,len(a)-1):
    if (sortedlist[i]>sortedlist[i-1]):
        counter+=1
        elementlist.append(counter)
        templist.append(sortedlist[i])
        
for i in range(0,len(a)-1):
    a=temp[i]
    for i in range(0,len(templist)):
        if (a==templist[i]):
            temp2.append(elementlist[i])

temp=list(map(int, temp2))

final['title']=temp


################################################column 3, DIRECTOR
a=dataset.iloc[:,3]
temp=[]

for i in range(0,len(a)-1):
    b=np.nan_to_num(a[i])
    if (b==0):
        temp.append(1)
    else:
        b = sum([ord(c) for c in a.iloc[i]])
        temp.append(b)

#turn arithmetic to sorted 0,1,2...
templist=[]
sortedlist=np.sort(temp)
counter=0
elementlist=[]
temp2=[]

i=0
elementlist.append(0)
templist.append(sortedlist[0])

for i in range(1,len(a)-1):
    if (sortedlist[i]>sortedlist[i-1]):
        counter+=1
        elementlist.append(counter)
        templist.append(sortedlist[i])
        
for i in range(0,len(a)-1):
    a=temp[i]
    for i in range(0,len(templist)):
        if (a==templist[i]):
            temp2.append(elementlist[i])

temp=list(map(int, temp2))

final['director']=temp


############################################column 4, ACTORS, can't use it, weird structure


##############################################column 5, COUNTRY
a=dataset.iloc[:,5]
temp=[]

for i in range(0,len(a)-1):
    b=np.nan_to_num(a[i])
    if (b==0):
        temp.append(1)
    else:
        b = sum([ord(c) for c in a.iloc[i]])
        temp.append(b)

#turn arithmetic to sorted 0,1,2...
templist=[]
sortedlist=np.sort(temp)
counter=0
elementlist=[]
temp2=[]

i=0
elementlist.append(0)
templist.append(sortedlist[0])

for i in range(1,len(a)-1):
    if (sortedlist[i]>sortedlist[i-1]):
        counter+=1
        elementlist.append(counter)
        templist.append(sortedlist[i])
        
for i in range(0,len(a)-1):
    a=temp[i]
    for i in range(0,len(templist)):
        if (a==templist[i]):
            temp2.append(elementlist[i])

temp=list(map(int, temp2)) 

final['country']=temp

##################################################column 6, DATE ADDED
a=dataset.iloc[:,6]
temp=[]

for i in range(0,len(a)-1):
    b=np.nan_to_num(a[i])
    if (b==0):
        temp.append(1)
    else:
        temp.append(a[i])

temp=[]

for i in range(0,len(a)-1):
    b=np.nan_to_num(a[i])
    if (b==0):
        temp.append(1)
    else:
        b = sum([ord(c) for c in a.iloc[i]])
        temp.append(b)

#turn arithmetic to sorted 0,1,2...
templist=[]
sortedlist=np.sort(temp)
counter=0
elementlist=[]
temp2=[]

i=0
elementlist.append(0)
templist.append(sortedlist[0])

for i in range(1,len(a)-1):
    if (sortedlist[i]>sortedlist[i-1]):
        counter+=1
        elementlist.append(counter)
        templist.append(sortedlist[i])
        
for i in range(0,len(a)-1):
    a=temp[i]
    for i in range(0,len(templist)):
        if (a==templist[i]):
            temp2.append(elementlist[i])

temp=temp2  

final['dateadded']=list(map(int, temp))

##############################################column 7, RELEASE YEAR
a=dataset.iloc[:,7]
temp=[]

for i in range(0,len(a)-1):
    b=np.nan_to_num(a[i])
    if (b==0):
        temp.append(1)
    else:
        temp.append(a[i])

final['releaseyear']=list(map(int, temp))

##############################################column 9, DURATION
a=dataset.iloc[:,9]
temp1=[]
temp2=[]

for i in range(0,len(a)-1):
    str=a[i]
    check=[int(s) for s in str.split() if s.isdigit()] #extract numbers from string
    if (check[0]>30):
        temp1.append(0)
        temp2.append(check[0])
    else:
        temp1.append(check[0])
        temp2.append(0)

final['movieduration']=list(map(int, temp2))
final['seriesduration']=list(map(int, temp1))

############################################column 10, TYPE OF MOVIE/SHOW
a=dataset.iloc[:,10]
temp=[]

for i in range(0,len(a)-1):
    b=np.nan_to_num(a[i])
    if (b==0):
        temp.append(1)
    else:
        b = sum([ord(c) for c in a.iloc[i]])
        temp.append(b)

#turn arithmetic to sorted 0,1,2...
templist=[]
sortedlist=np.sort(temp)
counter=0
elementlist=[]
temp2=[]

i=0
elementlist.append(0)
templist.append(sortedlist[0])

for i in range(1,len(a)-1):
    if (sortedlist[i]>sortedlist[i-1]):
        counter+=1
        elementlist.append(counter)
        templist.append(sortedlist[i])
        
for i in range(0,len(a)-1):
    a=temp[i]
    for i in range(0,len(templist)):
        if (a==templist[i]):
            temp2.append(elementlist[i])

temp=list(map(int, temp2))            

final['type']=temp


##############################################column 8, RATED-TARGET
a=dataset.iloc[:,8]
temp=[]

for i in range(0,len(a)-1):
    b=np.nan_to_num(a[i])
    if (b==0):
        temp.append(1)
    else:
        b = sum([ord(c) for c in a.iloc[i]])
        temp.append(b)

#turn arithmetic to sorted 0,1,2...
templist=[]
sortedlist=np.sort(temp)
counter=0
elementlist=[]
temp2=[]

i=0
elementlist.append(0)
templist.append(sortedlist[0])

for i in range(1,len(a)-1):
    if (sortedlist[i]>sortedlist[i-1]):
        counter+=1
        elementlist.append(counter)
        templist.append(sortedlist[i])
        
for i in range(0,len(a)-1):
    a=temp[i]
    for i in range(0,len(templist)):
        if (a==templist[i]):
            temp2.append(elementlist[i])

temp=list(map(int, temp2))     

final['rated']=temp

#np.savetxt("rated.csv", final, fmt="%d")




