def clean(order):
    order = order.replace(" ", "")
    order = order.replace("%", "")
    order = order.replace("m", "/1000")
    order = order.replace("K", "*1000")
    order = order.replace("M", "*1000000")
    order = order.replace("B", "*1000000000")
    if "=" in order or ":" in order:
        order = order.replace("=", ",")
        order = order.replace(":", "")
        order = order.replace("(", ",")
    else:
        order = order.replace("(", "")
    order = order.replace(")", "")
    return order