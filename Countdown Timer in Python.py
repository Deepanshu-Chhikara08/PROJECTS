import time
import winsound
import streamlit as st
from streamlit_option_menu import option_menu

# Set up the Streamlit page
st.title("Countdown Timer")

# Horizontal option menu for selecting the countdown type
selected = option_menu(
    None,
    ["Hours", "Min", "Sec"],
    icons=['clock', 'clock', 'clock'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    key="menu"
)

# Function to handle seconds countdown
def Sec():
    sec = st.text_input("Enter seconds for countdown:")
    if sec:
        try:
            sec = int(sec)
            countdown_placeholder = st.empty()  # Placeholder for dynamic updates

            for i in range(sec, -1, -1):
                countdown_placeholder.write(f"00:00:{i:02}")  # Format as 00:00:XX
                time.sleep(1)

            winsound.Beep(4150, 500)
            st.success("Countdown Complete!")
        except ValueError:
            st.warning("Please enter a valid number of seconds.")

# Function to handle minutes countdown
def Min():
    minutes = st.text_input("Enter minutes for countdown:")
    if minutes:
        try:
            minutes = int(minutes)
            countdown_placeholder = st.empty()

            for min_remaining in range(minutes - 1, -1, -1):
                for sec_remaining in range(59, -1, -1):
                    countdown_placeholder.write(f"00:{min_remaining:02}:{sec_remaining:02}")
                    time.sleep(1)

            winsound.Beep(4150, 500)
            st.success("Countdown Complete!")
        except ValueError:
            st.warning("Please enter a valid number of minutes.")

# Function to handle hours countdown
def Hours():
    hours = st.text_input("Enter hours for countdown:")
    if hours:
        try:
            hours = int(hours)
            countdown_placeholder = st.empty()

            for hr_remaining in range(hours - 1, -1, -1):
                for min_remaining in range(59, -1, -1):
                    for sec_remaining in range(59, -1, -1):
                        countdown_placeholder.write(f"{hr_remaining:02}:{min_remaining:02}:{sec_remaining:02}")
                        time.sleep(1)

            winsound.Beep(2000, 7000)
            st.success("Countdown Complete!")
        except ValueError:
            st.warning("Please enter a valid number of hours.")

# Determine which function to call based on the selected option
if selected == "Hours":
    Hours()
elif selected == "Min":
    Min()
elif selected == "Sec":
    Sec()
