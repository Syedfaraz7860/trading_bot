def validate_side(side):

    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError(
            "Invalid side. Use BUY or SELL"
        )


def validate_order_type(order_type):

    if order_type.upper() not in [
        "MARKET",
        "LIMIT"
    ]:
        raise ValueError(
            "Invalid order type. Use MARKET or LIMIT"
        )