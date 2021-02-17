import random
import numpy as np
import csv
import math

#settings
dataLenght = 1000000000 # define your data lenght in batches 
# Your data lenght: ----------------------------------------------
# Your data in batches: --------   --------   --------   --------    --------  
array_raw = []

#for x in range(array_length):
#    random_decimal = round(random.uniform(1,10),2)
#    array_raw.append(random_decimal)
with open('G:\Projects\csgoroll\DATASET_ALL_17_2.csv', newline='') as myFile:
    reader = csv.reader(myFile, delimiter=',', quoting=csv.QUOTE_NONE)
    for lists in reader:
        for row in lists:
            array_raw.append(float(row))

myFile.close()
partToSplit = math.ceil(len(array_raw)/dataLenght)
print("Data length is: " + str(len(array_raw)))
print("Biggest crash value is: " + str(max(array_raw)))
batch = np.array_split(array_raw, partToSplit)
counts = np.bincount(array_raw)
print("Most common crash value is: " + str(np.argmax(counts)))


def filter_stats( batch_list, n, m ):
    count = 1
    for batch in batch_list:
        array_length = len(batch)
        if m==0:
            filter_arr = (batch>=n)
        else:
            filter_arr = (batch>=n) & (batch<=m)
        
        newarr = batch[filter_arr]
        
        print("************* BATCH ---" + str(count) + "--- STATISTIC RESULTS **************")
        if filter_arr.sum()==0:
            print ("No numbers in that area")
        elif m==0:
            print("Percentage of numbers bigger than " + str(n) + " is " + str(round(filter_arr.sum()*100/array_length,2)) + " %")
        else:
            print("Percentage of numbers bigger than " + str(n) + " and smaller than " + str(m) + " is " + str(round(filter_arr.sum()*100/array_length,2)) + " %")
        #print("************************ BATCH STATISTIC END ************************")
        count += 1
    return True

def simulator (data_list, a, b, c, d, e, startingBalance, underDoubleTimes): # put value a to e in order: from smallest to biggest
    balanceD = startingBalance
    balanceE = startingBalance
    balanceB = startingBalance
    balanceC = startingBalance
    balanceA = startingBalance
    allowToBet = 0
    for data in data_list:
        result = float(data)
        if underDoubleTimes == 0 or underDoubleTimes == allowToBet :
            print("Condition is met, " + str(underDoubleTimes) + " under 2. The crash result would be: " + str(result)) # print drawing number
            allowToBet = 0 #reseting
            if result >= a:
                balanceD += a - 1
                if result >= b:
                    balanceA += b - 1            
                    if result >= c:
                        balanceC += c - 1
                        if result >= d:
                            balanceB += d - 1
                            if result >= e:
                                balanceE += e - 1
                            else:
                                balanceE -= 1
                        else:
                            balanceB -= 1
                            balanceE -= 1
                    else:
                        balanceC -= 1
                        balanceB -= 1
                        balanceE -= 1
                else:
                    balanceA -= 1
                    balanceC -= 1
                    balanceB -= 1
                    balanceE -= 1
            else:
                balanceD -= 1
                balanceA -= 1
                balanceC -= 1
                balanceB -= 1
                balanceE -= 1
        else:
            pass
        if result < 2:
            allowToBet += 1
        else:
            allowToBet = 0

    print("******************** SIMULATOR RESULTS ************************")
    print("balance with multiplier set on " + str(a) + " is " + str(round(balanceD,2)) + ". TOTAL OUTCOME: " + str(round(balanceD - startingBalance,2)) + ' coins')
    print("balance with multiplier set on " + str(b) + " is " + str(round(balanceA,2)) + ". TOTAL OUTCOME: " + str(round(balanceA - startingBalance,2)) + ' coins')
    print("balance with multiplier set on " + str(c) + " is " + str(round(balanceC,2)) + ". TOTAL OUTCOME: " + str(round(balanceC - startingBalance,2)) + ' coins')
    print("balance with multiplier set on " + str(d) + " is " + str(round(balanceB,2)) + ". TOTAL OUTCOME: " + str(round(balanceB - startingBalance,2)) + ' coins')
    print("balance with multiplier set on " + str(e) + " is " + str(round(balanceE,2)) + ". TOTAL OUTCOME: " + str(round(balanceE - startingBalance,2)) + ' coins')
    print("**************************** END ******************************")
    return True  
    
filter_stats(batch, 1, 2)
#filter_stats(batch, 2, 3)
#filter_stats(batch, 3, 4)
#filter_stats(batch, 4, 5)
filter_stats(batch, 10, 1000)
filter_stats(batch, 1000, 100000)
#simulator (array_raw, 2, 3, 4, 5, 10, 100, 0)
simulator (array_raw, 2, 3, 4, 5, 10, 100, 19)
#simulator (array_raw, 1.17, 1.30, 1.70, 1.90, 500, 100)
#simulator (array_raw, 1.01, 1000, 10000, 100000, 1000000, 100)
