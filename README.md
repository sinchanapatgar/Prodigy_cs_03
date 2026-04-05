🔑 PRODIGY_CS_03 – Password Complexity Checker
Prodigy Infotech Cybersecurity Internship – Task 03
📌 Overview
A Python GUI application that assesses password strength in real-time as you type. It checks multiple security criteria and gives detailed feedback to help users create strong, secure passwords.
🖥️ Features
⚡ Real-time strength analysis as you type
6-level strength rating: Very Weak → Excellent
Animated strength bar with color coding
Per-criterion visual indicators (✅ / ❌)
Pattern detection (repeated characters, sequential patterns)
Detailed suggestions for improvement
👁️ Show / Hide password toggle
Dark-themed GUI built with Tkinter
🧠 Scoring Criteria
Criteria
Points
Length ≥ 8 characters
+1
Length ≥ 12 characters
+2
Contains uppercase letters (A-Z)
+1
Contains lowercase letters (a-z)
+1
Contains numbers (0-9)
+1
Contains special characters (!@#$...)
+1
Repeated characters (aaa, 111)
-1 penalty
Sequential patterns (123, abc)
-1 penalty
Strength Levels
Score
Level
Color
0
Very Weak
🔴 Red
1
Weak
🟠 Orange
2
Fair
🟡 Amber
3
Moderate
🟡 Yellow
4
Strong
🟢 Light Green
5–6
Very Strong / Excellent
🟢 Cyan
🚀 How to Run
Prerequisites
Python 3.8+
No extra libraries needed (uses built-in tkinter and re)
Run the Program
python PRODIGY_CS_03.py
🖼️ Usage
Type a password in the input box
Watch the strength bar and criteria indicators update in real time
Read the suggestions panel for improvement tips
Toggle 👁️ to show/hide the password
📁 File Structure
PRODIGY_CS_03/
├── PRODIGY_CS_03.py   # Main program
└── README.md          # Documentation
🛠️ Tech Stack
Tool
Purpose
Python 3
Core language
tkinter
GUI framework
re (regex)
Pattern matching
💡 Tips for a Strong Password
Use 12+ characters
Mix uppercase, lowercase, numbers, and symbols
Avoid dictionary words and predictable sequences
Use a passphrase like Coffee!Sky#42Rain
