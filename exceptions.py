# Exception handling
def division(a, b):
    try:
        if type(a)==str or type(b)==str:
            return int(a)/int(b)
        return a/b
    except ZeroDivisionError as zde:
        print(zde)
        return f"you can not devide to zero"
    except:
        return f"please check your input."


def division2(a, b):
    if type(a)==str or type(b)==str:
        return int(a)/int(b)
    return a/b

#  Testing your code\
print()
print(division(45, 90))
print(division('45', 0))
print(division(-45, 90))
print(division('45', 90))
print(division('45', '90'))
print(division('john', 'doe'))
