def and_gate(*args):
    x1,x2 = args[0], args[1]
    w1 = 1
    w2 = 1
    bias = 0
    if len(args) == 3:
        x3 = args[2]
        w3 = 1
        yin = w1*x1 + w2*x2 + w3*x3 + bias
        if yin>=3:
            yout = 1
        else:
            yout = 0
        return yout
    elif len(args) == 2:
        yin = w1*x1 + w2*x2 + bias
        if yin>=2:
            yout = 1
        else:
            yout = 0
        return yout

def or_gate(*args):
    x1,x2 = args[0], args[1]
    w1 = 1
    w2 = 1
    bias = 0
    if len(args) == 3:
        x3 = args[2]
        w3 = 1
        yin = w1*x1 + w2*x2 + w3*x3 + bias
    elif len(args) == 2:
        yin = w1*x1 + w2*x2 + bias
    if yin>=1:
        yout = 1
    else:
        yout = 0
    return yout

def xor_gate(*args):
    x1,x2 = args[0], args[1]
    w1 = 1
    w2 = 1
    bias = 0
    if len(args) == 3:
        x3 = args[2]
        w3 = 1
        list_xor =  [w1*x1,w2*x2,w3*x3]
        ones = list_xor.count(1)
    elif len(args) == 2:
        list_xor =  [w1*x1,w2*x2]
        ones = list_xor.count(1)
    if ones == 1:
        yout = 1
    else:
        yout = 0
    return yout

def xnor_gate(*args):
    yout = not_gate(xor_gate(*args))
    return yout

def not_gate(x1):
    yin = x1
    if yin==0:
        yout = 1
    else:
        yout = 0
    return yout

in1 = int(input("Enter input 1: "))
in2 = int(input("Enter input 2: "))

print("Value of AND output y: ", and_gate(in1,in2))
print("Value of OR output y: ", or_gate(in1,in2))
print("Value of NOT output y for input 1: ", not_gate(in1))
print("Value of NOT output y for input 2: ", not_gate(in2))
print("Value of XOR output y: ", xor_gate(in1,in2))
print("Value of XNOR output y: ", xnor_gate(in1,in2))

in3 = int(input("Enter input 3: "))

print("Value of AND output with 3 inputs y: ", and_gate(in1,in2,in3))
print("Value of OR output with 3 inputs y: ", or_gate(in1,in2,in3))
print("Value of NOT output y for input 3: ", not_gate(in3))
print("Value of XOR output with 3 inputs y: ", xor_gate(in1,in2,in3))
print("Value of XNOR output with 3 inputs y: ", xnor_gate(in1,in2,in3))
