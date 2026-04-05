"""
PRODIGY_CS_03 - Password Complexity Checker
Prodigy Infotech Cybersecurity Internship - Task 03
Assess password strength based on length, character variety, and patterns.
"""

import tkinter as tk
from tkinter import font
import re


def check_password(password):
    score = 0
    feedback = []
    checks = {}

    # Length
    length = len(password)
    checks['length_ok'] = length >= 8
    checks['length_strong'] = length >= 12
    if length == 0:
        return 0, [], checks
    if length < 8:
        feedback.append("❌ Too short — use at least 8 characters")
    elif length < 12:
        feedback.append("⚠️  Good length, 12+ is stronger")
        score += 1
    else:
        feedback.append("✅ Excellent length")
        score += 2

    # Uppercase
    checks['has_upper'] = bool(re.search(r'[A-Z]', password))
    if checks['has_upper']:
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")

    # Lowercase
    checks['has_lower'] = bool(re.search(r'[a-z]', password))
    if checks['has_lower']:
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Add lowercase letters (a-z)")

    # Digits
    checks['has_digit'] = bool(re.search(r'\d', password))
    if checks['has_digit']:
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # Special characters
    checks['has_special'] = bool(re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\;\'`~/]', password))
    if checks['has_special']:
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Add special characters (!@#$...)")

    # Common patterns penalty
    checks['no_repeat'] = not bool(re.search(r'(.)\1{2,}', password))
    checks['no_sequence'] = not bool(re.search(r'(012|123|234|345|456|567|678|789|abc|bcd|cde|def)', password.lower()))
    if not checks['no_repeat']:
        score = max(0, score - 1)
        feedback.append("⚠️  Avoid repeating characters (aaa, 111)")
    if not checks['no_sequence']:
        score = max(0, score - 1)
        feedback.append("⚠️  Avoid sequential patterns (123, abc)")

    return score, feedback, checks


STRENGTH_LEVELS = [
    (0, "VERY WEAK",  "#ff2244", "#330008"),
    (1, "WEAK",       "#ff5533", "#2a0e05"),
    (2, "FAIR",       "#ffaa00", "#2a1a00"),
    (3, "MODERATE",   "#ffdd00", "#1f1a00"),
    (4, "STRONG",     "#88dd00", "#131a00"),
    (5, "VERY STRONG","#00ffcc", "#001a13"),
    (6, "EXCELLENT!", "#00ffcc", "#001a13"),
]


class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker - PRODIGY_CS_03")
        self.root.geometry("620x680")
        self.root.configure(bg="#0d0d1a")
        self.root.resizable(False, False)
        self.show_pass = False
        self.build_ui()

    def build_ui(self):
        # Header
        tk.Label(self.root, text="🔑 Password Strength Checker",
                 font=("Courier New", 18, "bold"), fg="#ffdd00", bg="#0d0d1a").pack(pady=(24, 2))
        tk.Label(self.root, text="PRODIGY INFOTECH  |  CS Task 03",
                 font=("Courier New", 8), fg="#333355", bg="#0d0d1a").pack()
        tk.Frame(self.root, height=1, bg="#1e1e3a").pack(fill='x', padx=30, pady=14)

        # Password entry
        tk.Label(self.root, text="Enter Password", font=("Courier New", 10, "bold"),
                 fg="#7777aa", bg="#0d0d1a").pack(anchor='w', padx=40)

        entry_frame = tk.Frame(self.root, bg="#131325",
                               highlightthickness=1, highlightbackground="#2e2e5e")
        entry_frame.pack(padx=40, fill='x', pady=(4, 0))

        self.pass_var = tk.StringVar()
        self.pass_var.trace('w', self.on_change)
        self.entry = tk.Entry(entry_frame, textvariable=self.pass_var,
                              show="●", font=("Courier New", 14),
                              bg="#131325", fg="#ffdd00", insertbackground="#ffdd00",
                              relief='flat', bd=0)
        self.entry.pack(side='left', fill='x', expand=True, padx=12, pady=10)

        self.toggle_btn = tk.Button(entry_frame, text="👁", font=("Courier New", 11),
                                    bg="#131325", fg="#555577", relief='flat',
                                    cursor='hand2', command=self.toggle_show,
                                    activebackground="#131325", activeforeground="#ffdd00",
                                    bd=0)
        self.toggle_btn.pack(side='right', padx=8)

        # Strength bar
        tk.Label(self.root, text="Strength", font=("Courier New", 9, "bold"),
                 fg="#444466", bg="#0d0d1a").pack(anchor='w', padx=40, pady=(14, 4))

        bar_frame = tk.Frame(self.root, bg="#0d0d1a")
        bar_frame.pack(padx=40, fill='x')
        self.bars = []
        for i in range(6):
            b = tk.Frame(bar_frame, height=10, bg="#1a1a2e",
                         highlightthickness=0)
            b.pack(side='left', expand=True, fill='x', padx=2)
            self.bars.append(b)

        # Strength label
        self.strength_var = tk.StringVar(value="—")
        self.strength_label = tk.Label(self.root, textvariable=self.strength_var,
                                       font=("Courier New", 22, "bold"),
                                       fg="#333355", bg="#0d0d1a")
        self.strength_label.pack(pady=(10, 0))

        # Criteria indicators
        tk.Frame(self.root, height=1, bg="#1e1e3a").pack(fill='x', padx=30, pady=12)
        tk.Label(self.root, text="Criteria", font=("Courier New", 9, "bold"),
                 fg="#444466", bg="#0d0d1a").pack(anchor='w', padx=40)

        crit_frame = tk.Frame(self.root, bg="#0d0d1a")
        crit_frame.pack(padx=40, fill='x', pady=(6, 0))

        criteria = [
            ('length_ok',    '8+ chars'),
            ('length_strong','12+ chars'),
            ('has_upper',    'Uppercase'),
            ('has_lower',    'Lowercase'),
            ('has_digit',    'Numbers'),
            ('has_special',  'Special chars'),
            ('no_repeat',    'No repeats'),
            ('no_sequence',  'No sequences'),
        ]
        self.crit_labels = {}
        for i, (key, label) in enumerate(criteria):
            col = i % 4
            row = i // 4
            f = tk.Frame(crit_frame, bg="#111122", padx=8, pady=5,
                         highlightthickness=1, highlightbackground="#1e1e3a")
            f.grid(row=row, column=col, padx=4, pady=4, sticky='ew')
            crit_frame.columnconfigure(col, weight=1)
            dot = tk.Label(f, text="○", font=("Courier New", 10), fg="#333355", bg="#111122")
            dot.pack(side='left')
            tk.Label(f, text=label, font=("Courier New", 8), fg="#555577", bg="#111122").pack(side='left', padx=4)
            self.crit_labels[key] = dot

        # Feedback
        tk.Frame(self.root, height=1, bg="#1e1e3a").pack(fill='x', padx=30, pady=12)
        tk.Label(self.root, text="Suggestions", font=("Courier New", 9, "bold"),
                 fg="#444466", bg="#0d0d1a").pack(anchor='w', padx=40)

        fb_frame = tk.Frame(self.root, bg="#111122",
                            highlightthickness=1, highlightbackground="#1e1e3a")
        fb_frame.pack(padx=40, fill='both', expand=True, pady=(4, 20))

        self.feedback_text = tk.Text(fb_frame, font=("Courier New", 9),
                                     bg="#111122", fg="#aaaacc", relief='flat',
                                     padx=12, pady=8, state='disabled',
                                     height=6, wrap='word')
        self.feedback_text.pack(fill='both', expand=True)

    def toggle_show(self):
        self.show_pass = not self.show_pass
        self.entry.config(show="" if self.show_pass else "●")

    def on_change(self, *args):
        password = self.pass_var.get()
        score, feedback, checks = check_password(password)

        # Update bars
        level = min(score, 6)
        _, label, color, _ = STRENGTH_LEVELS[min(score, len(STRENGTH_LEVELS)-1)]
        for i, bar in enumerate(self.bars):
            bar.config(bg=color if i < level else "#1a1a2e")

        # Update strength label
        if not password:
            self.strength_var.set("—")
            self.strength_label.config(fg="#333355")
        else:
            self.strength_var.set(label)
            self.strength_label.config(fg=color)

        # Update criteria dots
        for key, dot in self.crit_labels.items():
            val = checks.get(key, False)
            dot.config(text="●" if val else "○",
                       fg="#00ffcc" if val else "#333355")

        # Update feedback
        self.feedback_text.config(state='normal')
        self.feedback_text.delete("1.0", "end")
        self.feedback_text.insert("end", "\n".join(feedback) if feedback else "Start typing a password...")
        self.feedback_text.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()
