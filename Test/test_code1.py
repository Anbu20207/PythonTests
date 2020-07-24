#print("sjkdf")
values = [3,2, 5,4]
length = len(values)
#print("{}{}".format("THe length is:",length))
len1=0
for i in range(0,values[length-1]):
    chknum = values[i]
    #print("{}{}".format("chknum is:",values[i]))

    for j in range(0,values[length-1]):
        chknum1 = chknum+values[j]
        len1 = len1+1
        #print("{}{}".format("chknum1:",chknum1))
        if len1 == length-1:
            break
        elif chknum1 == 8:
            #print("{} {} {}".format("numbers which adds to 8:",values[j], values[j+1]))
            print("{} {} {}".format("numbers which adds to 8:",chknum,values[j]))





