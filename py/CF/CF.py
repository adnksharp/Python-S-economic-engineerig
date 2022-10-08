from Base import clean

def CashFlow(order):
    if order[0] == '(':
        v = True
    else:
        v = False
    order = clean(order)

    FI = [x.strip() for x in order.split(',')]

    if v:
        i = float(eval(FI[1]))
        n = float(eval(FI[2]))
        c = 1
    else:
        i = float(eval(FI[3]))
        n = float(eval(FI[4]))
        c = float(eval(FI[1]))
    i = float(i / 100)
    
    if 'F/P' in order or 'P/F' in order:
        out = (1 + i) ** n
    elif 'P/A' in order or 'A/P' in order:
        out = ((1 + i) ** n - 1) / (i * (1 + i) ** n)
    elif 'F/A' in order or 'A/F' in order:
        out = ((1 + i) ** n - 1) / i
        
    if 'P/F' in order or 'A/P' in order or 'A/F' in order:
            out = 1 / out
    if not v:
        out *= c

    return out
