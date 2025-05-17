import threading
import random
from plyer import notification

messages = [
    "💧 Time for a water break! Stay hydrated!",
    "🚰 Don't forget to drink water—your body will thank you!",
    "🌊 Hydration check! Take a sip and keep your energy up!",
    "🥤 Water time! Refresh yourself and power through the day!",
    "💙 A little water goes a long way—grab a glass now!"
]

max_reminders = 8  # Stop after 8 reminders (8 hours)
reminder_count = 0  # Track the number of reminders

def send_notification():
    """Displays a desktop notification with a random message."""
    message = random.choice(messages)
    notification.notify(title="Water Reminder 🚰", message=message, timeout=10)

def reminder():
    """Triggers notification and sets up the next reminder if limit isn't reached."""
    global reminder_count
    if reminder_count < max_reminders:
        send_notification()
        reminder_count += 1
        threading.Timer(3600, reminder).start()  # Schedule next reminder
    else:
        print("🚀 Hydration goal reached! No more reminders.")

# Start the reminders
reminder()
