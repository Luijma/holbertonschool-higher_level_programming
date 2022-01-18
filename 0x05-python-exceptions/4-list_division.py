#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    new_list = []
    while(index < list_length):
        try:
            new_list.append(my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except (ValueError, TypeError):
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            index += 1
    return new_list
