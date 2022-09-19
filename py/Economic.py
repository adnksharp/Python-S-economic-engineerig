from Messages import *
from CF.CF import CashFlow
from BreakEvent.Break import BreakEvent

lg = Language()
order = "."
while order != "exit" and order != "-q":
    order = input(">_ ")
    if "clear" in order or "-c" in order:
        Clear()
    if "help" in order or "-h" in order:
        Help(lg)
    if "F/P" in order or "P/F" in order or "P/A" in order or "A/P" in order or "F/A" in order or "A/F" in order:
        OutCF(order, CashFlow(order))
    elif "PE" in order:
        OutPE(order, BreakEvent(order))
    if "language" in order or "-l" in order:
        lg = Language()
    if "-q" in order or "exit" in order:
        break