def calculate_median(data):
    sorted_data = sorted(data)
    length = len(sorted_data)
    mid_index = length // 2

    if length % 2 == 0:
        median_value = (sorted_data[mid_index] + sorted_data[mid_index - 1]) / 2
    else:
        median_value = sorted_data[mid_index]

    return median_value

def main():
    
# Example dataset of ages
    age_data = [25, 30, 40, 22, 29, 35, 27, 32, 28, 31, 37]

    # Calculate the median age
    median_age = calculate_median(age_data)

    # Display the result
    print(f"Median Age: {median_age}")
    
if __name__ == "__main__":
    main()
