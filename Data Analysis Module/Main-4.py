import Data_Analysis_Module
import random
data=[random.randrange(10,100) for i in range(10)]
print(Data_Analysis_Module.mean(data))
print(Data_Analysis_Module.median(data))
print(Data_Analysis_Module.mode(data))