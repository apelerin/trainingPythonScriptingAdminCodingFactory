# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

def string_to_list(string):
    """
    Takes in a string, and return a list of characters of that string
    :param string:
    :return:
    """
    return [char for char in string]


def char_list_to_ascii_list(char_list):
    """
    Takes in a character list and return a list of ascii
    :param char_list:
    :return:
    """
    for i, char in enumerate(char_list):
        char_list[i] = ord(char)
    return char_list


def ascii_list_to_binary_list(ascii_list):
    """
    takes in a list of ascii values, and return a list of string binaries corresponding
    :param ascii_list:
    :return:
    """
    for i, char in enumerate(ascii_list):
        ascii_list[i] = bin(char).replace('b', '')
    return ascii_list


def string_list_to_string(string):
    """
    converts a string list to a string
    :param string:
    :return:
    """
    return ''.join(string)


def split_binary_to_block(string):
    """
    splits a binary string to a list of blocks of 6 characters when possible
    :param string:
    :return:
    """
    list_block = []
    i = 0
    block = ''
    for char in string:
        if i % 6 == 0 and i != 0:
            list_block.append(block)
            block = ''
        block += char
        i += 1
    if block != '':
        list_block.append(block)
    return list_block


def format_missing_zeros(list_binary):
    """
    formats the last element of a list of block binaries if there are less than 6 characters in it (filling with 0)
    :param list_binary:
    :return:
    """
    while len(list_binary[-1]) != 6:
        list_binary[-1] += '0'
    return list_binary


def binary_list_to_decimal_list(binary_list):
    """
    converts a binary list to a corresponding list of decimals
    :param binary_list:
    :return:
    """
    for index, value in enumerate(binary_list):
        binary_list[index] = int(value, 2)
    return binary_list


if __name__ == '__main__':
    original_string = input("Enter a string: ")
    splitted_list = string_to_list(original_string)
    ascii_list = char_list_to_ascii_list(splitted_list)
    binary_list = ascii_list_to_binary_list(ascii_list)
    string_binary = string_list_to_string(binary_list)
    list_block = split_binary_to_block(string_binary)
    print(list_block)
    list_block = format_missing_zeros(list_block)
    print(list_block)
    decimal_list = binary_list_to_decimal_list(list_block)
    print(decimal_list)