# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


def sort(array):
    size = len(array)
    src = array
    des = array
    num = 2
    
    while num > 1:
        num = 0
        i_begin = 0
        
        while i_begin < size:
            i_end_1 = i_begin + 1
            
        while i_end_1 < size and src[i_end_1 - 1] <= src[i_end_1]:
            i_end_1 += 1
        
        i_begin_2 = i_end_1
        
        if i_begin_2 < size:
            i_end_2 = i_begin_2 + 1
            
        else:
            i_end_2 = i_begin_2
        
        while i_end_2 < size and src[i_end_2 - 1] <= src[i_end_2]:
            i_end_2 += 1
        
        num += 1
        combine(src, des, i_begin, i_begin_2, i_end_2)
        i_begin = i_end_2
        
        temp = des
        des = src
        src = temp
            
    return src


def combine(source, destination, i_begin, i_begin_2, i_end_2):
    i_end_1 = i_begin_2
    
    for i_destination in range (i_begin, i_end_2):
        if(i_begin < i_end_1) and (i_begin_2 ==i_end_2 or source[i_begin] < source[i_begin_2]):
            destination[i_destination] = source[i_begin]
            i_begin += 1
        
        else:
            destination[i_destination] = source[i_begin_2]
            i_begin_2+= 1
    
    return destination
                

if __name__ == "__main__":
    print(sort([1, 5, 3]))
