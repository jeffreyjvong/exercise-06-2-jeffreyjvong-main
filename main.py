#!/usr/bin/env python3
# GitHub 06.2: Returning a Rocket Launch

# Task 1. Modify the function countdown()
def countdown(secs):
  msg = secs

  if msg == -60:
    return "T-60 Seconds"
  elif msg == -30:
    return "T-30 Seconds"
  elif msg == -15:
    return "T-15 Seconds"
  elif msg in [-10, -9, -8, -7, -6, -5, -3, -2, -1]:
    return f"{msg * -1}"
  elif msg == -4:
    return "Four stage engine start."
  elif msg == 0:
    return "0\nBooster Ignition"
  elif msg == 1:
    return "and lift off of Artemis I."
  elif msg == 2:
    return "We rise together to the moon and beyond!"
  else:
    return None


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