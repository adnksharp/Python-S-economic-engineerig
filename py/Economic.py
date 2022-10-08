from Messages import *
from CF.CF import CashFlow
from GAG.GAG import Gradient    
from BreakEvent.Break import BreakEvent

lg = "en"
order = "."
while order != "exit" and order != "-q":
    order = input(">_ ")
    if "F/P" in order or "P/F" in order or "P/A" in order or "A/P" in order or "F/A" in order or "A/F" in order:
        OutCF(order, CashFlow(order))
    elif "A_n" in order or "A/G" in order or "P/G" in order or "F/G" in order or "F/g" in order or "P/g" in order:
        OutCF(order, Gradient(order))
    elif "Sum" in order:
        OutSG(order, Gradient(order))
    elif "BE" in order or "PE" in order:
        OutPE(order, BreakEvent(order))
    elif "lang" in order or "-l" in order:
        lg = Language()
    elif "clear" in order or "-c" in order:
        Clear()
    elif "help" in order or "-h" in order:
        Help(lg, 200)
    elif "exit" in order or "-q" in order:
        break
    else:
        Help(lg, 404)
