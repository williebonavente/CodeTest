import pandas as pd

def calculate_median(data):
    median_value = data.median()
    return median_value

def main():
    # Read patient ages from a CSV file
    ages_data = pd.read_csv('patient_ages.csv')
    median_age = calculate_median(ages_data['age'])
    print(f"Median Age: {median_age}")

    # Read blood pressure readings from a CSV file
    bp_data = pd.read_csv('blood_pressure_readings.csv')
    median_systolic = calculate_median(bp_data['systolic'])
    median_diastolic = calculate_median(bp_data['diastolic'])
    print(f"Median Systolic BP: {median_systolic}")
    print(f"Median Diastolic BP: {median_diastolic}")

    # Read cholesterol levels from a CSV file
    cholesterol_data = pd.read_csv('cholesterol_levels.csv')
    median_total_cholesterol = calculate_median(cholesterol_data['total_cholesterol'])
    print(f"Median Total Cholesterol: {median_total_cholesterol}")

if __name__ == "__main__":
    main()
