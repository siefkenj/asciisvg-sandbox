import io
import os
import pythonsvg
from lxml import etree

# ============================================================

# HTML Contents
contents = "<html> \
<body> \
<table border='1' cellpadding=10> \
<trbgcolor='#DDDDDD'><td>SVG Code</td><td>PNG Image</td><td>SVG Image</td><td>Refresh Page</td><tr>"

# ============================================================

# Read directory
path="/home/leen/SiyaVula/monassis/development/Tools/asciisvg-sandbox/pythonSVG/test_ascii_svg/test/"

i = 1
count_error = 0
count_success = 0

for dirpath, dirnames, filenames in os.walk(path):
    for filename in [f for f in filenames if f.endswith(".ascsvg")]:
        
			# Read ASCIISVG files
			g = open(os.path.join(dirpath, filename),'r')
			ascii_text = g.read()
			g.close()

			print str(i) + " " + filename.split(".")[0]

			# SVG (xml script)
			my_svg = pythonsvg.mySvgCanvas(filename.split(".")[0], 400, 400) # default size of SVG
			my_svg.process_ascii_multi_line(ascii_text)
			xml = my_svg.generate_string()

			# XML object
			svg_object = etree.fromstring(xml)

			# PNG Image	
			pythonsvg.create_png("png_images/" + filename.split(".")[0], int(float(svg_object.attrib['width'])), int(float(svg_object.attrib['height'])), xml) 

			# Append contents to the HTML page
			if ("ERROR" in xml): contents += "<tr bgcolor='#cd7879'><td>"; count_error += 1
			else: contents += "<tr bgcolor='#86cd78'><td>";  count_success += 1
			contents += "Folder: /" + dirpath.split("/")[-1] + "/<br>"
			if ("ERROR" in xml): contents += "Error: #" + str(count_error) + "<br>"
			else: contents += "Correct: #" + str(count_success) + "<br>"
			contents += "File: " + filename.split(".")[0] + ".png<br><br>"
			contents += "<textarea rows=20 cols=40>" + xml + "</textarea>"
			contents += "</td><td>"
			contents += "<img src='png_images/" + filename.split(".")[0] + ".png'/>"
			contents += "</td><td>"
			contents += xml
			contents += "</td><td>"
			contents += '<form><input type=button value="Refresh" onClick="window.location.reload()"></form>'
			contents += "</td></tr>"
		
			# Increment file name counter
			i = i + 1			

print "\nSuccess Count: " + str(count_success)
print "Error Count: " + str(count_error)

# ============================================================

# Complete HTML page
contents += "</table> \
</body> \
</html>"

# ============================================================

# Write HTML document
f = open('compare_graphs.html','w')
f.write(contents)
f.close()

# ============================================================

