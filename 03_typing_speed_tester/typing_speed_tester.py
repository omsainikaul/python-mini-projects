import time
import random

# display the text that has to be typed
text_to_type = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be, or not to be, that is the question."
    ]
print("Type the following text as quickly and accurately as possible:")
text = random.choice(text_to_type)
print(text)

# calculate the time taken to type the text
start_time = time.time()

# take input from the user
user_input = input("Your input: ")

end_time = time.time()
time_taken = end_time - start_time
print(f"Time taken: {time_taken:.2f} seconds")

# calculate the typing speed in words per minute (WPM)
words = user_input.split()
if time_taken > 0:
    wpm = len(words) / (time_taken / 60)
else:
    wpm = 0
print(f"Typing speed: {wpm:.2f} WPM")

# calculate the accuracy of the typed text
correct_chars = sum(1 for a, b in zip(user_input, text) if a == b)
accuracy = (correct_chars / len(text)) * 100
print(f"Accuracy: {accuracy:.2f}%")
