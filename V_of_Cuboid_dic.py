#make a dictionary of 5 keys and loop the function through each variable, store the answers in a list
figures = {'a':[5, 7, 9], 'b':[13, 22, 45], 'c':[34, 73, 86], 'd':[101, 243, 531], 'e':[555, 777, 999]}
volumes = []

for key in figures:
    l = figures[key][0]
    b = figures[key][1]
    h = figures[key][2]
    volume = l*b*h
    volumes.append(volume)

print(volumes)