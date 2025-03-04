import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyautogui
import time


# Function to automate typing
def auto_typer():
    try:
        time.sleep(delay_start)  # Initial delay before starting
        for _ in range(repeat_count):
            pyautogui.typewrite(user_text, interval=0.05)  # Increased speed of typing
            pyautogui.press("enter")
            time.sleep(interval)  # Adding delay between repetitions
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        exit_program()


# Exit the program
def exit_program():
    root.quit()


# First window: Enter text
def show_text_window():
    global user_text
    user_text = text_input.get("1.0", tk.END).strip()
    if not user_text:
        messagebox.showerror("Error", "Please enter some text!")
        return
    text_window.withdraw()  # Hide current window
    show_repeat_window()


# Second window: Enter repeat count
def show_repeat_window():
    global repeat_window
    repeat_window = tk.Toplevel(root)
    repeat_window.title("Auto Typer - Repeat Count")
    repeat_window.geometry("650x400")
    repeat_window.configure(bg="#EAEAEA")

    ttk.Label(repeat_window, text="How many times to repeat the text?", font=("Helvetica", 12, "bold"), background="#EAEAEA").pack(pady=10)
    global repeat_input
    repeat_input = ttk.Entry(repeat_window, width=15, font=("Helvetica", 12))
    repeat_input.pack(pady=10)

    ttk.Button(repeat_window, text="Back", command=back_to_text_window, width=15).pack(pady=5)
    ttk.Button(repeat_window, text="Next", command=show_interval_window, width=15).pack(pady=10)
    ttk.Button(repeat_window, text="Exit", command=exit_program, width=15).pack(pady=5)


# Third window: Enter interval
def show_interval_window():
    global repeat_count
    try:
        repeat_count = int(repeat_input.get().strip())
        if repeat_count <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number for repeat count!")
        return

    repeat_window.withdraw()  # Hide current window

    global interval_window
    interval_window = tk.Toplevel(root)
    interval_window.title("Auto Typer - Interval")
    interval_window.geometry("650x400")
    interval_window.configure(bg="#EAEAEA")

    ttk.Label(interval_window, text="Enter interval (in seconds):", font=("Helvetica", 12, "bold"), background="#EAEAEA").pack(pady=10)
    global interval_input
    interval_input = ttk.Entry(interval_window, width=15, font=("Helvetica", 12))
    interval_input.pack(pady=10)

    ttk.Button(interval_window, text="Back", command=back_to_repeat_window, width=15).pack(pady=5)
    ttk.Button(interval_window, text="Next", command=show_delay_window, width=15).pack(pady=10)
    ttk.Button(interval_window, text="Exit", command=exit_program, width=15).pack(pady=5)


# Fourth window: Enter start delay
def show_delay_window():
    global interval
    try:
        interval = float(interval_input.get().strip())
        if interval < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid non-negative number for interval!")
        return

    interval_window.withdraw()  # Hide current window

    global delay_window
    delay_window = tk.Toplevel(root)
    delay_window.title("Auto Typer - Start Delay")
    delay_window.geometry("650x400")
    delay_window.configure(bg="#EAEAEA")

    ttk.Label(delay_window, text="Enter delay before starting (in seconds):", font=("Helvetica", 12, "bold"), background="#EAEAEA").pack(pady=10)
    global delay_input
    delay_input = ttk.Entry(delay_window, width=15, font=("Helvetica", 12))
    delay_input.pack(pady=10)

    ttk.Button(delay_window, text="Back", command=back_to_interval_window, width=15).pack(pady=5)
    ttk.Button(delay_window, text="Run", command=start_typing, width=15).pack(pady=10)
    ttk.Button(delay_window, text="Exit", command=exit_program, width=15).pack(pady=5)


# Start auto typing
def start_typing():
    global delay_start
    try:
        delay_start = float(delay_input.get().strip())
        if delay_start < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid non-negative number for delay!")
        return

    delay_window.withdraw()  # Hide current window
    auto_typer()


# Back to text window
def back_to_text_window():
    repeat_window.withdraw()  # Hide current window
    text_window.deiconify()  # Show text window again


# Back to repeat window
def back_to_repeat_window():
    interval_window.withdraw()  # Hide current window
    repeat_window.deiconify()  # Show repeat window again


# Back to interval window
def back_to_interval_window():
    delay_window.withdraw()  # Hide current window
    interval_window.deiconify()  # Show interval window again


# Main function
def main():
    global root
    root = tk.Tk()
    root.title("Auto Typer - Enter Text")
    root.geometry("650x400")
    root.configure(bg="#EAEAEA")

    ttk.Label(root, text="Enter the text you want to type:", font=("Helvetica", 12, "bold"), background="#EAEAEA").pack(pady=10)
    global text_input
    text_input = tk.Text(root, height=5, width=40, font=("Helvetica", 12))
    text_input.pack(pady=10)

    ttk.Button(root, text="Next", command=show_text_window, width=15).pack(pady=10)
    ttk.Button(root, text="Exit", command=exit_program, width=15).pack(pady=5)

    global text_window
    text_window = root
    root.mainloop()


# Run the main function
main()
