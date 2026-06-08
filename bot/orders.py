import logging

def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity
    }

    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValueError(
                "Price required for LIMIT order"
            )

        params["price"] = price
        params["timeInForce"] = "GTC"

    try:
        logging.info(f"Order Request: {params}")

        response = client.create_order(**params)

        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logging.error(str(e))
        raise