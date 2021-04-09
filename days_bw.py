

def isleap(yr):      # leap year checker functuion type:bool
    year=int(yr)
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

#---------------#---------------#---------------#---------------#---------------    

mondic={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
lmond= {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
nlmond={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

#---------------#---------------#---------------#---------------#---------------
    
def validator(datex):     #function to check that wether both dates are valid or not type:bool
    if int(datex.split("-")[1])==2:
        if (int(datex.split("-")[2])<= 28) or (int(datex.split("-")[2])<30 and isleap(datex.split('-')[0])) :
            return True
    if int(datex.split("-")[1]) in (1,3,5,7,8,10,12) and int(datex.split("-")[2])<32 :
        return True
    elif int(datex.split("-")[1]) in (4,6,9,11) and int(datex.split("-")[2])<31 :
        return True

#---------------#---------------#---------------#---------------#---------------#---------------

def sameyr(dt1,dt2):
    
    if int(dt1.split('-')[1]) < int(dt2.split('-')[1]):   # for month
        xx=dt1.split('-')
        yy=dt2.split('-')
    else:
        yy=dt1.split('-')
        xx=dt2.split('-')
                  
    if int(xx[1]) == int(yy[1]):
            return abs(int(xx[2]) - int(yy[2]))
    else:
            LL=list([int(xx[1]),int(yy[1])])
            LL.sort()
            Lrange=tuple(range(LL[0],LL[1]+1))

            if Lrange[0]==2 :
                if (isleap(xx[0])):
                    small = abs(29-int(xx[2])) 
                else:
                    small=abs(28-int(xx[2])) 
                
                big = abs(int(yy[2]))
                midT=Lrange[1:-1]
                midL= sum([mondic[i] for i in midT])
                return(big+small+midL)
            
            elif (2 in Lrange[1:-1]) :
                small=abs(mondic[int(xx[1])] - int(xx[2]) )
                big= int(yy[2])
                if isleap(xx[0]):
                    midL= sum([lmond[i] for i in Lrange[1:-1]])
                else:
                    midL= sum([lmond[i] for i in Lrange[1:-1]])-1
                return (big+small+midL)

            else:
                small=abs(mondic[int(xx[1])] - int(xx[2]) )
                big=int(yy[2])
                midL = sum([mondic[i] for i in Lrange[1:-1]])
                return (big+small+midL)

#---------------#---------------#---------------#---------------#---------------#---------------

def nsameyr(dt1,dt2):
    if int(dt1.split('-')[1]) < int(dt2.split('-')[1]):   # for month
        xx=dt1.split('-')
        yy=dt2.split('-')
    else:
        yy=dt1.split('-')
        xx=dt2.split('-')
        
    if int(dt1.split('-')[0]) < int(dt2.split('-')[0]):    # for years
        ys=dt1.split('-')
        yb=dt2.split('-')
    else:
        yb=dt1.split('-')
        ys=dt2.split('-')
        
    if xx[0] != yy [0]:
        smR=tuple(range(int(ys[1]),13))
        bmR=tuple(range(1,int(yb[1])))
        smal=sum([nlmond[i] for i in smR])-int(ys[2])
        big=sum([nlmond[i] for i in bmR])+int(yb[2])
        
        if isleap(ys[0]) :
                  smal=sum([lmond[i] for i in smR])-int(ys[2])
        if isleap(yb[0]) :
                  big=sum([lmond[i] for i in bmR])+int(yb[2])
        
        return (smal+big)

#---------------#---------------#---------------#---------------#---------------#---------------

def submain(dt1,dt2):
    if int(dt1.split('-')[1]) < int(dt2.split('-')[1]):   # for month
        xx=dt1.split('-')
        yy=dt2.split('-')
    else:
        yy=dt1.split('-')
        xx=dt2.split('-')
        
    if int(dt1.split('-')[0]) < int(dt2.split('-')[0]):    # for years
        ys=dt1.split('-')
        yb=dt2.split('-')
    else:
        yb=dt1.split('-')
        ys=dt2.split('-')
        
    # main logic and execution
    
    if int(xx[0]) == int(yy[0]):
        return sameyr(dt1,dt2)
        
    else:
        return nsameyr(dt1,dt2)


#---------------#---------------#---------------#---------------#---------------#---------------

def main(d1,d2):
    if type(d1)==str and type(d2)== str:
        if validator(d1) and validator(d2):
            return submain(d1,d2)
            
        else:
            print("enter valid date in YYYY-MM-DD format \nseparated by '-'\nfor example,\t2021-04-05")
    else: 
        print("enter date in string format in YYYY-MM-DD\nseparated by '-'\nfor example,\t2021-04-05 ")

#---------------#---------------#---------------#---------------#---------------#---------------        
