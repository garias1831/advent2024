'''Brute force approach'''

reports = list()
with open('input.txt', 'r') as f:
    for line in f:
        str_report = line.split()
        reports.append([int(lv) for lv in str_report])


numsafe = 0
#Loop through all of the reports, checking the invariants
for report in reports:
    
    #First two elems establish if we should continuously be decreasing or increasing
    increasing = report[0] <= report[1]
    
    #We also need to keep track of subsequent levels to mantain the adjency invariant
    lastlv = report[0]
    unsafe = False
    for level in report[1:]:
        dist = abs(lastlv - level)
        if not (1 <= dist and dist <= 3):
            unsafe = True
            break #violates adjacency invariant

        #Make sure we follow the pattern
        if increasing and lastlv >= level:
            unsafe = True
            break #level is a decrease from last
        elif (not increasing) and (lastlv <= level):
            unsafe = True
            break #Violates decreasing
        lastlv = level

    if not unsafe: 
        numsafe += 1

print(f'Total number of safe reports:{numsafe}')