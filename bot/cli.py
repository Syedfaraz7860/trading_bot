import argparse

from client import get_client
from orders import place_order
from validators import (
    validate_side,
    validate_order_type
)
from logging_config import (
    setup_logger
)

setup_logger()

parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True
)

parser.add_argument(
    "--side",
    required=True
)

parser.add_argument(
    "--type",
    required=True
)

parser.add_argument(
    "--quantity",
    type=float,
    required=True
)

parser.add_argument(
    "--price",
    type=float
)

args = parser.parse_args()

try:

    validate_side(args.side)

    validate_order_type(
        args.type
    )

    client = get_client()

    response = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nORDER SUCCESS\n")

    print(
        f"Order ID : "
        f"{response.get('orderId')}"
    )

    print(
        f"Status : "
        f"{response.get('status')}"
    )

    print(
        f"Executed Qty : "
        f"{response.get('executedQty')}"
    )

except Exception as e:

    print(
        f"\nORDER FAILED\n{e}"
    )