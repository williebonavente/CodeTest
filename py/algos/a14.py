import time

def read_temperature_sensor():
    # Simulate reading the temperature sensor
    # In a real system, this would involve interacting with an actual temperature sensor
    return 25.0  # Simulated temperature value in Celsius

def control_fan(temperature):
    # Simulate controlling the fan based on the temperature reading
    if temperature > 30.0:
        print("Temperature is too high. Turning on the fan.")
        # In a real system, this would involve activating the fan using GPIO or other hardware interfaces
    else:
        print("Temperature is normal. Fan is turned off.")
        # In a real system, this would involve deactivating the fan using GPIO or other hardware interfaces

def main():
    while True:
        # Read temperature from the sensor
        temperature = read_temperature_sensor()

        # Control the fan based on the temperature reading
        control_fan(temperature)

        # Wait for a few seconds before taking the next temperature reading
        time.sleep(5)

if __name__ == "__main__":
    main()
