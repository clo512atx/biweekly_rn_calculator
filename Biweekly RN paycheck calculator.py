#biweekly RN paycheck calculator

#collect wage rate information

wage=float(input("What is your hourly rate?: "))
ot_pay= (wage / 2)
holiday_pay= (wage / 2)
#shiftdiffpaywk_one=float(input("What is the shift differential amount?: "))
#shiftdiffpaywk_two=float(input("What is the shift differential amount?: "))


#week 1 calculations

hourswk_one=float(input("How many hours did you work in week one? : "))
ot_wk_one=float(input("How many hours are overtime in week one? (over 40 hours) : "))
shiftdiffwk_one=int(input("Did you have a shift differential in week one? (1: Yes\n 2: No)"))
if shiftdiffwk_one == 1:
    shiftdiffpaywk_one=float(input("What is the shift differential amount?: "))
    shifthourwk_one=float(input("How many hours of shift differential in week one? : "))    
else:
    shifthourwk_one= 0
    shiftdiffpaywk_one=0

holiday_wk1=int(input("Did you have holiday pay on week 1? (1: Yes\n 2: No) :"))
if holiday_wk1 == 1:
    hol_hourwk_one=float(input("How many hours of holiday in week one? : "))   
else:
    hol_hourwk_one= 0


#week 2 calculations

hourswk_two=float(input("How many hours did you work in week two? : "))
ot_wk_two=float(input("How many hours are overtime in week two? (over 40 hours) : "))
shiftdiffwk_two=int(input("Did you have a shift differential in week two? (1: Yes\n 2: No) :"))
if shiftdiffwk_two == 1:
    shiftdiffpaywk_two=float(input("What is the shift differential amount?: "))
    shifthourwk_two=float(input("How many hours of shift differential in week two? : "))
else:
    shifthourwk_two=0
    shiftdiffpaywk_two=0

holiday_wk2=int(input("Did you have holiday pay on week two? (1: Yes\n 2: No) :"))
if holiday_wk2 == 1:
    hol_hourwk_two=float(input("How many hours of holiday in week two? : "))   
else:
    hol_hourwk_two=0

'''Functions for gross and net pay
This is gross paycheck function. In order for net, need deductions: (taxes/SS/Medicare) 
'''

def pay():    
    paycheck= float((wage * (hourswk_one + hourswk_two)) + (ot_pay * (ot_wk_one + ot_wk_two)) + (shiftdiffpaywk_one * shifthourwk_one) + (shiftdiffpaywk_two * shifthourwk_two) + (holiday_pay * (hol_hourwk_one +hol_hourwk_two)))
    return paycheck

#net pay variables for function (SS=6.2 % and mc=1.45%)
ss= pay() * 0.062 
mc= pay() * 0.0145
contribute= int(input("What is the contribution percentage per pay period?"))
retirement= pay()* (contribute/100)

#netpay function
def finalpay():
    finalpaycheck= pay() - ss - mc- retirement
    return finalpaycheck

print("$",pay(), "is your estimated gross paycheck. ")
print("$",finalpay(),"is your net/take home paycheck")