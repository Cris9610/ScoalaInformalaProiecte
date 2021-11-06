my_list = [7,8,9,2,3,1,4,10,5,6]
my_list.sort(reverse=False)
my_list_impare = my_list[::2]
my_list_pare = my_list[1::2]
my_list_multiplu3 = my_list[2::3]

print ( my_list )

my_list.sort(reverse=True)

print ( my_list )
print ( my_list_impare)
print ( my_list_pare)
print ( my_list_multiplu3)