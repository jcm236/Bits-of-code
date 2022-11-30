
def math1(exp):
    bits = []
    bitstemp = ""
    inb = False
    inb2 = False
    x = -1
    for letter in exp:
        x += 1
        if letter == "(" and inb == False and inb2 == False:
            inb = True
            bits.append(bitstemp)
            bitstemp= ""
            continue
        
        if inb == True and inb2 == False:
            if letter == "(":
               inb2 = True
               continue
            if letter == ")":
                inb = False
                bits.append(bitstemp)
                continue
            bitstemp += letter
        else:
            if inb2 == False:
                bitstemp += letter
        if inb2 == True:
            xx = x - 2
            if letter == ")":
                bitstemp += str(math1(exp[xx:x+1])).replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace(",", "")
                inb2 = False
        
    return bits
def math2(exp):
    r = ""
    calc = ""
    nums = "0123456789"
    cal = "*/-+"
    var = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for e in exp:
        for letter in e:
            if letter in nums:
                calc += "num"
            if letter in cal:
                calc += "cal"
            if letter in var:
                calc += "var"
    if calc == "numcalnum":
        if exp[1] == "*":
            r += exp[0] * exp[2]
        if exp[1] == "/":
            
        
print(math1("5*(3-(5))"))
