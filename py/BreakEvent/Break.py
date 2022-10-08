from Base import clean
def BreakEvent(order):
    order = clean(order)
    
    pe = [ x.strip() for x in order.split(",") ]
    for x in range(1, len(pe)):
      pe[x] = float(eval(pe[x]))
    k = [ (pe[2])/(pe[1]-pe[3]), 
          (pe[2])/(1-(pe[3]/pe[1])) ]

    return k