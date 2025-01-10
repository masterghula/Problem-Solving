def tally(sl):
    counter = {}
    for names in sl:
        if names in counter:
            counter[names]+=1
        else:
            counter[names]=1
    for key, value in counter.items():
        print(key + ":" + str(value))


staff_list = ['Simon', 'Mark', 'Mark', 'Peter', 'Leo', 'George', 'George', 'Ian', 'Ian', 'Pat', 'Nicola', 'Ian']
tally(staff_list)