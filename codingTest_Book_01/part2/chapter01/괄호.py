
for _ in range(int(input())) :
    stk = []
    vps = 'YES'

    for c in input() :
        if c == '(' :
            stk.append(c)
        else :
            if len(stk) > 0 :
                stk.pop()
            else :
                vps = 'NO'
    if len(stk) > 0 :
        vps = 'NO'
    print(vps)
        
            


