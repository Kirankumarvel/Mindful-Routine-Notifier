import time
import schedule
from plyer import notification
from tts_helper import speak

# 💡 Custom notifications list
reminders = [
    {"time": "06:00", "task": "Wake up and start your day 🌅"},
    {"time": "06:30", "task": "Morning exercise or yoga 🏋️‍♂️🧘"},
    {"time": "07:00", "task": "Good morning! Time to journal 🌅"},
    {"time": "07:30", "task": "Healthy breakfast time 🍳"},
    {"time": "08:00", "task": "Time for a mindful meditation 🧘"},
    {"time": "09:00", "task": "Start your work or study session 💻📚"},
    {"time": "10:30", "task": "Take a break. Breathe and relax 🌬️"},
    {"time": "12:00", "task": "Lunch break! Enjoy your meal 🍴"},
    {"time": "13:00", "task": "Go for a short walk or stretch 🚶‍♂️"},
    {"time": "14:00", "task": "Sip some tea and reset your mind ☕"},
    {"time": "15:30", "task": "Quick break! Hydrate yourself 💧"},
    {"time": "17:00", "task": "Wrap up your work or study session 📋"},
    {"time": "18:00", "task": "Evening exercise or walk 🏃‍♂️"},
    {"time": "19:00", "task": "Dinner time! Enjoy your meal 🍽️"},
    {"time": "20:30", "task": "Reflect on your day. Journal time 📓"},
    {"time": "21:00", "task": "Relax with a hobby or family time 🎨👨‍👩‍👧‍👦"},
    {"time": "22:00", "task": "Prepare for a restful sleep 💤"},
    {"time": "22:30", "task": "Unwind with light reading or meditation 📖🧘"},
    {"time": "23:00", "task": "Goodnight! Time to unwind 🌙"},
    {"time": "23:30", "task": "Prepare for bed. No screens! 📵"},
    {"time": "23:45", "task": "Brush your teeth and relax 🪥"},
    {"time": "23:55", "task": "Read a book before sleep 📚"},
    {"time": "00:25", "task": "Sleep tight! Sweet dreams 🌌"},
]

def send_reminder(task):
    print(f"⏰ Reminder: {task}")
    notification.notify(
        title="Mindful Routine Notifier",
        message=task,
        timeout=10
    )
    speak(task)

# ✅ Test reminder on start
send_reminder("🧘 Mindful Notifier Started Successfully!")

# ⏱ Schedule each task
for reminder in reminders:
    try:
        schedule.every().day.at(reminder["time"]).do(send_reminder, task=reminder["task"])
    except Exception as e:
        print(f"⚠️ Error scheduling reminder at {reminder['time']}: {e}")

print("🧘 Mindful Notifier is running in background... Press Ctrl+C to stop.")

# 🔁 Run the scheduler
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("🛑 Mindful Notifier stopped manually.")
