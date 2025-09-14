import time  # Import the time module to use sleep for delays

# Loop from 5 down to 1 for the countdown
for i in range(5, 0, -1):
    print(f"Countdown: {i}\r", end="")  # Print the countdown number on the same line
    time.sleep(1)  # Wait for 1 second before the next number

print("Blast off! 🚀")  # Print the final message after the countdown