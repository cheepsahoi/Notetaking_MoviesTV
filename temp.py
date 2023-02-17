import time

# Ask the user if they want to start the timer at a specific time or an interval
start_option = input("Do you want to start the timer at a specific time (s) or an interval (i)? ")

if start_option.lower() == "s":
    # If the user wants to start the timer at a specific time, ask them for the time in seconds
    start_time_input = input("Enter the start time in HH:MM:SS format: ")
    try:
        # Attempt to parse the user's input as a time object in seconds
        start_time = time.mktime(time.strptime(start_time_input, "%H:%M:%S"))
        stopwatch_start = time.time() - start_time
    except ValueError:
        # If the user's input is not in the correct format, start the timer at 0 seconds
        print("Invalid format. Starting timer at 0 seconds.")
        stopwatch_start = time.time()
elif start_option.lower() == "i":
    # If the user wants to start the timer at an interval, ask them for the interval in seconds
    interval = float(input("Enter the interval in seconds: "))
    stopwatch_start = time.time() - interval
else:
    # If the user enters an invalid option, start the timer at 0 seconds
    print("Invalid option. Starting timer at 0 seconds.")
    stopwatch_start = time.time()

notes = []  # Initialize an empty list for notes

while True:
    # Display the current stopwatch time in the HH:MM:SS format
    stopwatch_current = time.time() - stopwatch_start
    stopwatch_struct_time = time.gmtime(stopwatch_current)
    stopwatch_formatted = time.strftime("%H:%M:%S", stopwatch_struct_time)
    print("Stopwatch: {}".format(stopwatch_formatted))
    
    # Ask the user if they want to add a note, adjust the start time, or continue the stopwatch
    user_input = input("Press 'n' to add a note, 's' to adjust the start time, 'q' to quit, or any other key to continue: ")
    
    # Handle the user's input
    if user_input.lower() == 'n':
        # If the user wants to add a note, ask them for the note text and append it to the notes list along with the current stopwatch time
        note_text = input("Enter note text: ")
        notes.append((stopwatch_formatted, note_text))
    elif user_input.lower() == 's':
        # If the user wants to adjust the start time, ask them for the new start time
        new_start_time_input = input("Enter the new start time in HH:MM:SS format: ")
        try:
            # Attempt to parse the user's input as a time object in seconds
            new_start_time = time.mktime(time.strptime(new_start_time_input, "%H:%M:%S"))
            stopwatch_start = time.time() - new_start_time
        except ValueError:
            # If the user's input is not in the correct format, keep the current start time
            print("Invalid format. Start time not changed.")
    elif user_input.lower() == 'q':
        # If the user wants to quit, break out of the loop
        break
    else:
        # Otherwise, continue the stopwatch by waiting for a short amount of time (0.1
        time.sleep(0.1)

# Print out the notes and the stopwatch times when each note was taken
print("Notes:")
for note in notes:
    print("{} - {}".format(note[0], note[1]))
