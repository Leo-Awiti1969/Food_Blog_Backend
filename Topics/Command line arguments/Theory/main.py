# import sys
#
# args = sys.argv
#
# if len(args) != 3:
#     print("The script should be called with two arguments, the first and the second number to be multiplied")
#
# else:
#     first_num = float(args[1])
#     second_num = float(args[2])
#
#     # product = first_num * second_num
#
#     # print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))
#
#     print(first_num, second_num)

words_selection = []
with open('words.txt', 'r') as test_file:
    words = test_file.read()
    # print(words)
    for word in words:
        words_selection.append(word)

print(*[''.join(words_selection).replace('\\', ',')])
