import tkinter as tk

class BouncingBallAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Ball Animation")

        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(10, 10, 30, 30, fill="blue", outline="blue")

        self.dx = 5
        self.dy = 5

        self.animate()

    def animate(self):

        self.canvas.move(self.ball, self.dx, self.dy)


        x1, y1, x2, y2 = self.canvas.coords(self.ball)


        if x1 < 0 or x2 > 400:
            self.dx *= -1

        if y1 < 0 or y2 > 300:
            self.dy *= -1


        self.root.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBallAnimation(root)
    root.mainloop()