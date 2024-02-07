def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2],list[pos1]
    return list


#input List
list=[25,4,1996]

new_list = swapPositions(list, 0, 2)
print(f"{list[0]}/{list[1]}/{list[2]}")