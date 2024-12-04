import math

def read_reports(filename):
    infile = open(filename, 'r')
    line = infile.readline()
    reports_list = []

    while line != '':
        report = line.strip('\n').split(' ')
        reports_list.append(report)
        line = infile.readline()

    return reports_list

# Function to check if report is safe
def is_safe(report):
    change = 0

    for i in range(1, len(report)):
        diff = int(report[i]) - int(report[i - 1])
        new_change = math.copysign(1, diff)
        abs_diff = abs(diff)

        # If unsafe
        if abs_diff > 3 or abs_diff < 1 or (change != new_change and change != 0):
            return False
        
        # Update previous change if pass test
        change = new_change    

    return True
            

# Part 1 - Count safe levels
def count_safe(reports_list):
    safe = 0

    for report in reports_list:
        if is_safe(report):
            safe += 1
    
    return safe

# Part 2 - Count safe levels with problem dampener
def count_safe_dampener(reports_list):
    safe = 0

    for report in reports_list:
        check_safe = is_safe(report)

        if check_safe == False:
            for ignore in range(len(report)):
                check_list = []
                for index in range(len(report)):
                    if index != ignore:
                        check_list.append(report[index])
                    
                if is_safe(check_list):
                    check_safe = True
                    break
        
        if check_safe == True:
            safe += 1
        
    return safe


reports_list = read_reports('input.txt')
print("Part 1:", count_safe(reports_list))
print("Part 2:", count_safe_dampener(reports_list))