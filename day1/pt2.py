'''(slightly better) Quadtratic-time brute force mthd'''

#Unpack the input
left_ids = list()
right_ids = list()
with open('input.txt', 'r') as f:
    for line in f:
        idl, idr = line.split()
        left_ids.append(int(idl))
        right_ids.append(int(idr))

counts = dict()
similarity_score = 0
#Store dict of the counts so far, so we can lookup if 
#we've seen a number already
for l in left_ids:
    #We've already counted occurences in the right list, so just add the score
    if l in counts:
        similarity_score += l * counts[l]
        continue
    
    #If we reach this, we have to count the occurences in the right
    counts[l] = 0
    for r in right_ids:
        if r == l:
            counts[l] += 1
    
    similarity_score += l * counts[l]

print(f'The total similarity score is {similarity_score}.')

