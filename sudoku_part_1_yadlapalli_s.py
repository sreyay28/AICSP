import time

def gen_col():
    col = {}
    col[0] = [0, 9, 18, 27, 36, 45, 54, 63, 72]
    col[1] = [1, 10, 19, 28, 37, 46, 55, 64, 73]
    col[2] = [2, 11, 20, 29, 38, 47, 56, 65, 74]
    col[3] = [3, 12, 21, 30, 39, 48, 57, 66, 75]
    col[4] = [4, 13, 22, 31, 40, 49, 58, 67, 76]
    col[5] = [5, 14, 23, 32, 41, 50, 59, 68, 77]
    col[6] = [6, 15, 24, 33, 42, 51, 60, 69, 78]
    col[7] = [7, 16, 25, 34, 43, 52, 61, 70, 79]
    col[8] = [8, 17, 26, 35, 44, 53, 62, 71, 80]
    return col

def gen_box():
    box = {}
    box[0] = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    box[1] = [3, 4, 5, 12, 13, 14, 21, 22, 23]
    box[2] = [6, 7, 8, 15, 16, 17, 24, 25, 26]
    box[3] = [27, 28, 29, 36, 37, 38, 45, 46, 47]
    box[4] = [30, 31, 32, 39, 40, 41, 48, 49, 50]
    box[5] = [33, 34, 35, 42, 43, 44, 51, 52, 53]
    box[6] = [54, 55, 56, 63, 64, 65, 72, 73, 74]
    box[7] = [57, 58, 59, 66, 67, 68, 75, 76, 77]
    box[8] = [60, 61, 62, 69, 70, 71, 78, 79, 80]
    return box

def gen_row():
    rows = {}
    rows[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    rows[1] = [9, 10, 11, 12, 13, 14, 15, 16, 17]
    rows[2] = [18, 19, 20, 21, 22, 23, 24, 25, 26]
    rows[3] = [27, 28, 29, 30, 31, 32, 33, 34, 35]
    rows[4] = [36, 37, 38, 39, 40, 41, 42, 43, 44]
    rows[5] = [45, 46, 47, 48, 49, 50, 51, 52, 53]
    rows[6] = [54, 55, 56, 57, 58, 59, 60, 61, 62]
    rows[7] = [63, 64, 65, 66, 67, 68, 69, 70, 71]
    rows[8] = [72, 73, 74, 75, 76, 77, 78, 79, 80]
    return rows

def gen_adjs(row, col, box):
    adjs = {}
    for index in range(0, 81):
        row_adjs = get_row(index, row)
        col_adjs = get_col(index, col)
        box_adjs = get_box(index, box)

        list = set()

        for i in range(0, len(row_adjs)):
            list.add(row_adjs[i])
            list.add(col_adjs[i])
            list.add(box_adjs[i])
        adjs[index] = list
    return adjs

def get_row(index, rows):
    for row in rows:
        if index in rows[row]:
            return rows[row]
    return None

def get_col(index, cols):
    for col in cols:
        if index in cols[col]:
            return cols[col]
    return None

def get_box(index, boxes):
    for box in boxes:
        if index in boxes[box]:
            return boxes[box]
    return None

def gen_domain():
    domain_dict = {}
    for i in range(0, 81):
        domain_dict[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return domain_dict

def backtracking_search(assignment, adjs, domain_dict):
    return recursive_backtracking(assignment, adjs, domain_dict)

def recursive_backtracking(assignment, adjs, domain_dict):

    if isComplete(assignment):
        return assignment

    var = find(domain_dict, assignment)
    for value in range(1,10):
        bool = check_num(value, var, adjs, assignment)
        if(bool):
            assignment[var] = value
            domain_dict = del_domain(var, value, adjs, domain_dict)
            result = recursive_backtracking(assignment, adjs, domain_dict)
            if(result == None):
                del assignment[var]
                domain_dict = add_domain(var, value, adjs, domain_dict)
            else:
                return result
    return None

def del_domain(orig, value, adjs, domain):
    for adj in adjs[orig]:
        possibilities = domain[adj]
        if value in possibilities:
            possibilities.remove(value)
            domain[adj] = possibilities
    return domain

def add_domain(orig, value, adjs, domain):
    for adj in adjs[orig]:
        possibilities = domain[adj]
    if value not in possibilities:
        possibilities.append(value)
    domain[adj] = possibilities
    return domain

def check_num(value, var, adjs, assignment):
    for neighbor in adjs[var]:
        if neighbor in assignment:
            if assignment[neighbor] == value:
                return False
    return True

def isComplete(assignment):
    if len(assignment) == 81:
        return True
    return False

def find(domains, assignment):
    min = 10
    val = 0
    for key in domains:
        length = len(domains[key])
        bool = key not in assignment
        if(length < min and bool):
            val = key
            min = length
    return val

def finish(result):
    print(str(result[0]) + " " + str(result[1]) + " " + str(result[2]) + "   "  + \
            str(result[3]) + " " + str(result[4]) + " " + str(result[5]) + "   " + \
          str(result[6]) + " " + str(result[7]) + " " + str(result[8]))

    print(str(result[9]) + " " + str(result[10]) + " " + str(result[11]) + "   "  + \
            str(result[12]) + " " + str(result[13]) + " " + str(result[14]) + "   " + \
          str(result[15]) + " " + str(result[16]) + " " + str(result[17]))

    print(str(result[18]) + " " + str(result[19]) + " " + str(result[20]) + "   "  + \
            str(result[21]) + " " + str(result[22]) + " " + str(result[23]) + "   " + \
          str(result[24]) + " " + str(result[25]) + " " + str(result[26]))

    print()

    print(str(result[27]) + " " + str(result[28]) + " " + str(result[29]) + "   " + \
          str(result[30]) + " " + str(result[31]) + " " + str(result[32]) + "   " + \
          str(result[33]) + " " + str(result[34]) + " " + str(result[35]))

    print(str(result[36]) + " " + str(result[37]) + " " + str(result[38]) + "   " + \
          str(result[39]) + " " + str(result[40]) + " " + str(result[41]) + "   " + \
          str(result[42]) + " " + str(result[43]) + " " + str(result[44]))

    print(str(result[45]) + " " + str(result[46]) + " " + str(result[47]) + "   " + \
          str(result[48]) + " " + str(result[49]) + " " + str(result[50]) + "   " + \
          str(result[51]) + " " + str(result[52]) + " " + str(result[53]))

    print()

    print(str(result[54]) + " " + str(result[55]) + " " + str(result[56]) + "   " + \
          str(result[57]) + " " + str(result[58]) + " " + str(result[59]) + "   " + \
          str(result[60]) + " " + str(result[61]) + " " + str(result[62]))

    print(str(result[63]) + " " + str(result[64]) + " " + str(result[65]) + "   " + \
          str(result[66]) + " " + str(result[67]) + " " + str(result[68]) + "   " + \
          str(result[69]) + " " + str(result[70]) + " " + str(result[71]))

    print(str(result[72]) + " " + str(result[73]) + " " + str(result[74]) + "   " + \
          str(result[75]) + " " + str(result[76]) + " " + str(result[77]) + "   " + \
          str(result[78]) + " " + str(result[79]) + " " + str(result[80]))

def main():
    cur_time = time.time()
    assignment = {}
    initial = input("Type 81 char input: ")
    print("INITIAL STATE: ")
    print("---------------------")
    finish(initial)
    for i in range(len(initial)):
        if initial[i] != '.':
           assignment[i] = int(initial[i])

    rows = gen_row()
    cols = gen_col()
    boxes = gen_box()

    adjs = gen_adjs(rows, cols, boxes)
    domain = gen_domain()

    for var in assignment:
        value = assignment[var]
        for neighbor in adjs[var]:
            poss = domain[neighbor]
            if value in poss:
                poss.remove(value)
            domain[neighbor] = poss

    result = backtracking_search(assignment, adjs, domain)

    print()
    print("SOLUTION: ")
    print("---------------------")
    finish(result)

    next_time = time.time()
    print((next_time - cur_time))

if __name__ == '__main__':
    main()
