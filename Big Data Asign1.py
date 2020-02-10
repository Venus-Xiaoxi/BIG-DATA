

rate = float(input('input rate in decimal format:'))
cashflow = input('Please enter a list of cashflow for years in sequences : ').split(sep=',')
cashflows = list(map(int, cashflow))
print(cashflows)

NPV = []
for x in cashflows:
    for y in range(1, len(cashflows)+1):
        npv = (x / ((1 + rate) ** y))
        print((1 + rate) ** y)
        print(npv)
        NPV.append(npv)
        break
    print(NPV)
    print(round(sum(NPV),2))
