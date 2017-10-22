# declaration of variables
from functools import reduce

size_of_teacher_list = int(input())

teacher_list = list(map(int, input().split()))
if size_of_teacher_list == 1:
    xor_of_teacher_list = teacher_list[0]
else:
    xor_of_teacher_list = reduce(lambda x, y: int(bin(x), 2) ^ int(bin(y), 2), teacher_list)

teacher_dict = dict([(teacher_list[i], i) for i in range(size_of_teacher_list)])


def get_result():
    for first_number in range(2 ** 30):
        mini = first_number - 2 ** 8
        for second_number in range(1 if mini <= 0 else mini, first_number + 2 ** 8 ):

            # checking that we don't have any numbers which already exists in teacher list

            if ((int(bin(first_number), 2) ^ int(bin(second_number), 2)) == xor_of_teacher_list) and \
                    (first_number not in teacher_dict) and (second_number not in teacher_dict):
                # output the result
                print(first_number, second_number)

                return


get_result()
