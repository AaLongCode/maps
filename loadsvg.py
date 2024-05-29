import svgwrite
import tkinter as tk
from tkinterhtml import HtmlFrame

# Erstelle eine neue SVG-Zeichnung
dwg = svgwrite.Drawing(profile='tiny')

# Definiere den Pfad
path = dwg.path(d="M10,10 L10,20 L30,30", stroke="black", fill="none")

# Füge den Pfad zur Zeichnung hinzu
dwg.add(path)

# Speichere die Zeichnung in eine Variable
dwg_content = dwg.tostring()

# Erstelle eine HTML-Datei mit eingebettetem SVG und JavaScript für Zoom
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SVG Zoom Example</title>
    <style>
        .zoom-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }}
        .zoom-controls {{
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="zoom-container">
        <div class="zoom-controls">
            <label for="zoom">Zoom: </label>
            <input type="range" id="zoom" name="zoom" min="0.1" max="3.0" step="0.1" value="1" oninput="updateZoom(this.value)">
        </div>
        <div id="svg-container">
            {dwg_content}
        </div>
    </div>
    <script>
        function updateZoom(value) {{
            const svgElement = document.querySelector('#svg-container svg');
            svgElement.style.width = (value * 100) + '%';
            svgElement.style.height = (value * 100) + '%';
        }}
    </script>
</body>
</html>
"""

# Speichere die HTML-Datei
with open("svg_zoom_example.html", "w") as file:
    file.write(html_content)

# Erstelle ein tkinter-Fenster
root = tk.Tk()
root.title("SVG Zoom Example")

# Erstelle ein HtmlFrame-Widget und lade die HTML-Datei
frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.set_content("svg_zoom_example.html") 
frame.pack(fill="both", expand=True)

# Starte die tkinter-Hauptschleife
root.mainloop()