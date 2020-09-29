def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    toBase = Stack()
    while decNumber > 0:
        rem = decNumber % base
        toBase = rem.push()
        decNumber = decNumber // base

    result = ""

    while not toBase.isEmpty():
        result = result + digits[toBase.pop()]

    return result


