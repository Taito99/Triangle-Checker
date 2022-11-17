

def main():
    user_input_1 = int(input("Type in first value: "))
    user_input_2 = int(input("Type in second value: "))
    user_input_3 = int(input("Type in third value: "))

    input_list = [user_input_1, user_input_2, user_input_3]
    input_list.sort()
    max_value = input_list[2]
    min_value = input_list[0]
    medium_value = input_list[1]

    if max_value <= 0 or medium_value <= 0 or min_value <= 0:
        print("Values have to be positive")
    else:
        if min_value + medium_value >= max_value:
            print("This is triangle")
            if max_value == min_value and min_value == medium_value and max_value == medium_value:
                print("This is equilateral triangle")
            elif medium_value == min_value:
                print("This is isosceles triangle")

        else:
            print("This isn't triangle")

    print(f"Here are your values, Max value: {max_value}, Medium value: {medium_value}, and Minimal value: {min_value}")


if __name__ == "__main__":
    main()
