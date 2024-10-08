<<<<<<< Updated upstream

=======
# General Guidelines
# Here are some general recommendations for daily caloric intake:

# Adult Women:

# Sedentary: 1,800 to 2,000 calories
# Active: 2,000 to 2,400 calories
# Adult Men:

# Sedentary: 2,200 to 2,400 calories
# Active: 2,400 to 3,000 calories

import random

def calories_burned(weight, distance_miles):
    # MET value for walking (average)
    met = 3.5  # This is a general estimate for walking at a moderate speed

    # Calories burned formula: (MET * weight in kg) * time in hours
    weight_kg = weight / 2.20462  # Convert weight from pounds to kg
    calories = met * weight_kg * distance_miles
    return calories

def walking_plan(days_walking_per_week, min_distance_miles, max_distance_miles, min_speed_mph, max_speed_mph):
    plan = []
    for day in range(1, days_walking_per_week + 1):
        # Randomize distance and speed for the day
        distance_miles = random.uniform(min_distance_miles, max_distance_miles)
        speed_mph = random.uniform(min_speed_mph, max_speed_mph)
        time_hours = distance_miles / speed_mph
        plan.append(f"Day {day}: Walk {distance_miles:.2f} miles at {speed_mph:.2f} mph "
                    f"for approximately {time_hours * 60:.1f} minutes")
    return plan

def adjust_plan(steps_per_day, plateau_effect):
    # Adjust walking plan based on plateau effect
    adjusted_steps = steps_per_day
    # Instead of just increasing steps, we could add a specific strategy here
    adjusted_steps += int(steps_per_day * plateau_effect)  # Increase steps to combat plateau
    return adjusted_steps

def main():
    # User input
    steps_per_day = int(input("Enter the number of steps taken each day: "))
    weeks = float(input("Enter the time in weeks: "))
    days_walking_per_week = int(input("Enter the number of days per week you will walk: "))
    gender = input("Enter your gender (M/F): ").strip().upper()
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    daily_calories_consumed = float(input("Enter your daily caloric intake: "))

    # User input for distance and speed variation
    min_distance_miles = float(input("Enter the minimum walking distance (in miles): "))
    max_distance_miles = float(input("Enter the maximum walking distance (in miles): "))
    min_speed_mph = float(input("Enter the minimum walking speed (in mph): "))
    max_speed_mph = float(input("Enter the maximum walking speed (in mph): "))

    # Convert steps to miles (2000 steps is approximately 1 mile)
    distance_per_day_miles = steps_per_day / 2000

    # Calculate total distance over the given weeks and days walking
    total_distance_miles = distance_per_day_miles * (weeks * days_walking_per_week)

    # Calculate calories burned based on total distance
    total_calories_burned = calories_burned(weight, total_distance_miles)

    # Total caloric intake over the same period
    total_calories_consumed = daily_calories_consumed * (weeks * 7)

    # Calculate net caloric deficit
    net_caloric_deficit = total_calories_burned - total_calories_consumed

    # Considering 1 pound of weight loss is approximately equal to 3500 calories
    weight_loss = net_caloric_deficit / 3500

    # Apply plateau effect (more nuanced adjustment)
    plateau_effect = 0.10  # 10% increase in activity to combat plateau
    weight_loss_adjusted = weight_loss * (1 - plateau_effect)

    print(f"Estimated weight loss over {weeks} weeks: {weight_loss_adjusted:.2f} pounds")

    # Adjust walking plan based on plateau effect
    adjusted_steps_per_day = adjust_plan(steps_per_day, plateau_effect)
    
    print("\nAdjusted Walking Plan with Distance and Speed Variation:")
    adjusted_plan = walking_plan(days_walking_per_week, min_distance_miles, max_distance_miles, min_speed_mph, max_speed_mph)
    for entry in adjusted_plan:
        print(entry)

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
