# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:00:00 2026

@author: mbalab
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
# 1. Define Fuzzy Variables
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')
# 2. Sub-partition (Membership Functions)
service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['good'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])
food['rancid'] = fuzz.trimf(food.universe, [0, 0, 5])
food['delicious'] = fuzz.trimf(food.universe, [5, 10, 10])
tip['cheap'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['average'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['generous'] = fuzz.trimf(tip.universe, [13, 25, 25])
# 3. Set Up Rules
rule1 = ctrl.Rule(service['poor'] | food['rancid'], tip['cheap'])
rule2 = ctrl.Rule(service['good'], tip['average'])
rule3 = ctrl.Rule(service['excellent'] | food['delicious'], tip['generous'])
# 4. Control System Creation
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
# 5. Assign Values
tipping.input['service'] = 9.8
tipping.input['food'] = 6.5
# 6. Compute Result
tipping.compute()
# 7. Print Results and Plot
print(f"Tip amount: {tipping.output['tip']:.2f}%")
# Plotting
service.view()
food.view()
tip.view(sim=tipping)
plt.show()
