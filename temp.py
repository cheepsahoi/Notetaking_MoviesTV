import time

# Ask the user if they want to start the timer at a specific time or an interval
start_option = input("Do you want to start the timer at a specific time (s) or an interval (i)? ")

if start_option.lower() == "s":
    # If the user wants to start the timer at a specific time, ask them for the time in seconds
    while True:
        start_time_input = input("Enter the start time in HH:MM:SS format: ")
        try:
            # Attempt to parse the user's input as a time object in seconds
            start_time = time.mktime(time.strptime(start_time_input, "%H:%M:%S"))
            stopwatch_start = time.time() - start_time
            break  # Exit the loop if the input is valid
        except ValueError:
            # If the user's input is not in the correct format, give them a chance to retry
            retry_input = input("Invalid format. Do you want to retry (y/n)? ")
            if retry_input.lower() != 'y':
                # If the user doesn't want to retry, start the timer at 0 seconds
                print("Starting timer at 0 seconds.")
                stopwatch_start = time.time()
                break  # Exit the loop
    # End of loop
elif start_option.lower() == "i":
    # If the user wants to start the timer at an interval, ask them for the interval in seconds
    interval = float(input("Enter the interval in seconds: "))
    stopwatch_start = time.time() - interval
else:
    # If the user enters an invalid option, start the timer at 0 seconds
    print("Invalid option. Starting timer at 0 seconds.")
    stopwatch_start = time.time()
# Chunk 2
start_option = input("Do you want to start the timer at a specific time (s) or an interval (i)? ")

if start_option.lower() == "s":
    # If the user wants to start the timer at a specific time, ask them for the time in seconds
    while True:
        start_time_input = input("Enter the start time in HH:MM:SS format: ")
        try:
            # Attempt to parse the user's input as a time object in seconds
            start_time = time.mktime(time.strptime(start_time_input, "%H:%M:%S"))
            stopwatch_start = time.time() - start_time
            break  # Exit the loop if the input is valid
        except ValueError:
            # If the user's input is not in the correct format, give them a chance to retry
            retry_input = input("Invalid format. Do you want to retry (y/n)? ")
            if retry_input.lower() != 'y':
                # If the user doesn't want to retry, start the timer at 0 seconds
                print("Starting timer at 0 seconds.")
                stopwatch_start = time.time()
                break  # Exit the loop
    # End of loop
elif start_option.lower() == "i":
    # If the user wants to start the timer at an interval, ask them for the interval in seconds
    interval = float(input("Enter the interval in seconds: "))
    stopwatch_start = time.time() - interval
else:
    # If the user enters an invalid option, start the timer at 0 seconds
    print("Invalid option. Starting timer at 0 seconds.")
    stopwatch_start = time.time()

notes = []  # Initialize an empty list for notes
# Chunk 3
