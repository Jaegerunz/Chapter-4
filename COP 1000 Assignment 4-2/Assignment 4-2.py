#This will be assignment 4-2
#Productivity = (dollarValue/ numTransacitons) / numShiftsWorked
#<=30=$50, 31-69 = $75, 70-199= $100, >=200= $200


#declarations
dollarValue= 0.00
numTransactions= 0.00
numShiftsWorked = 0.00
productivityScore= 0.00
employeeBonus= 0.00
employeeName="string"
#input?
employeeName=input("Employee Name?:")
numShiftsWorked=int(input("How many shifts were worked?:"))
numTransactions=int(input("How many transactions were performed?"))
dollarValue=int(input("Total Dollar value of transactions?:"))
#bonus calculations here

productivityScore=(dollarValue/numTransactions)/ numShiftsWorked
if productivityScore <=30:
    employeeBonus=50.00
else:
    if productivityScore <= 69:
        employeeBons=75.00
    else:
        if productivityScore <= 199:
            employeeBonus=100
        else:
            if productivityScore >= 200:
                employeeBonus=200
#tests
#print(str(productivityScore))
#print(str(employeeBonus))
#output statements here
print("Employee Name:" + employeeName)
print("Employee Bonus: " + employeeBonus)