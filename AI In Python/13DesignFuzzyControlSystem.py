import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Define the variables (Inputs and Output)
# Range assumptions:
# Temperature = 0-40°C
# Humidity = 0-100%
# Precipitation = 0-20 mm/hr
# Weather Score = 0-10

temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
precipitation = ctrl.Antecedent(np.arange(0, 21, 1), 'precipitation')
weather = ctrl.Consequent(np.arange(0, 11, 1), 'weather')

# 2. Define Membership Functions

# Temperature: Cold, Good, Hot
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 18])
temperature['good'] = fuzz.trimf(temperature.universe, [15, 22, 30])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 40, 40])

# Humidity: Dry, Good, Wet
humidity['dry'] = fuzz.trimf(humidity.universe, [0, 0, 40])
humidity['good'] = fuzz.trimf(humidity.universe, [30, 55, 80])
humidity['wet'] = fuzz.trimf(humidity.universe, [70, 100, 100])

# Precipitation: No rain, Little rain, Rain
precipitation['no_rain'] = fuzz.trimf(precipitation.universe, [0, 0, 2])
precipitation['little_rain'] = fuzz.trimf(precipitation.universe, [1, 5, 10])
precipitation['rain'] = fuzz.trimf(precipitation.universe, [8, 20, 20])

# Weather: Bad, OK, Perfect
weather['bad'] = fuzz.trimf(weather.universe, [0, 0, 5])
weather['ok'] = fuzz.trimf(weather.universe, [3, 5, 7])
weather['perfect'] = fuzz.trimf(weather.universe, [6, 10, 10])

# 3. Define Rules
rule1 = ctrl.Rule(
    temperature['good'] & humidity['good'] & precipitation['no_rain'],
    weather['perfect']
)

rule2 = ctrl.Rule(
    temperature['hot'] | temperature['cold'] | precipitation['rain'],
    weather['bad']
)

rule3 = ctrl.Rule(
    humidity['wet'] | humidity['dry'],
    weather['ok']
)

rule4 = ctrl.Rule(
    temperature['good'] & precipitation['little_rain'],
    weather['ok']
)

# 4. Build Control System
weather_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
weather_sim = ctrl.ControlSystemSimulation(weather_ctrl)

# 5. Example Input
weather_sim.input['temperature'] = 24
weather_sim.input['humidity'] = 50
weather_sim.input['precipitation'] = 0

weather_sim.compute()

# Output
score = weather_sim.output['weather']

print(f"Weather Condition Score: {score:.2f}")

if score >= 7:
    print("Report: Perfect")
elif score >= 4:
    print("Report: OK")
else:
    print("Report: Bad")