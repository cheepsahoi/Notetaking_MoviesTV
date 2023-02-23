import time
import tkinter as tk

class StopwatchGUI:
    def __init__(self, master):
        self.master = master
        master.title("Film Notetaking")
        
        # Create the widgets for the GUI
        self.note_label = tk.Label(master, text="Notes:", font=("Arial", 18))
        self.note_label.pack(pady=10)
        self.note_text = tk.Text(master, height=10, width=50)
        self.note_text.pack(pady=10)
        self.copy_button = tk.Button(master, text="Copy Notes to Clipboard", command=self.copy_notes)
        self.copy_button.pack(pady=10)
        self.stopwatch_label = tk.Label(master, text="Stopwatch: 00:00:00", font=("Arial", 24))
        self.stopwatch_label.pack(pady=10)
        self.time_label = tk.Label(master, text="Set Time: (HH:MM:SS)", font=("Arial", 18))
        self.time_label.pack(pady=10)
        self.time_entry = tk.Entry(master, width=8)
        self.time_entry.pack(pady=10)
        self.time_button = tk.Button(master, text="Set Time", command=self.set_time)
        self.time_button.pack(pady=10)
        self.note_text.config(state="disabled")
        self.note_label = tk.Label(master, text="Enter Notes below then press 'enter'", font=("Arial", 12))
        self.note_label.pack(pady=10)
        self.note_entry = tk.Entry(master, width=50)
        self.note_entry.pack(pady=10)
        self.note_entry.bind('<Return>', self.add_note)
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_stopwatch)
        self.pause_button.pack(pady=10)
        self.start_stopwatch()
    
    def start_stopwatch(self):
        self.stopwatch_start = time.time()
        self.pause_start = None
        self.current_time = self.stopwatch_start
        self.notes = []
        self.update_stopwatch_label()
    
    def update_stopwatch_label(self):
        if self.pause_start:
            stopwatch_current = self.pause_start - self.stopwatch_start
        else:
            stopwatch_current = time.time() - self.stopwatch_start
        stopwatch_struct_time = time.gmtime(stopwatch_current)
        stopwatch_formatted = time.strftime("%H:%M:%S", stopwatch_struct_time)
        self.stopwatch_label.config(text="Stopwatch: " + stopwatch_formatted)
        self.master.after(100, self.update_stopwatch_label)
    
    def set_time(self):
        time_str = self.time_entry.get()
        try:
            time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], time_str.split(":")))
        except ValueError:
            self.time_entry.delete(0, tk.END)
            return
        if self.pause_start:  # Check if stopwatch was paused
            self.stopwatch_start = self.pause_start - time_seconds
        else:
            self.stopwatch_start = time.time() - time_seconds
        self.current_time = self.stopwatch_start

    def copy_notes(self):
        sorted_notes = sorted(self.notes, key=lambda note: note[0])
        notes_str = ""
        for note in sorted_notes:
            notes_str += note[0] + " - " + note[1] + "\n"
        self.master.clipboard_clear()
        self.master.clipboard_append(notes_str)


    def add_note(self, event=None):
        if self.pause_start:
            note_time = self.pause_start - self.stopwatch_start
        else:
            note_time = time.time() - self.stopwatch_start
        note_struct_time = time.gmtime(note_time)
        note_formatted = time.strftime("%H:%M:%S", note_struct_time)
        note_text = self.note_entry.get()
        self.notes.append((note_formatted, note_text))
        self.note_entry.delete(0, tk.END)
        self.update_note_text()
    
    def update_note_text(self):
        self.note_text.config(state="normal")
        self.note_text.delete("1.0", tk.END)
        for note in reversed(self.notes):
            self.note_text.insert(tk.END, note[0] + " - " + note[1] + "\n")
        self.note_text.config(state="disabled")

    
    def pause_stopwatch(self):
        if self.pause_start:
            self.stopwatch_start += time.time() - self.pause_start
            self.pause_start = None
            self.pause_button.config(text="Pause")
        else:
            self.pause_start = time.time()
            self.pause_button.config(text="Resume")

root = tk.Tk()
gui = StopwatchGUI(root)
root.mainloop()
