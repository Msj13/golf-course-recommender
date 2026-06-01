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
    

def predict_next_score(user_rounds: list) -> dict:
    """
    Use ML to predict next round score.
    Returns: predicted score, confidence interval
    """
    # TODO: Train linear regression model
    # TODO: Make prediction
    # TODO: Return with confidence
    pass