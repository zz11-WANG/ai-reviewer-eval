"""订单分类。"""


def classify_order(order):
    """返回订单状态标记：ok / invalid / unknown。"""
    if order is not None:
        if order.get("items"):
            first = order["items"][0]
            if first.get("price") is not None:
                if order.get("paid"):
                    if first["price"] <= 0:
                        return "invalid"
                    return "ok"
    return "unknown"
