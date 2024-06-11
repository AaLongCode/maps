import tkinter as tk
from tksvg import SvgImage

class SvgZoomApp:
    def __init__(self, root, svg_path):
        self.root = root
        self.root.title("SVG Zoom Example")

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill="both", expand=True)

        self.svg_image = SvgImage(file=svg_path)
        self.canvas.create_image(0, 0, anchor="nw", image=self.svg_image)

        self.scale_factor = 1.0
        self.canvas.bind("<MouseWheel>", self.zoom)

        # Update the canvas size based on the SVG image size
        self.update_canvas_size()

    def update_canvas_size(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.svg_image)

    def zoom(self, event):
        if event.delta > 0:
            self.svg_imgae = self.svg_image.zoom(2,2)
        else:
            self.svg_imgae = self.svg_image.zoom(2,2)
        self.update_canvas_size()

if __name__ == "__main__":
    root = tk.Tk()
    svg_file = "maptest.svg"  # Ersetzen Sie dies durch den Pfad Ihrer SVG-Datei
    app = SvgZoomApp(root, svg_file)
    root.mainloop()