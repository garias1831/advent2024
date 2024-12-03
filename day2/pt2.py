reports = list()
with open('input.txt', 'r') as f:
    for line in f:
        str_report = line.split()
        reports.append([int(lv) for lv in str_report])

#The algo is the same as pt1, but with a slight modification
#Top 10 brute search: try the current report, and removing every level, only unsafe if all fail

#Helper - check if a (undampened) report is safe 
def safe(report) -> bool:
    increasing = report[0] <= report[1]
    
    #We also need to keep track of subsequent levels to mantain the adjency invariant
    lastlv = report[0]
    for level in report[1:]:
        dist = abs(lastlv - level)
        if not (1 <= dist and dist <= 3):
            return False

        #Make sure we follow the pattern
        if increasing and lastlv >= level:
            return False
        elif (not increasing) and (lastlv <= level):
            return False
        lastlv = level
    
    return True

numsafe = 0
for report in reports:
    #Brute force: check if the report is safe, or if removing one level makes it safe
    if safe(report):
        numsafe += 1
        continue
    
    for i in range(len(report)):
        #Get segment excluding i
        left = report[:i]
        if i == len(report) - 1:
            right = []
        else:
            right = report[i+1:]
        damped = left + right
        
        if safe(damped):
            numsafe += 1
            break

print(f'Total number of safe reports:{numsafe}')