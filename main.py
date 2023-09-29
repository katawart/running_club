from record import *
from sorting import *

def main():
# The code you provided is a Python program that calculates whether a race record has been broken.
    mens_records = [9.58, 9.86, 9.87]  #World, European, British
    womens_records = [10.49, 10.73, 10.99] #World, European, British
    
    race_times = bubble_sort([10.5, 9.4, 11.2, 9.5])
    
    is_record_broken = record_broken(race_times,mens_records)

    print(is_record_broken)
    
if __name__ == "__main__":
    main()