filename = input("input file name:    ")
filename += ".txt"
textbad = ""
try:
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    filelen = i + 1
    file=open(filename,'r')
    for i in range(filelen):
        try:
            textbad += file.readline()[42]
        except IndexError:
            continue
    text = textbad[1:]    
    print(text)
    file.close()
except FileNotFoundError:
    print("FILE NOT FOUND")
pulse = False
breaklen = 1
pulselen = 1
times = []
for i in range(len(text)):
    if text[i] != "0":
        if breaklen != 1:
            times.append(breaklen)
            breaklen = 1
        if pulse == True:
            pulselen += 1
        pulse = True
    else:
        if pulselen != 1:
            times.append(pulselen)
            pulselen = 1
        if pulse == False:
            breaklen += 1
        pulse = False
del times[0]
print(times)
del times[-1]
timesadd = []
for i in range(int(len(times)/2)):
    timesadd.append( times[2*i] + times[2*i+1] )
print(timesadd)
print(sum(timesadd)/len(timesadd))
input()
