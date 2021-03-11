def freq_word():
    str=input("Enter the  sting : ")
    li=str.split() # to seprte the word
    print(li)
    d={} 
    
    #now count
    for i in li:
        if i not in d.keys(): #check whether the keys present in the dic or not 
            d[i]=0            #initialize key value=0
        d[i]=d[i]+1           #and here increment by 1
    print(d)
    
    
freq_word()
