from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime


def get_score_trend(user_rounds: list) -> dict:
    """
    Calculate score trend from historical rounds.
    Returns: average score, trend direction, improvement rate
    """
    # TODO: Extract scores and dates
    # TODO: Calculate trend
    # TODO: Return results
    
    if not user_rounds:
        return {"error": "no rounds found"}
    
    scores = [r.score for r in user_rounds]
    dates = [r.date for r in user_rounds]

    worst_score = max(scores)
    best_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 1)

    trend = "improving" if scores[-1] < scores[0] else "declining"

    return {
        "average_score": round(avg_score, 1),
        "best_score": best_score,
        "worst_score": worst_score,
        "trend": trend,
        "rounds_played": len(scores)
    }
    
def calculate_handicap(rounds):
    """
    Calculate a WHS Handicap Index from a player's scoring record.

    `rounds`: list ordered oldest -> newest, each item having:
        - score:         adjusted gross score for the round
        - course_rating: e.g. 72.4
        - slope_rating:  e.g. 131

    Returns the Handicap Index rounded to one decimal,
    or None if there aren't enough rounds.
    """
    if len(rounds) < 3:
        return None  # WHS needs at least 3 rounds (54 holes) to establish

    # 1. Score differential per round: (113 / slope) * (score - rating)
    #    113 = slope of a course of standard difficulty.
    #    PCC (playing-conditions adjustment) is treated as 0 here.
    differentials = [
        (113 / r["slope_rating"]) * (r["score"] - r["course_rating"])
        for r in rounds
    ]

    # 2. WHS only looks at the most recent 20 rounds, lowest first.
    recent = sorted(differentials[-20:])

    # 3. Selection table: (how many lowest to average, adjustment).
    table = {
        3: (1, -2.0), 4: (1, -1.0), 5: (1, 0.0),
        6: (2, -1.0), 7: (2, 0.0),  8: (2, 0.0),
        9: (3, 0.0),  10: (3, 0.0), 11: (3, 0.0),
        12: (4, 0.0), 13: (4, 0.0), 14: (4, 0.0),
        15: (5, 0.0), 16: (5, 0.0),
        17: (6, 0.0), 18: (6, 0.0),
        19: (7, 0.0), 20: (8, 0.0),
    }
    count, adjustment = table[len(recent)]

    # 4. Average the lowest `count` differentials, apply the adjustment.
    index = sum(recent[:count]) / count + adjustment

    # 5. Round to nearest tenth, cap at the WHS maximum of 54.0.
    return min(round(index, 1), 54.0)