def calories_burned(weight, distance_miles):
    # MET value for walking (average)
    met = 3.5  # This is a general estimate for walking at a moderate speed

    # Calories burned formula: (MET * weight in kg) * time in hours
    weight_kg = weight / 2.20462  # Convert weight from pounds to kg
    calories = met * weight_kg * distance_miles
    return calories

def main():
    # User input
    steps_per_day = int(input("Enter the number of steps taken each day: "))
    weeks = float(input("Enter the time in weeks: "))
    gender = input("Enter your gender (M/F): ").strip().upper()
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    walking_speed = float(input("Enter your walking speed in miles per hour: "))

    # Convert steps to miles (2000 steps is approximately 1 mile)
    distance_per_day_miles = steps_per_day / 2000

    # Calculate total distance over the given weeks
    total_distance_miles = distance_per_day_miles * (weeks * 7)  # 7 days in each week

    # Calculate calories burned based on total distance
    total_calories = calories_burned(weight, total_distance_miles)

    # Considering 1 pound of weight loss is approximately equal to 3500 calories
    weight_loss = total_calories / 3500

    print(f"Estimated weight loss over {weeks} weeks: {weight_loss:.2f} pounds")

if __name__ == "__main__":
    main()