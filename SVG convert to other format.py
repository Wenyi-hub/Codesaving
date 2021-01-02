import svglib
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


drawing = svg2rlg("<filename>.svg")
renderPDF.drawToFile(drawing, "<filename>.pdf")
renderPM.drawToFile(drawing, "<filename>", fmt="PNG")
renderPM.drawToFile(drawing, "<filename>.jpg", fmt="JPG")