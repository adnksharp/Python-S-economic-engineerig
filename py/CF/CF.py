from Base import clean

def CashFlow(order):
    order = clean(order)
    
    fin = [ x.strip() for x in order.split(",") ]
    
    if len(fin) == 3:
        fin[1] = float(eval(fin[1]))
        fin[1] = float(fin[1] / 100)
        fin[2] = float(eval(fin[2]))
    else:
        fin[1] = float(eval(fin[1]))
        fin[3] = float(eval(fin[3]))
        fin[3] = float(fin[3] / 100)
        fin[4] = float(eval(fin[4]))
    
    if "F/P" in order:
        if fin[0] == 'F':
            out = fin[1] * ((1 + fin[3]) ** fin[4])
        elif fin[0] == 'F/P':
            out = (1 + fin[1]) ** fin[2]
    elif "P/F" in order:
        if fin[0] == 'P':
            out = fin[1] * (((1 + fin[3]) ** fin[4]) ** -1)
        elif fin[0] == 'P/F':
            out = ((1 + fin[1]) ** (fin[2])) ** -1
    elif "P/A" in order:
        if fin[0] == 'P':
            out = fin[1] * (((1 + fin[3]) ** fin[4]) - 1)/(fin[3] * (1 + fin[3]) ** fin[4])
        elif fin[0] == 'P/A':
            out = (((1+fin[1]) ** fin[2] ) - 1)/(fin[1] * ((1 + fin[1]) ** fin[2]))
    elif "A/P" in order:
        if fin[0] == 'A':
            out = fin[1] * (((((1 + fin[3]) ** fin[4]) - 1)/(fin[3] * (1 + fin[3]) ** fin[4])) ** -1 )
        elif fin[0] == 'A/P':
            out = ((((1+fin[1]) ** fin[2] ) - 1)/(fin[1] * ((1 + fin[1]) ** fin[2]))) ** -1
    elif "F/A" in order:
        if fin[0] == 'F':
            out = fin[1] * (((1 + fin[3]) ** fin[4]) - 1)/(fin[3])
        elif fin[0] == 'F/A':
            out = ((1 + fin[1]) ** fin[2] - 1)/(fin[1])
    else:
        if fin[0] == 'A':
            out = fin[1] * (((((1 + fin[3]) ** fin[4]) - 1)/(fin[3])) ** -1)
        else:
            out = (((1 + fin[1]) ** fin[2] - 1)/(fin[1])) ** -1
    return out;