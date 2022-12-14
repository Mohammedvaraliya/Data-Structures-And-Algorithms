'''
You are given some integer as input, (i.e. ... -3, -2, -1, 0, 1, 2, 3 ...)
Convert the integer you are given to a string. 
Do not make use of the built-in "str" function.

Examples:

    Input: 123
    Output: "123"

    Input: -123
    Output: "-123"

'''


def int_to_str(input_int):
    
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []
    while input_int > 0:
        output_str.append(chr(ord('0') + input_int % 10))
        input_int //= 10
    
    output_str = output_str[::-1]
    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str



if __name__ == "__main__":

    int_1 = 123
    int_2 = -123

    X = int_to_str(int_1)
    print(X)
    print(type(X))
    print("\n")

    Y = int_to_str(int_2)
    print(Y)
    print(type(Y))


