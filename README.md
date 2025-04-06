# 🧠 Mindful Routine Notifier

A simple and personal desktop notification system that reminds you to stay mindful throughout your day — from journaling and meditation to tea breaks and bedtime routines.

<!-- Optional: Add a custom banner -->

## ✨ Features
- 🔔 Sends desktop notifications for mindfulness tasks
- 🗣️ Uses text-to-speech for audible reminders
- ⏰ Fully customizable daily routine
- 🧘 Designed for a calm, structured day
- 🔌 Runs offline – no internet needed

## 📋 Default Daily Routine

| Time   | Task                                 |
|--------|--------------------------------------|
| 06:00  | Wake up and start your day 🌅        |
| 06:30  | Morning exercise or yoga 🏋️‍♂️🧘     |
| 07:00  | Good morning! Time to journal 🌅     |
| 07:30  | Healthy breakfast time 🍳            |
| 08:00  | Time for a mindful meditation 🧘     |
| 09:00  | Start your work or study session 💻📚 |
| 10:30  | Take a break. Breathe and relax 🌬️  |
| 12:00  | Lunch break! Enjoy your meal 🍴      |
| 13:00  | Go for a short walk or stretch 🚶‍♂️  |
| 14:00  | Sip some tea and reset your mind ☕  |
| 15:30  | Quick break! Hydrate yourself 💧     |
| 17:00  | Wrap up your work or study session 📋|
| 18:00  | Evening exercise or walk 🏃‍♂️       |
| 19:00  | Dinner time! Enjoy your meal 🍽️     |
| 20:30  | Reflect on your day. Journal time 📓|
| 21:00  | Relax with a hobby or family time 🎨👨‍👩‍👧‍👦 |
| 22:00  | Prepare for a restful sleep 💤      |
| 22:30  | Unwind with light reading or meditation 📖🧘 |
| 23:00  | Goodnight! Time to unwind 🌙        |
| 23:30  | Prepare for bed. No screens! 📵     |
| 23:45  | Brush your teeth and relax 🪥       |
| 23:55  | Read a book before sleep 📚         |
| 00:25  | Sleep tight! Sweet dreams 🌌        |

## 🧰 Requirements
- Python 3.8+
- plyer
- schedule
- pyttsx3

## 📦 Installation
```bash
git clone https://github.com/kirankumarvel/mindful-routine-notifier.git
cd mindful-routine-notifier
pip install -r requirements.txt
```

## ▶️ Run the Notifier
```bash
python notifier.py
```
You'll see:
```vbnet
🧘 Mindful Notifier is running... Press Ctrl+C to stop.
```

## 📁 File Structure
```bash
mindful-routine-notifier/
├── notifier.py          # Main script that runs reminders
├── tts_helper.py        # Handles text-to-speech using pyttsx3
├── requirements.txt     # Required dependencies
└── README.md            # This file
```

## 💡 Customization
You can change the reminders list in `notifier.py` to your own timing and messages!

## 🚀 Ideas for Future
- Sync with Alexa/Google Home
- Add GUI for editing reminders
- Add persistent settings using JSON or SQLite

## 🧘‍♂️ Author
Kiran Kumar
- 🔗 [[LinkedIn](https://www.linkedin.com/in/kirankumarvel/)]
- 🌱 [[Personal Projects](https://github.com/Kirankumarvel/)]
- 🧠 Mental Wellness Advocate

---

