"""Professional, playable Snake game using Tkinter.

Features:
- Responsive keyboard controls (arrows and WASD)
- Pause/resume (P), restart (Enter after game over)
- Increasing speed as score increases
- Persistent high score saved beside script
- Clean, self-contained single-file implementation

Run: python Projects/snake_game.py
"""

import tkinter as tk
import random
import os


class SnakeGame:
	def __init__(self, master):
		self.master = master
		master.title("Snake — Python Basics")

		# Game configuration
		self.cell_size = 20
		self.cols = 40
		self.rows = 30
		self.width = self.cell_size * self.cols
		self.height = self.cell_size * self.rows

		self.speed_base = 200  # milliseconds per move (will decrease). Increased for a slower start
		self.running = False
		self.paused = False
		self.game_over = False

		# Score and high score
		self.score = 0
		self.highscore_file = os.path.join(os.path.dirname(__file__), "snake_highscore.txt")
		self.highscore = self._load_highscore()

		# Canvas
		self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="#0f1720")
		self.canvas.pack(side=tk.TOP)

		# Info label
		self.info_var = tk.StringVar()
		self._update_info_text()
		self.info_label = tk.Label(master, textvariable=self.info_var, font=("Consolas", 12), bg="#0f1720", fg="#e2e8f0")
		self.info_label.pack(fill=tk.X)

		# Bind controls
		master.bind("<Key>", self.on_key)

		self.reset()
		self.start()

	def reset(self):
		self.direction = (1, 0)  # moving right
		cx = self.cols // 2
		cy = self.rows // 2
		self.snake = [(cx - i, cy) for i in range(3)]  # initial 3-length snake
		self._place_food()
		self.score = 0
		self.game_over = False
		self.paused = False
		self._update_info_text()

	def start(self):
		if not self.running:
			self.running = True
			self._loop()

	def stop(self):
		self.running = False

	def _load_highscore(self):
		try:
			with open(self.highscore_file, "r") as f:
				return int(f.read().strip() or 0)
		except Exception:
			return 0

	def _save_highscore(self):
		try:
			with open(self.highscore_file, "w") as f:
				f.write(str(self.highscore))
		except Exception:
			pass

	def _place_food(self):
		free = set((x, y) for x in range(self.cols) for y in range(self.rows)) - set(self.snake)
		self.food = random.choice(list(free))

	def on_key(self, event):
		if event.keysym.lower() in ("up", "w"):
			self._set_direction(0, -1)
		elif event.keysym.lower() in ("down", "s"):
			self._set_direction(0, 1)
		elif event.keysym.lower() in ("left", "a"):
			self._set_direction(-1, 0)
		elif event.keysym.lower() in ("right", "d"):
			self._set_direction(1, 0)
		elif event.keysym.lower() == "p":
			if not self.game_over:
				self.paused = not self.paused
				self._update_info_text()
		elif event.keysym == "Return":
			if self.game_over:
				self.reset()
				self.start()

	def _set_direction(self, dx, dy):
		# Prevent direct reverse
		if (dx, dy) == (-self.direction[0], -self.direction[1]):
			return
		self.direction = (dx, dy)

	def _loop(self):
		if not self.running:
			return
		if not self.paused and not self.game_over:
			self._move()
		self._draw()
		delay = max(30, int(self.speed_base - self.score * 3))
		self.master.after(delay, self._loop)

	def _move(self):
		head = self.snake[0]
		new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

		# Check collisions with walls
		if not (0 <= new_head[0] < self.cols and 0 <= new_head[1] < self.rows):
			self._end_game()
			return

		# Check collisions with self
		if new_head in self.snake:
			self._end_game()
			return

		self.snake.insert(0, new_head)

		if new_head == self.food:
			self.score += 1
			if self.score > self.highscore:
				self.highscore = self.score
				self._save_highscore()
			self._place_food()
		else:
			self.snake.pop()

	def _end_game(self):
		self.game_over = True
		self.paused = False
		self._update_info_text()

	def _draw(self):
		self.canvas.delete("all")

		# Draw grid subtle lines
		for i in range(0, self.width, self.cell_size * 5):
			self.canvas.create_line(i, 0, i, self.height, fill="#071024")
		for j in range(0, self.height, self.cell_size * 5):
			self.canvas.create_line(0, j, self.width, j, fill="#071024")

		# Draw food
		fx, fy = self.food
		x1, y1 = fx * self.cell_size, fy * self.cell_size
		x2, y2 = x1 + self.cell_size, y1 + self.cell_size
		self.canvas.create_oval(x1 + 3, y1 + 3, x2 - 3, y2 - 3, fill="#ef4444", outline="#b91c1c")

		# Draw snake
		for i, (sx, sy) in enumerate(self.snake):
			x1, y1 = sx * self.cell_size, sy * self.cell_size
			x2, y2 = x1 + self.cell_size, y1 + self.cell_size
			if i == 0:
				self.canvas.create_rectangle(x1, y1, x2, y2, fill="#10b981", outline="#065f46")
			else:
				self.canvas.create_rectangle(x1 + 1, y1 + 1, x2 - 1, y2 - 1, fill="#34d399", outline="#047857")

		# If game over, show message
		if self.game_over:
			self.canvas.create_rectangle(100, 200, self.width - 100, 360, fill="#0b1220", outline="#334155", width=2)
			self.canvas.create_text(self.width // 2, 240, text="Game Over", fill="#f8fafc", font=("Consolas", 28, "bold"))
			self.canvas.create_text(self.width // 2, 280, text=f"Score: {self.score}  Highscore: {self.highscore}", fill="#e2e8f0", font=("Consolas", 14))
			self.canvas.create_text(self.width // 2, 320, text="Press Enter to play again", fill="#94a3b8", font=("Consolas", 12))

	def _update_info_text(self):
		status = "Paused" if self.paused else ("Game Over" if self.game_over else "Running")
		self.info_var.set(f"Score: {self.score}    Highscore: {self.highscore}    Status: {status}    Controls: Arrows/WASD — P to pause")


def main():
	root = tk.Tk()
	# Fix window position and disallow resizing for consistent gameplay
	root.resizable(False, False)
	game = SnakeGame(root)
	root.mainloop()


if __name__ == "__main__":
	main()
