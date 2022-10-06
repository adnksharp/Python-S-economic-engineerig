from Base import clean

def Gradient (order):
    if 'A_n' in order:
        form = False
        if '%' in order:
            G = False
        else:
            G = True
    else:
        form = True

    order = clean(order)
    Input = [x.strip() for x in order.split(',')]

    if form:
        if 'Sum' in order:
            l = len(Input)
            i = float(eval(Input[1]))
            i = float(i / 100)
            P = 0
            F = 0
            n = 0
            for k in range(2, l):
                if k % 2 == 0:
                    n = float(eval(Input[k])) 
                else:
                    P += (float(eval(Input[k])) / (1 + i) ** n)
                    F += (float(eval(Input[k])) * (1 + i) ** (n - 1))
            out = [P, F]
        else:
            g = float(eval(Input[1]))
            i = float(eval(Input[3]))
            i = float(i / 100)
            n = float(eval(Input[4]))
            A_1 = float(eval(Input[5]))

            if 'A/G' in order:
                out = g * ((1 / i ) - ( n / ((1 + i) ** n - 1))) + A_1
            elif 'P/G' in order:
                out = (g / i) * ((((1 + i) ** n - 1) / i) - n) * (1 / ((1  + i) ** n))
                out += (A_1 * (((1 + i) ** n - 1) / (i * (1  + i) ** n)))
            elif 'F/G' in order:
                out = (g / i) * ((((1  + i) ** n - 1) / i) - n)
                out += (A_1 * (((1 + i) ** n - 1) /i))
            elif i != float(g / 100):
                g = float(g / 100)
                if 'F/g' in order:
                    out = A_1 * ((((1 + g) ** n) - ((1 + i) ** n)) / (g - i))
                elif 'P/g' in order:
                    out = (A_1 * (1 - (((1 + g) / (1 + i)) ** n))) / (i - g)
            else:
                if 'F/g' in order:
                    out = A_1 * n * ((1 + i) ** (n - 1))
                else:
                    out = A_1 * (n / (1 + i)) 
    else:
        out = []
        n = int(eval(Input[1]))
        g = float(eval(Input[2]))
        A_1 = float(eval(Input[3]))
        if G == False:
            g /= 100
            for i in range (1, n + 1):
                out.append ( (A_1 * (1 + g) ** (i - 1)) )
        else:
            for i in range(1, n + 1):
                out.append( (A_1 + (i - 1 ) * g) )
    return out
