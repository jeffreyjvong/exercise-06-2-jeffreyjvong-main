def countdown(t):
    positive_t = abs(t)
    
    if positive_t == 0:
        return "Liftoff!"
    elif positive_t == 5:
        return "T-Minus 5 seconds. Get ready!"
    elif positive_t == 10:
        return "T-Minus 10 seconds. Prepare for launch!"
    elif positive_t == 15:
        return "T-Minus 15 seconds."
    elif positive_t == 30:
        return "T-Minus 30 seconds."
    elif positive_t == 60:
        return "T-Minus 60 seconds."
    elif 1 <= positive_t <= 4:
        return f"T-Minus {positive_t} seconds. Ignition!"
    else:
        return None

def main():
    # Start input from T-Minus 80 seconds to T-Minus 15 seconds
    t = -80  # Starting point for countdown

    # Modify the while loop to conditionally run
    while t <= 10:
        message = countdown(t)
        if message is not None:
            print(message)
        # Increment t to continue the countdown
        t += 1

if __name__ == "__main__":
    main()