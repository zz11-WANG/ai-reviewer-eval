"""订单分类。"""


def classify_order(order):
    """返回订单状态标记：ok / invalid / unknown。"""
    if order is None:
        return "unknown"
    items = order.get("items") or []
    if not items:
        return "unknown"
    first = items[0]
    if first.get("price") is None:
        return "unknown"
    if not order.get("paid"):
        return "unknown"
    if first["price"] <= 0:
        return "invalid"
    return "ok"
