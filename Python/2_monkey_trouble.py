def monkey_trouble(a_smile, b_smile):
    if((a_smile and b_smile)or( not a_smile and not b_smile)):
        return True
    else:
        return False


x = monkey_trouble(True, False)
print(x)
