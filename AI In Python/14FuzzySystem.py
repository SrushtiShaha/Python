import numpy as np


class ProjectRiskFuzzySystem:
    def __init__(self):
        # Define ranges for inputs and output
        self.universe = np.linspace(0, 100, 101)

    def trimf(self, x, abc):
        """Triangular membership function"""
        a, b, c = abc

        left = 0 if b == a else (x - a) / (b - a)
        right = 0 if c == b else (c - x) / (c - b)

        return max(0, min(left, right))

    def get_memberships(self, funding, staffing):
        # Input 1: Project Funding
        mu_funding = {
            'Inadequate': self.trimf(funding, [0, 0, 45]),
            'Marginal': self.trimf(funding, [30, 50, 70]),
            'Adequate': self.trimf(funding, [55, 100, 100])
        }

        # Input 2: Project Staffing
        mu_staffing = {
            'Small': self.trimf(staffing, [0, 0, 60]),
            'Large': self.trimf(staffing, [40, 100, 100])
        }

        return mu_funding, mu_staffing

    def estimate_risk(self, funding_val, staffing_val):
        mu_f, mu_s = self.get_memberships(funding_val, staffing_val)

        # Rule 1
        rule1 = max(mu_f['Adequate'], mu_s['Small'])

        # Rule 2
        rule2 = min(mu_f['Marginal'], mu_s['Large'])

        # Rule 3
        rule3 = mu_f['Inadequate']

        # Weighted average
        numerator = (rule1 * 20) + (rule2 * 50) + (rule3 * 80)
        denominator = rule1 + rule2 + rule3

        risk_score = numerator / denominator if denominator != 0 else 0

        if risk_score < 40:
            return "Low", risk_score
        elif risk_score < 70:
            return "Normal", risk_score
        else:
            return "High", risk_score


# --- Execution ---
system = ProjectRiskFuzzySystem()

level, score = system.estimate_risk(funding_val=35, staffing_val=60)

print("Project Funding Score: 35 | Staffing Score: 60")
print(f"Estimated Risk: {level} ({score:.2f}%)")