import numpy as np
from typing import List

class AnomalyDetector:
    def __init__(self, threshold_z: float = 3.0):
        self.threshold = threshold_z

    def detect_volume_anomaly(self, current_count: int, historical_counts: List[int]) -> bool:
        """Uses Z-Score to detect if record volume is statistically impossible."""
        if not historical_counts:
            return False
            
        mean = np.mean(historical_counts)
        std = np.std(historical_counts)
        
        if std == 0: return False
        
        z_score = abs((current_count - mean) / std)
        return z_score > self.threshold
