

#Precondition: Takes two parameters, a list of race times, and a list of records.
#Postconditions: Returns a string stating if the World, European, British, or no record has been broken
def record_broken(list_of_times, list_of_records):
    
    for i in list_of_times:
        if i < list_of_records[0]:
            return "World record broken"
        elif i < list_of_records[1]:
            return "European record broken"
        elif i < list_of_records[2]:
            return "British record broken"
        else:
            return "No record broken"



if __name__ == "__main__":
    print(record_broken([9.5, 9.8, 10.1, 11.0], [9.58, 9.86, 9.87]))