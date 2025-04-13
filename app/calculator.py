def is_arbitrage(odds_a: float, odds_b: float) -> bool:
    """
    Determines if there's an arbitrage opportunity between two odds.
    
    Args:
        odds_a: Decimal odds for outcome A
        odds_b: Decimal odds for outcome B
        
    Returns:
        bool: True if arbitrage exists, False otherwise
    """
    return (1 / odds_a + 1 / odds_b) < 1

def calculate_stakes(odds_a: float, odds_b: float, bankroll: float) -> dict:
    """
    Calculates optimal stake distribution for an arbitrage opportunity.
    
    Args:
        odds_a: Decimal odds for outcome A
        odds_b: Decimal odds for outcome B
        bankroll: Total amount to stake
        
    Returns:
        dict: Contains stake amounts, returns, profit, and ROI
    """
    # Calculate optimal stakes
    stake_a = (odds_b * bankroll) / (odds_a + odds_b)
    stake_b = bankroll - stake_a
    
    # Calculate returns
    return_a = stake_a * odds_a
    return_b = stake_b * odds_b
    
    # Calculate profit and ROI
    guaranteed_return = min(return_a, return_b)
    profit = guaranteed_return - bankroll
    roi = (profit / bankroll) * 100
    
    return {
        "stake_a": round(stake_a, 2),
        "stake_b": round(stake_b, 2),
        "return_a": round(return_a, 2),
        "return_b": round(return_b, 2),
        "guaranteed_return": round(guaranteed_return, 2),
        "profit": round(profit, 2),
        "roi": round(roi, 2)
    }
