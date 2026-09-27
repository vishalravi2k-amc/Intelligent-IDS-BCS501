"""
Markov Chain Network State Anomaly Detector
Models sequential state transitions for multi-stage cyber attack detection.
"""

from typing import Dict, List
import numpy as np


class NetworkMarkovModel:

    def __init__(self):
        self.states = [0, 1, 2]  # Safe, Suspicious, Critical
        self.transition_matrix = np.array(
            [
                [0.85, 0.12, 0.03],
                [0.20, 0.50, 0.30],
                [0.05, 0.15, 0.80],
            ]
        )

    def calculate_sequence_probability(
        self, state_sequence: List[int]
    ) -> float:
        prob = 1.0
        for i in range(len(state_sequence) - 1):
            curr_state = state_sequence[i]
            next_state = state_sequence[i + 1]
            prob *= self.transition_matrix[curr_state][next_state]
        return prob

    def evaluate_threat_chain(self, sequence: List[int]) -> Dict[str, float]:
        likelihood = self.calculate_sequence_probability(sequence)
        is_anomalous = likelihood < 0.05
        return {
            "sequence_likelihood": float(likelihood),
            "is_sequence_anomaly": is_anomalous,
        }
