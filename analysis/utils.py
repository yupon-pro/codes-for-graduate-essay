from statsmodels.tsa.filters.hp_filter import hpfilter
import pandas as pd
from typing import Literal

def hp_filter_trend(
    target_series: pd.Series,
    time_scale: Literal["yearly", "quarterly", "monthly"] = "yearly",
    with_cycle: bool | None = False
) -> pd.Series | tuple[pd.Series, pd.Series]:
    """
    Apply Hodrick-Prescott (HP) filter to extract the trend component
    from a time-series variable (e.g. productivity, utilization).
    Args:
        target_series (pd.Series): 時系列データ（インデックスは時系列）
        time_scale (str): "yearly", "quarterly", または "monthly"
    Returns:
        pd.Series: トレンド成分（trend component）
    """
    if time_scale == "yearly":
        lamb = 6.25
    elif time_scale == "quarterly":
        lamb = 1600
    elif time_scale == "monthly":
        lamb = 14400
    else:
        raise ValueError("time_scale must be 'yearly', 'quarterly', or 'monthly'.")

    cycle, trend = hpfilter(target_series, lamb=lamb)
    trend.index = target_series.index  # 元の時系列インデックスを保持
    if not with_cycle:
        return trend
    else:
        cycle.index = target_series.index 
        return cycle, trend
    
if __name__ == "__main__":
  pass