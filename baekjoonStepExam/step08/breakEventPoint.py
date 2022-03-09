fixExpense, varExpense, ltPrice = input().split()

fixExpense = int(fixExpense)
varExpense = int(varExpense)
ltPrice = int(ltPrice)
benefit = 0
cnt = 0
 
if fixExpense > 2100000000 :
    exit()
elif varExpense > 2100000000 :
	exit()	
elif ltPrice > 2100000000 :	
    exit()
if varExpense > ltPrice :
    print('-1')
    exit()

while True :
    benefit = (ltPrice * cnt) - (varExpense * cnt) - fixExpense
    if benefit > 0 :
        break
    cnt += 1
print(cnt)
    
		
	
