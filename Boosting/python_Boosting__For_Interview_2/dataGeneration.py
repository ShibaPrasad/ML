from numpy import *
import data
import adaboost

print ('1 = Training\n2 = Testing')
var = input("Please enter something: ")
print ("you entered", var)

if (int(var) == 1):
    # data Generation for Training
    data.randomData('train',150,'train')
else:
    # data Generation for Testing
    data.randomData('test',15,'test')