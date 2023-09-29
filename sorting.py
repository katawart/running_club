
def reverse_bubble_sort(new_list):
    
    #Loops are used in sorting algorithms
    for i in new_list:
        for j in range(len(new_list)-1):
        #If the value at index 1 is greater than the value at index j
            if new_list[j] < new_list[j+1]:
            
            #Swap them over
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]

    return new_list

#Preconditions: Take an unsorted list
#Postcnditions: returns a list in accending order.
def bubble_sort(new_list):
    
    #Loops are used in sorting algorithms
    for i in new_list:
        for j in range(len(new_list)-1):
        #If the value at index 1 is greater than the value at index j
            if new_list[j] > new_list[j+1]:
            
            #Swap them over
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]

    return new_list




if __name__ == "__main__":
    print(reverse_bubble_sort([10,23,1,5]))