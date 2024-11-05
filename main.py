#!/usr/bin/env python3
# GitHub 06.2: Returning a Rocket Launch

# Task 1. Modify the function countdown()
def countdown(secs):
  msg = None

  if secs == -60:
    msg = "T-60 Seconds"
  elif secs == -30:
    msg = "T-30 Seconds"
  elif secs == -15:
    msg = "T-15 Seconds"
  elif secs in [-10, -9, -8, -7, -6, -5, -3, -2, -1]:
    msg = f"{secs * -1}"
  elif secs == -4:
    msg = "Four stage engine start."
  elif secs == 0:
    msg = "0\nBooster Ignition\nand lift off of Artemis I."
  elif secs == 2:
    msg = "We rise together to the moon and beyond!"

  return msg

def main():
  # Task 2. Manually test by taking input for seconds variable
  seconds = int(input("Enter Seconds to Launch: "))
  

  # Tip, if positive number entered convert to a negative for start of count
  if (seconds > 0):
    seconds = seconds * -1

  t = seconds

  # Task 3. Modify Loop Condition and Call Count Down Function
  while t <= 2:
    message = countdown(t)
    if message is not None:
      print(message)

    t += 1

# DO NOT MODIFY BELOW
if __name__ == "__main__":
  main()