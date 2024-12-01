#Unpack input into the two lists
left_ids = list()
right_ids = list()
with open('input.txt', 'r') as f:
    for line in f:
        idl, idr = line.split()
        left_ids.append(idl)
        right_ids.append(idr)

assert len(left_ids) == len(right_ids)

#Sort the lists; so (l[i], r[i]) will correspond to the smallest pair from each list
left_ids = sorted(left_ids)
right_ids = sorted(right_ids)

totaldist = 0
for idl, idr in zip(left_ids, right_ids):
    #add to the dist
    totaldist += abs(int(idl) - int(idr))

print(f'The total distance between the ids is {totaldist}.')


       