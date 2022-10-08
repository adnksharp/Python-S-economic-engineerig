def clean(order):
    rep = [ " ", "$", "%", ":", ")" ]
    if "Sum" not in order:
        order = order.replace("m", "/1000")
    if "BE" not in order:
        order = order.replace("B", "MM")
    order = order.replace("M", "KK")
    order = order.replace("K", "*1000")
    if "=" in order or ":" in order:
        order = order.replace("=", ",")
        order = order.replace("(", ",")
    else:
        order = order.replace("(", "")
    for x in rep:
        order = order.replace(x, "")
    return order 
