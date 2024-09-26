def check_reverse(data):
    reverse_data=data[::-1] #It creates a reversed copy of the list.
    if data==sorted(data):
         print(f"your data is in sorted array: reverse it:, {reverse_data}")
        #print(data[::-1]) #It creates a reversed copy of the list.
    elif data==sorted (data, reverse=True):
         print(f"input is in descending order: ,{reverse_data}")
         #print(data[::-1])
a_str=input("Enter your desired data(number seprated by space): ")
data=list(map(int, a_str.split())) #Splitting the input string by spaces, creating a list of strings.,Applying the int function to each element in the list, converting the strings to integers.
check_reverse(data)