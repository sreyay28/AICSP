import math
import time

#REALLY SLOW BUT RIGHT ALGORITHM


def gen_col9():
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

def gen_box9():
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

def gen_row9():
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

def gen_col12():
    col = {}
    col[0] = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132]
    col[1] = [1, 13, 25, 37, 49, 61, 73, 85, 97, 109, 121, 133]
    col[2] = [2, 14, 26, 38, 50, 62, 74, 86, 98, 110, 122, 134]
    col[3] = [3, 15, 27, 39, 51, 63, 75, 87, 99, 111, 123, 135]
    col[4] = [4, 16, 28, 40, 52, 64, 76, 88, 100, 112, 124, 136]
    col[5] = [5, 17, 29, 41, 53, 65, 77, 89, 101, 113, 125, 137]
    col[6] = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 138]
    col[7] = [7, 19, 31, 43, 55, 67, 79, 91, 103, 115, 127, 139]
    col[8] = [8, 20, 32, 44, 56, 68, 80, 92, 104, 116, 128, 140]
    col[9] = [9, 21, 33, 45, 57, 69, 81, 93, 105, 117, 129, 141]
    col[10] = [10, 22, 34, 46, 58, 70, 82, 94, 106, 118, 130, 142]
    col[11] = [11, 23, 35, 47, 59, 71, 83, 95, 107, 119, 131, 143]
    return col

def gen_box12():
    box = {}
    box[0] = [0, 1, 2, 3, 12, 13, 14, 15, 24, 25, 26, 27]
    box[1] = [4, 5, 6, 7, 16, 17, 18, 19, 28, 29, 30, 31]
    box[2] = [8, 9, 10, 11, 20, 21, 22, 23, 32, 33, 34, 35]
    box[3] = [36, 37, 38, 39, 48, 49, 50, 51, 60, 61, 62, 63]
    box[4] = [40, 41, 42, 43, 52, 53, 54, 55, 64, 65, 66, 67]
    box[5] = [44, 45, 46, 47, 56, 57, 58, 59, 68, 69, 70, 71]
    box[6] = [72, 73, 74, 75, 84, 85, 86, 87, 96, 97, 98, 99]
    box[7] = [76, 77, 78, 79, 88, 89, 90, 91, 100, 101, 102, 103]
    box[8] = [80, 81, 82, 83, 92, 93, 94, 95, 104, 105, 106, 107]
    box[9] = [108, 109, 110, 111, 120, 121, 122, 123, 132, 133, 134, 135]
    box[10] = [112, 113, 114, 115, 124, 125, 126, 127, 136, 137, 138, 139]
    box[11] = [116, 117, 118, 119, 128, 129, 130, 131, 140, 141, 142, 143]
    return box

def gen_row12():
    rows = {}
    rows[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    rows[1] = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    rows[2] = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    rows[3] = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
    rows[4] = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
    rows[5] = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    rows[6] = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
    rows[7] = [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
    rows[8] = [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]
    rows[9] = [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
    rows[10] = [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]
    rows[11] = [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]
    return rows

def gen_col16():
    col = {}
    col[0] = [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]
    col[1] = [1, 17, 33, 49, 65, 81, 97, 113, 129, 145, 161, 177, 193, 209, 225, 241]
    col[2] = [2, 18, 34, 50, 66, 82, 98, 114, 130, 146, 162, 178, 194, 210, 226, 242]
    col[3] = [3, 19, 35, 51, 67, 83, 99, 115, 131, 147, 163, 179, 195, 211, 227, 243]
    col[4] = [4, 20, 36, 52, 68, 84, 100, 116, 132, 148, 164, 180, 196, 212, 228, 244]
    col[5] = [5, 21, 37, 53, 69, 85, 101, 117, 133, 149, 165, 181, 197, 213, 229, 245]
    col[6] = [6, 22, 38, 54, 70, 86, 102, 118, 134, 150, 166, 182, 198, 214, 230, 246]
    col[7] = [7, 23, 39, 55, 71, 87, 103, 119, 135, 151, 167, 183, 199, 215, 231, 247]
    col[8] = [8, 24, 40, 56, 72, 88, 104, 120, 136, 152, 168, 184, 200, 216, 232, 248]
    col[9] = [9, 25, 41, 57, 73, 89, 105, 121, 137, 153, 169, 185, 201, 217, 233, 249]
    col[10] = [10, 26, 42, 58, 74, 90, 106, 122, 138, 154, 170, 186, 202, 218, 234, 250]
    col[11] = [11, 27, 43, 59, 75, 91, 107, 123, 139, 155, 171, 187, 203, 219, 235, 251]
    col[12] = [12, 28, 44, 60, 76, 92, 108, 124, 140, 156, 172, 188, 204, 220, 236, 252]
    col[13] = [13, 29, 45, 61, 77, 93, 109, 125, 141, 157, 173, 189, 205, 221, 237, 253]
    col[14] = [14, 30, 46, 62, 78, 94, 110, 126, 142, 158, 174, 190, 206, 222, 238, 254]
    col[15] = [15, 31, 47, 63, 79, 95, 111, 127, 143, 159, 175, 191, 207, 223, 239, 255]
    return col

def gen_box16():
    box = {}
    box[0] = [0, 1, 2, 3, 16, 17, 18, 19, 32, 33, 34, 35, 48, 49, 50, 51]
    box[1] = [4, 5, 6, 7, 20, 21, 22, 23, 36, 37, 38, 39, 52, 53, 54, 55]
    box[2] = [8, 9, 10, 11, 24, 25, 26, 27, 40, 41, 42, 43, 56, 57, 58, 59]
    box[3] = [12, 13, 14, 15, 28, 29, 30, 31, 44, 45, 46, 47, 60, 61, 62, 63]

    box[4] = [64, 65, 66, 67, 80, 81, 82, 83, 96, 97, 98, 99, 112, 113, 114, 115]
    box[5] = [68, 69, 70, 71, 84, 85, 86, 87, 100, 101, 102, 103, 116, 117, 118, 119]
    box[6] = [72, 73, 74, 75, 88, 89, 90, 91, 104, 105, 106, 107, 120, 121, 122, 123]
    box[7] = [76, 77, 78, 79, 92, 93, 94, 95, 108, 109, 110, 111, 124, 125, 126, 127]

    box[8] = [128, 129, 130, 131, 144, 145, 146, 147, 160, 161, 162, 163, 176, 177, 178, 179]
    box[9] = [132, 133, 134, 135, 148, 149, 150, 151, 164, 165, 166, 167, 180, 181, 182, 183]
    box[10] = [136, 137, 138, 139, 152, 153, 154, 155, 168, 169, 170, 171, 184, 185, 186, 187]
    box[11] = [140, 141, 142, 143, 156, 157, 158, 159, 172, 173, 174, 175, 188, 189, 190, 191]

    box[12] = [192, 193, 194, 195, 208, 209, 210, 211, 224, 225, 226, 227, 240, 241, 242, 243]
    box[13] = [196, 197, 198, 199, 212, 213, 214, 215, 228, 229, 230, 231, 244, 245, 246, 247]
    box[14] = [200, 201, 202, 203, 216, 217, 218, 219, 232, 233, 234, 235, 248, 249, 250, 251]
    box[15] = [204, 205, 206, 207, 220, 221, 222, 223, 236, 237, 238, 239, 252, 253, 254, 255]

    return box

def gen_row16():
    rows = {}
    rows[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    rows[1] = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    rows[2] = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
    rows[3] = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    rows[4] = [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
    rows[5] = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
    rows[6] = [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
    rows[7] = [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]
    rows[8] = [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]
    rows[9] = [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]
    rows[10] = [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175]
    rows[11] = [176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191]
    rows[12] = [192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207]
    rows[13] = [208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223]
    rows[14] = [224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239]
    rows[15] = [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]

    return rows


def gen_adjs(row, col, box, size):
    adjs = {}
    for index in range(0, size*size):
        row_adjs = get_row(index, row)
        col_adjs = get_col(index, col)
        box_adjs = get_box(index, box)

        list = set()

        for i in range(0, len(row_adjs)):
            list.add(row_adjs[i])
            x = col_adjs[i]
            list.add(x)
            s = box_adjs[i]
            list.add(s)
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

def gen_domain9():
    domain_dict = {}
    for i in range(0, 81):
        domain_dict[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return domain_dict

def gen_domain12():
    domain_dict = {}
    for i in range(0, 144):
        domain_dict[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C']
    return domain_dict

def gen_domain16():
    domain_dict = {}
    for i in range(0, 144):
        domain_dict[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    return domain_dict

def backtracking_search(assignment, adjs, domain_dict, size):
    return recursive_backtracking(assignment, adjs, domain_dict, size)

def recursive_backtracking(assignment, adjs, domain_dict, size):

    if isComplete(assignment, size):
        return assignment

    var = find(domain_dict, assignment)
    for value in domain_dict[var]:
        bool = check_num(value, var, adjs, assignment)
        if (bool):
            assignment[var] = value
            result = recursive_backtracking(assignment, adjs, domain_dict, size)
            if (result == None):
                del assignment[var]
            else:
                return result
    return None

def check_num(value, var, adjs, assignment):
    for neighbor in adjs[var]:
        if neighbor in assignment:
            if ord(str(assignment[neighbor])) == ord(str(value)):
                return False
    return True

def isComplete(assignment, size):
    if len(assignment) == size * size:
        return True
    return False


def find(domains, assignment):

    min = 20
    val = 0
    for key in domains:
        length = len(domains[key])
        bool = key not in assignment
        if(length < min and bool):
            val = key
            min = length
    return val

def checksum(result, size):
    total = 0
    for i in result:
        total = total + ord(str(result[i]))
    return total - (48 * size * size)

def main():
    cur_time = time.time()

    rows9 = gen_row9()
    cols9 = gen_col9()
    boxes9 = gen_box9()
    adjs9 = gen_adjs(rows9, cols9, boxes9, 9)
    domain9 = gen_domain9()

    rows12 = gen_row12()
    cols12 = gen_col12()
    boxes12 = gen_box12()
    adjs12 = gen_adjs(rows12, cols12, boxes12, 12)
    domain12 = gen_domain12()

    rows16 = gen_row16()
    cols16 = gen_col16()
    boxes16 = gen_box16()
    adjs16 = gen_adjs(rows16, cols16, boxes16, 16)
    domain16 = gen_domain16()

    count = 1

    puzzles = open("NbyN_sample.txt", 'r')
    for line in puzzles:
        assignment = {}
        initial = line
        size = math.sqrt(len(initial) - 1)
        for i in range(len(initial) - 1):
            if initial[i] != '.':
                assignment[i] = initial[i]
        if size == 9:
            result = backtracking_search(assignment, adjs9, domain9, size)
        if size == 12:
            result = backtracking_search(assignment, adjs12, domain12, size)
        if size == 16:
            result = backtracking_search(assignment, adjs16, domain16, size)

        print("Puzzle " + str(count), end = " ")
        for i in range(0, int(size)*int(size)):
            print(result[i], end="")
        print(" " + str(checksum(result, size)))


        count += 1

    next_time = time.time()
    print((next_time - cur_time))

if __name__ == '__main__':
    main()
