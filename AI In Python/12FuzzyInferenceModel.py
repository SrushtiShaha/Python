import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Define Antecedents (Inputs) and Consequents (Output)
# Service and Food are rated 0-10; Tip is 0-25%

service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# 2. Define Membership Functions (Fuzzy Sets)

# Service: Poor, Good, Excellent
service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['good'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])

# Food: Rancid, Delicious
food['rancid'] = fuzz.trimf(food.universe, [0, 0, 10])
food['delicious'] = fuzz.trimf(food.universe, [0, 10, 10])

# Tip: Cheap, Average, Generous
tip['cheap'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['average'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['generous'] = fuzz.trimf(tip.universe, [13, 25, 25])

# 3. Define Rules

# Rule 1: If service is poor OR food is rancid, then tip is cheap
rule1 = ctrl.Rule(service['poor'] | food['rancid'], tip['cheap'])

# Rule 2: If service is good, then tip is average
rule2 = ctrl.Rule(service['good'], tip['average'])

# Rule 3: If service is excellent OR food is delicious, then tip is generous
rule3 = ctrl.Rule(service['excellent'] | food['delicious'], tip['generous'])

# 4. Create and Simulate Control System
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# 5. Example Calculation
tipping.input['service'] = 9.8
tipping.input['food'] = 6.5

tipping.compute()

print(f"Service Score: 9.8, Food Score: 6.5")
print(f"Suggested Tip: {tipping.output['tip']:.2f}%")