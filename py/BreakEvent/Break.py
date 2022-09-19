from Base import clean
def BreakEvent(order):
    order = clean(order)
    
    pe = [ x.strip() for x in order.split(",") ]
    
    pe[1] = float(eval(pe[1]))
    pe[2] = float(eval(pe[2]))
    pe[3] = float(eval(pe[3]))

    k = [ (pe[2])/(pe[1]-pe[3]), 
          (pe[2])/(1-(pe[3]/pe[1])) ]
    return k