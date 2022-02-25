




# ! Loops
# 


#  2 types of loops
# while 
# for


# for i in range(10, 100, 20):
#     print(i, end=" ")


#? range(stop) -> [0 ; stop)
#? range(start, stop) -> [start; stop)
#? range(start, stop, step)

# for i in range(200, 99, -2):
#     print(i, end=" ")

# for i in range(1, 11):
#     print(f"9 x {i} = {9 * i}")





# def print_mult_table(num, up_to):
#     for i in range(1, up_to + 1):
#         print(f"{num} x {i} = {num * i}")
# print(print_mult_table(4, 10))



# def exponens_table(num, up):
#     for i in range(1, up + 1):
#         print(f"{num} ** {i} = {num ** i}")
# print(exponens_table(5, 10))        





# for i in range():      in range() we can not use float numbers
#     print(i)




# for letter in "Ramziddin Velikiy":
#     if letter == " ":
#         continue 
#     else:
#         print(letter, end=" ")






# print("ramziddin". upper())
# print("Ramziddin". lower())
# print("R". isupper())
# print("ramziddin". isupper())



new_str = " "
for letter in "Ramziddin Bakhridinof is a student":
    new_str = new_str + letter.swapcase()
print(new_str)



