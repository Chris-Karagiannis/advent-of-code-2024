def read_lists(filename):
    infile = open(filename, 'r')
    line = infile.readline()
    left_list = []
    right_list = []

    while line != '':
        numbers = line.strip('\n').split('   ')
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))
        line = infile.readline()
    
    return [left_list, right_list]

# Part 1 - Difference between sorted lists
def list_difference(lists):
    left_list = lists[0]
    right_list = lists[1]  

    left_list.sort()
    right_list.sort()

    difference = 0

    for i in range(len(left_list)):
        temp_diff = abs(left_list[i] - right_list[i])
        difference += temp_diff

    return difference

# Part 2 - Similarity score comparing the lists
def similarity_score(lists):
    left_list = lists[0]
    right_list = lists[1]
    similarity_score = 0


    for i in range(len(left_list)):
        right_count = right_list.count(left_list[i])
        similarity_score += left_list[i] * right_count

    return similarity_score



lists = read_lists('input.txt')
print("Part 1:", list_difference(lists))
print("Part 2:", similarity_score(lists))