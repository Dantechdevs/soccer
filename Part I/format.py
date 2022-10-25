from sys import intern


n=int(input()) #number of the country 
nt=list(map(str,input().split())) #name of the country
na=dict() 
for i in range(n):
    na[nt[i]]=i  #na[‘spain]=0 , na[‘England]=1
    
del nt    
m=int(input()) #number of matches 
ar=[[0 for i in range(5)] for j in range(n)] #array for storing the the no of match , GF , GA , GD POINTS 
po=dict() #DICTIONARY FOR POINTS
fla=1
mt=dict() #for keeping count that no two country play more than 2 match with each other
for i in range(m):
    t1,t2,g1,g2=input().split(” “)
    if(t1<t2):   
        z=t1+t2
        if(t1+t2 not in mt):
            mt[t1+t2]=1  # matches played  between two country arranger alphabetically like FranceSpain  not as SpainFrance
        else:
            mt[t1+t2]+=1 
    else:
        z=t2 + t1
        if(t2+t1 not in mt):
            mt[t2+t1]=1 
        else:
            mt[t2+t1]+=1
        
    if(t1==t2 or mt[z]>2): #if match between two team is greater than 2 or playing with themself break
        print(‘Invalid input’)
        fla=0
        break
    g1=int(g1)  
    g2=int(g2)
    x=na[t1] #ith row value to be used for maintaing the table
    y=na[t2]
    ar[x][0]+=1  #match played
    ar[y][0]+=1
    #Gf
    ar[x][1]+=g1
    ar[y][1]+=g2 
    #GA
    ar[x][2]+=g2 
    ar[y][2]+=g1 
    #GD
    ar[x][3]=ar[x][1]-ar[x][2]
    ar[y][3]=ar[y][1]-ar[y][2] 
    #points
    if(g1>g2):
        ar[x][4]+=2
        
    elif(g1==g2):
        ar[x][4]+=1 
        ar[y][4]+=1
        
    else:
        ar[y][4]+=2 
if(fla==1): #if valid input
    del mt
    for i in range(n):
        po[i]=ar[i][4] #point dictionary 
     #sort the dictionary a/c to their value    
    sorted_dict = {}
    sorted_keys = sorted(po, key=po.get)  # [1, 3, 2]
    
    for w in sorted_keys:
        sorted_dict[w] = po[w] #sorted dict
    #print(*ar,sep=’\n’) 
    #print(sorted_dict)
    del po
    ky=sorted_dict.keys()
    del sorted_keys
    li=[]  
    prev=-1
    prep=0
    val=list(na.values()) #list of value of dict(na)
    kyl=list(na.keys())   #list of key of dict(na)
    #storing the name of the country a/c to their point
    for j in (ky):
        x=val.index(j)
        li.append(kyl[x]) #appending their name
    #print(li) 
    #print(na) 
    #sorting the list with same point but diffrent GD or same point and same GD then alphabetically.
    for i in range(len(li)): 
        x=li[i]
        y=na[x]
        #print( x)
        for j in range(i+1,len(li)):
            a=li[j]
            b=na[a]
            #print( a)
            if(ar[y][4]==ar[b][4] and ar[y][3]>ar[b][3]): #if point is same bt GD is diffrent
                #print(‘h’)
                li[i],li[j]=li[j],li[i]
            elif(ar[y][4]==ar[b][4] and ar[y][3]==ar[b][3]): # point and GD both are same
                if(x<a): #then according to their name
                    #print(‘j’)
                    li[i],li[j]=li[j],li[i]
                    #print(li)
    li.reverse()
    print(*li,sep=‘\)
