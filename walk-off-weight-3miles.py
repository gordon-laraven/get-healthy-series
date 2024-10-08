def calculate_weight_loss(weeks, gender, weight, height, walking_speed):
    # Constants
    MET_VALUES = {
        3.0: 3.8,  # Walking at 3.0 mph
        3.5: 4.0,  # Walking at 3.5 mph
        4.0: 4.3,  # Walking at 4.0 mph
        4.5: 4.5,  # Walking at 4.5 mph
        5.0: 5.0   # Walking at 5.0 mph
    }
    
    # Get the MET value for the given walking speed
    if walking_speed in MET_VALUES:
        met_value = MET_VALUES[walking_speed]
    else:
        print("Walking speed not in range. Please use one of the following speeds: 3.0, 3.5, 4.0, 4.5, 5.0 mph")
        return None

    # Calculate calories burned per minute
    calories_per_minute = (met_value * 3.5 * weight) / 200

    # Calculate total minutes walked in the given time frame
    miles_walked = 3
    hours_per_week = 7  # Assuming walking 7 days a week
    minutes_per_hour = 60
    total_minutes = (miles_walked / walking_speed) * minutes_per_hour * weeks * hours_per_week

    # Calculate total calories burned
    total_calories_burned = calories_per_minute * total_minutes

    # Calculate weight loss in pounds
    weight_loss_pounds = total_calories_burned / 3500  # 3500 calories per pound of fat

    return weight_loss_pounds


# User input
weeks = float(input("Enter the time in weeks: "))
gender = input("Enter gender (M/F): ")
weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))
walking_speed = float(input("Enter walking speed in miles per hour (3.0, 3.5, 4.0, 4.5, 5.0): "))

# Calculate weight loss
weight_loss = calculate_weight_loss(weeks, gender, weight, height, walking_speed)

if weight_loss is not None:
    print(f"Estimated weight loss after {weeks} weeks of walking 3 miles: {weight_loss:.2f} pounds")

