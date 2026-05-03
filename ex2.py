def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average_temperature(num_list)
    min, max = calc_min_max_temperature(num_list)
    print("Average Temperature=", avg)
    print("Minimum Temperature=", min)
    print("Maximum Temperature=", max)

def display_main_menu():
       print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    temp=input("enter temperatures:")
    num_list = temp.split(",")
    num_list = [int(x) for x in num_list]
    return num_list
    


def calc_average_temperature(temp):
    total = sum(temp)
    avg= total / len(temp)
    return avg

def calc_min_max_temperature(temp):
    min_temp = min(temp)
    max_temp = max(temp)
    return [min_temp, max_temp]

main()