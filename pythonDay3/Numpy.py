import numpy as np

'''
x=np.array([[12,13,14],
           [13,14,55],
           [56,67,78],
           [33,44,55]])
print(x.shape)
#-------resizing the array-------
x.shape=(3,4)
print(x,)

x.shape=(2,6)
print(x)
'''

'''
x=np.arange(10)
print(x)

x=np.arange(3,30) #returns 3-29
print(x)

x=np.arange(3,30,3) #returns 3-29 in step 3
print(x)

x=np.arange(5,51,5)
x.shape=(5,2)
print(x)


x=np.ones((1,7)) #same as np.ones((7))
print(x)

x=np.ones((3,2))
print(x)

x=np.linspace(10,50,7) #10-50 evenly spaced 7 values
print(x)

x=np.array([1,35,45,65,75,85,95,55])
y=slice(1,6,2)
print(x[y])

y=x[1:6:2]
print(y)
'''

'''
x=np.array([[12,13,14],
           [13,14,55],
           [56,67,78],
           [33,44,55]])

print(x[...,1]) #all rows but only 1st column
print(x[1,...]) #frst row all columns
print(x[1:,...]) #all columns from 1st row

print(x[x>44])  #prints values which are greater than 44
'''
'''
x=np.array([[12,13,14],
           [13,14,55],
           [56,67,78],
           [33,44,55]])
y=np.array([[10,10,14],
           [13,14,50],
           [56,88,70],
           [330,400,50]])


print(x+y)
print(x-y)
print(x/y)

print(np.add(x,y))
print(np.subtract(x,y))
print(np.divide(x,y))


print(np.mod(x,y))

print(np.transpose(x))
print(x.T) # prints transpose, same as above one

print(x.flatten()) #converts to 1D array
print(x.flatten(order="F")) #converts to 1d arrar but columns wise


print(np.concatenate((x,y))) #concatenates.
print(np.concatenate((x,y),axis=1)) #concatenates row wise.

'''

'''
x=np.array([[12,13,14],
           [13,14,55],
           [56,67,78],
           [33,44,55],
           [99,00,88],
           [22,44,00]]) 
print(np.split(x,2))    #rows must be even to achieve this, else error

print(np.unique(x)) #uniques elements with ascending order.
'''

'''
x=np.array([[12,13,14],
           [13,14,55],
           [56,67,78],
           [33,44,55],
           [99,00,88],
           [22,44,1]])


print(np.amin(x))   #max overall
print(np.amin(x,0)) #min in each columns
print(np.amin(x,1)) #min in each rows

print(np.amax(x))   
print(np.amax(x,0)) #max in each columns
print(np.amax(x,1)) #max in each rows

print(np.median(x))
print(np.mean(x))
'''

'''
x=np.array([[12,13,14],
           [13,14,55],
           [56,67,78],
           [33,44,55],
           [99,00,88],
           [22,44,1]])

print(np.nonzero(x)) #returns two lists: one is of colums another row
                     #match two lists to obtain indices of nonzero ele 
'''

x="heLLo tHIs is PYTHON"
print(np.char.upper(x))
print(np.char.lower(x))
print(np.char.title(x))
print(np.char.capitalize(x))
print("---------------------------------")
print(np.char.replace(x,'tHIs',"that"))
print("---------------------------------")
print(np.char.multiply("Hiee",5))
print(np.char.add("joe","Biden"))










































