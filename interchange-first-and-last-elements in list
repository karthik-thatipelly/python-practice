'''
def swap_list(list):
    length = len(list)
    
    temp = list[0]
    list[0] = list[length - 1]
    list[length - 1] = temp
    
    return list
    
list = [12,35,9,56,24]

print(swap_list(list))
'''
'''
def swap_list(list):
    
    list[0], list[-1] = list[-1], list[0]
    
    return list
    
list = [12,35,9,56,24]

print(swap_list(list))
'''
'''
def swap_list(list):
    start, *middle, end = list
    list = [end, *middle, start]
    
    return list
    
list = [12,35,9,56,24]
print(swap_list(list))
'''

def swap_list(list):
    first = list.pop(0)
    last = list.pop(-1)
    
    list.insert(0, last)
    list.append(first)
    
    return list
    
list = [12,35,9,56,24]
print(swap_list(list))
    
