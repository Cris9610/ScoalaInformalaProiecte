# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.
# -your_function(1, 5, -3, 'abc', [12, 56, 'cad']) va returna 3 (1 + 5 - 3).
# -your_function() va returna 0.
# -your_function(2, 4, 'abc', param_1=2) va returna 6 (2 + 4).

def my_sum(*args,**kwargs):
    result = 0
    for x in args:
        if isinstance(x,int):
            result += x
        else:
            pass
    return result

print(my_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
