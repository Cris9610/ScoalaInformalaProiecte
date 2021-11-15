#Suma tuturor numerelor de la [0, n]

# def my_fct(n=int(input("nr intreg: "))):
#     if n==0:
#         return 0
#     return n + my_fct(n-1)
# print(my_fct())

#Suma tuturor numerelor pare de la [0, n]

# def my_fct(n=int(input("nr intreg: "))):
#     if n==0:
#         return 0
#     elif n % 2 == 0:
#         return n + my_fct(n-2)
#     elif n % 2 != 0:
#         return my_fct(n-1)
# print(my_fct())

#Suma tuturor numerelor impare de la [0, n]

def my_fct(n=int(input("nr intreg: "))):
    if n==0:
        return 0
    elif n % 2 == 0:
        return my_fct(n-1)
    elif n % 2 != 0:
        return n + my_fct(n-1)
print(my_fct())