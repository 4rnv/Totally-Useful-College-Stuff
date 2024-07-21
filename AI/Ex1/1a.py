def verify(state, direction):
    if direction == "xtoy":
        temp_y = state[1] + state[0]
    elif direction == "ytox":
        temp_x = state[0] + state[1]
    else:
        return False  # Invalid direction
    
    if direction == "xtoy":
        if temp_y <= 3:
            return True
        else:
            print("Exceeding jug limit")
            return False
    elif direction == "ytox":
        if temp_x <= 4:
            return True
        else:
            print("Exceeding jug limit")
            return False
        
x = 3
y = 4
flag = 1
state_true = [0,0]
state = [0,0]
print('''
1: Fill jug X
2: Fill jug y
3: Empty jug X
4: Empty jug y
5: Transfer from x to y
6: Transfer from y to x
7: Transfer some from x to y
8: Transfer some from y to x
''')

while flag>0:
    uinput = input("Enter your choice")
    uinput = int(uinput)
    if(uinput==1):
        state = state_true
        state[0] = 4
        print(state_true)
        state_true = state
    elif(uinput==2):
        state = state_true
        state[1] = 3
        print(state_true)
        state_true = state
    elif(uinput==3):
        state = state_true
        if(state[0]==0):
            print("X is already empty")
        else:
            state[0]=0
        print(state_true)
        state_true = state
    elif(uinput==4):
        state = state_true
        if(state[1]==0):
            print("Y is already empty")
        else:
            state[1]=0
        print(state_true)
        state_true = state
    elif(uinput==5):
        state = state_true
        if(verify(state, direction="xtoy")):
            state_true = state
            state[0]=0
        else:
            state = state_true
        print(state_true)
    elif(uinput==6):
        state = state_true
        if(verify(state, direction="ytox")):
            state[0] = state[0] + state[1]
            state_true = state
            state[1]=0
        else:
            state = state_true
        print(state_true)
    elif(uinput==7):
        pass
    elif(uinput==8):
        pass
    elif(uinput==0):
        flag = 0
    else:
        print("Invalid input")
