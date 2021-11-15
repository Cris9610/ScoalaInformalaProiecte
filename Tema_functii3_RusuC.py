def my_fct(val1):
    try:
        val_intr= int(val1)
        print(val1)
    except ValueError as e:
        print("0")
my_fct(input('nr intreg:'))