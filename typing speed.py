import tkinter as tk
import time
import random

# Sample sentences (you can add more)
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing fast and accurately is a great skill.",
    "AI is changing the future of technology.",
    "Always keep learning and improving your skills."
]

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("700x400")
        self.root.configure(bg="#1e1e2f")

        self.sentence = random.choice(sentences)
        self.start_time = 0
        self.end_time = 0

        self.title_label = tk.Label(root, text="⏱ Typing Speed Tester", font=("Helvetica", 20, "bold"), bg="#1e1e2f", fg="white")
        self.title_label.pack(pady=20)

        self.sentence_label = tk.Label(root, text=self.sentence, wraplength=650, font=("Arial", 14), bg="#1e1e2f", fg="#f1c40f")
        self.sentence_label.pack(pady=10)

        self.entry = tk.Text(root, height=5, width=70, font=("Arial", 14), wrap="word", bd=3, relief="solid")
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)

        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#1e1e2f", fg="white")
        self.result_label.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Speed", font=("Arial", 12, "bold"), bg="#9b59b6", fg="white", command=self.check_speed)
        self.check_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Try Another Sentence", font=("Arial", 12, "bold"), bg="#8e44ad", fg="white", command=self.reset)
        self.reset_button.pack(pady=5)

    def start_timer(self, event):
        self.start_time = time.time()

    def check_speed(self):
        self.end_time = time.time()
        typed_text = self.entry.get("1.0", "end-1c").strip()
        elapsed_time = round(self.end_time - self.start_time, 2)

        # Words per minute
        word_count = len(typed_text.split())
        wpm = round((word_count / elapsed_time) * 60)

        # Accuracy
        original_words = self.sentence.split()
        typed_words = typed_text.split()
        correct = 0
        for o, t in zip(original_words, typed_words):
            if o == t:
                correct += 1
        accuracy = round((correct / len(original_words)) * 100)

        self.result_label.config(text=f"Time: {elapsed_time} sec  |  WPM: {wpm}  |  Accuracy: {accuracy}%")

    def reset(self):
        self.sentence = random.choice(sentences)
        self.sentence_label.config(text=self.sentence)
        self.entry.delete("1.0", "end")
        self.result_label.config(text="")
        self.start_time = 0

# Run the app
root = tk.Tk()
app = TypingSpeedTester(root)
root.mainloop()
