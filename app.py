import sys
import time

# Modules
from CalculateBinaryNumbers import calculateBinaryNumbers

# Main-Function
if __name__ == "__main__":
    while True:
        # Input for the 8-Bit
        binaryNumber = input("Write 8-Bit (1 Bit = 0 or 1): ")

        # Time management for the progress which will be saved
        currentTime = time.localtime()

        day = currentTime.tm_mday
        month = currentTime.tm_mon
        year = currentTime.tm_year

        # When the day or / and the month is lower than 10, it begins with a "0". For example: 01, 02, 03
        if day < 10:
            day = f"0{day}"

        if month < 10:
            month = f"0{month}"

        hour = currentTime.tm_hour
        minute = currentTime.tm_min

        # Here I do the same with the hour and the minute.
        if hour < 10:
            hour = f"0{hour}"

        if minute < 10:
            minute = f"0{minute}"

        if binaryNumber == "$exit":
            sys.exit()

        # Call calculateBinaryNumbers-function to get the solution of the binary number
        output = calculateBinaryNumbers(binaryNumber)

        # When the binary number is none, you´ll see the text: "Invalid input"
        if output is None:
            print("Invalid input")

        # Write progress only if the binary number is valid (is not none)
        if output is not None:
            print(output)
            with open("./progress.txt", "a") as file:
                file.write(
                    f"[{day}.{month}.{year} / {hour}:{minute}]   {binaryNumber} = {output}\n")
