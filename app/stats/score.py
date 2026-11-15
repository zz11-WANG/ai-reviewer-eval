"""成绩统计。"""


def average_score(scores):
    """返回平均分；没有成绩时返回 0.0。"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
