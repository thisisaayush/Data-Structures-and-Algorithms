"""

Author: Aayush Shahi Thakuri

"""
def average_of_positives_1(list):
    # initialization of sum, and size.
    sum = float(0)
    size = 0

    for i in range(len(list)):      #Iterates through each elements of a list.
        if(list[i] > 0):            #Checks if element in a list is positive or not.
            size = size + 1         #Counts the number of positive elements in a list (works as length).
            sum = sum + list[i]

    if size == 0:                   #Checks if the length of a list is 0 or not. If 0, simply returns 0.
        return 0                    # Mathematicial operation- division- for denominator 0 is not possible.

    else:                           #If length is not 0, it will simply return the average of positive number of a list.
        return sum / size


def average_of_positives_2(list):
    new_list = []                   #Secondary list which will contains just positive elements of a given list.

    for i in range(len(list)):
        if(list[i] > 0):
           new_list.append(list[i]) #Appends just positive elements to new_list from a given list.

    if len(new_list) == 0:
        return 0

    else:
        return sum(new_list) / len(new_list)






