import numpy as np


def trimf(x, abc):
    """Triangular membership function"""
    a, b, c = abc

    if x <= a or x >= c:
        return 0
    if a < x <= b:
        return (x - a) / (b - a)
    if b < x < c:
        return (c - x) / (c - b)

    return 0


def calculate_fan_speed(temp_val, hum_val):

    # 1. Fuzzification
    mu_temp = {
        'Cool': trimf(temp_val, [-10, 10, 25]),
        'Warm': trimf(temp_val, [15, 25, 35]),
        'Hot': trimf(temp_val, [25, 40, 55])
    }

    mu_hum = {
        'Low': trimf(hum_val, [-20, 20, 50]),
        'Medium': trimf(hum_val, [30, 50, 70]),
        'High': trimf(hum_val, [50, 80, 120])
    }

    # 2. Rule Evaluation
    r1 = mu_temp['Cool']                        # High
    r2 = min(mu_temp['Warm'], mu_hum['High'])  # Low
    r3 = mu_temp['Hot']                        # No
    r4 = min(mu_temp['Warm'], mu_hum['Low'])   # Medium

    # 3. Defuzzification
    numerator = (r3 * 0) + (r2 * 30) + (r4 * 60) + (r1 * 90)
    denominator = r1 + r2 + r3 + r4

    if denominator == 0:
        return 0, "No"

    crisp_speed = numerator / denominator

    # Labeling
    if crisp_speed < 15:
        label = "No"
    elif crisp_speed < 45:
        label = "Low"
    elif crisp_speed < 75:
        label = "Medium"
    else:
        label = "High"

    return crisp_speed, label


# --- Test Case ---
temperature = 18
humidity = 25

speed, level = calculate_fan_speed(temperature, humidity)

print(f"Room Stats: Temp {temperature}°C, Humidity {humidity}%")
print(f"Heater Fan Action: {level} Speed ({speed:.2f}%)")