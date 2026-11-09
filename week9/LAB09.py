# 1. Name:
#      Gabriel Wargha
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program is meant to get a list and reverse this list. 
# 4. What was the hardest part? Be as specific as possible.
#     The hard part for me was to understand that when I do des = array, I am just pointing to the array. 
#     My program was not working, after much attempts I asked for help to AI to identify why. 
#     Claude taught me about this principle that would be better to use [0] * len(array) to create an array of the same size. 
#      I read on the syllabus that we need to inform if we have any line that we got help, this line des = [0] * len(array) was the only one that I get help from Claude.
# 5. How long did it take for you to complete the assignment?
#      2h


def sort(array):
    size = len(array)
    src = array
    des = [0] * len(array)
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
        if(i_begin < i_end_1) and (i_begin_2 == i_end_2 or source[i_begin] < source[i_begin_2]):
            destination[i_destination] = source[i_begin]
            i_begin += 1
        
        else:
            destination[i_destination] = source[i_begin_2]
            i_begin_2 += 1
    
    return destination
                

if __name__ == "__main__":
    print(sort([1, 5, 3, 4, 2, 34, 12]))

