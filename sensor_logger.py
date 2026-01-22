import time
import random
import csv

counter = 0
file = open("sensor_data.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["temperature"])

try:
    while True:
        if counter < 40:
            temperature = random.normalvariate(40, 2)
        else:
            temperature = random.normalvariate(70, 5)

        print("Temperature:", round(temperature, 2), flush=True)
        writer.writerow([temperature])

        counter += 1
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

finally:
    file.close()
    print("Data saved to sensor_data.csv")
