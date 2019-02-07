import csv
def task2():
    street = []
    newstreet = []
    reader1 = open('Street_Centrelines.csv', 'r')
    reader2 = open('Bus_Stops.csv', 'r')
    for r in reader1:
        nread = r.split(",")
        if nread[10] == "MINOR COLLECTOR":
            stree = nread[4].strip()
            stree = stree.lower()
            if stree not in street:
                 street.append(stree)
    for stre in street:
         if stre not in newstreet:
             newstreet.append(stre)    
    metro = []
    for st in newstreet:
        for dir in reader2:
            ndir = dir.split(",")
            if ndir[7] == "Inaccessible":
                stack = ndir[6].strip()
                stack = stack.lower()
                if stack.find(st) >= 0:
                     metro.append(ndir[2])              
    print("Stop Number    |    Location    |    FCODE")
    for bus in metro:
        for char in open('Bus_Stops.csv', 'r'):
            newchar = char.split(",")
            if newchar[2].find(bus) >= 0:
                print(newchar[4],"",newchar[6],"",newchar[10])
task2()

