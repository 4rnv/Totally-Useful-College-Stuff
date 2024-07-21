import random

def ones_complement(bin):
    mid = int(len(bin)/2)
    binhigh, binlow = bin[:mid], bin[mid:]
    print(binhigh, binlow)
    sum = []
    r = [0] * mid
    for i in range(mid,0,-1):
        s = int(binlow[i-1])+int(binhigh[i-1])+r[i-1]
        if s == 2: 
            s = 0
            r[i-2] = 1
        if s == 3:
            s =1
            r[i-2] = 1
        sum.append(s)
    print ("R bin =", r)
    sum.reverse()
    print(sum)
    sum_comp = ""
    for num in sum:
        if num == 1:
            num = 0
            #sum_comp.append(num)
            sum_comp += str(num)
        else:
            #sum_comp.append(num)
            num = 1
            sum_comp += str(num)
    print(sum_comp)
    return sum_comp

def sender():
    string = input("Enter binary string")
    try:
        bin = int(string, 2)
    except ValueError:
        print('Please make sure your number contains digits 0-1 only.')
    checksum = ones_complement(string)
    data = string + checksum
    #print(data)
    userinput = int(input("If you want to send corrupted data, press 1. Press 0 if no."))
    if userinput==1:
        twe(data)
    else:
        twoe(data)

def twoe(data):
    receive(data)

def twe(data):
    index = random.randint(0, 8-1)
    bit = '1' if data[index] == '0' else '0'
    corrupted_data = data[:index] + bit + data[index+1:]
    print("Data with error:", corrupted_data)
    receive(corrupted_data)

def receive(data):
    print(data)
    third = int(len(data)/3)
    binhigh, binmiddle, binlow = data[:third], data[third:2*third], data[2*third:]
    print(binhigh, binmiddle, binlow)

    # Convert binary strings to integers
    int_high = int(binhigh, 2)
    int_middle = int(binmiddle, 2)
    int_low = int(binlow, 2)
    
    sum_result = int_high + int_middle + int_low
    sum_bin = bin(sum_result)[2:] #Binary result 0bxxxx so get rid of 0b
    
    sum_bin_comp = ""
    for num in sum_bin:
        if num == 1:
            num = 0
            sum_bin_comp += str(num)
        else:
            num = 1
            sum_bin_comp += str(num)
    print(sum_bin_comp)

    if sum_bin_comp=="0000":
        print("No errors in transmission")
    else:
        print("Error in transmission")

sender()