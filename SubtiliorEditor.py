import argparse
import xml.etree.ElementTree as ET
import verovio
from bs4 import BeautifulSoup

def parse_command_line():
    parser = argparse.ArgumentParser(description='Convert MEI to "subtilior" SVG')
    parser.add_argument('input_file', help='Input MEI file path')
    return parser.parse_args()

args = parse_command_line()
tree = ET.parse(args.input_file)
root = tree.getroot()
ns = {"mei": "http://www.music-encoding.org/ns/mei"}

def modify(root, ns):
    for note in root.findall(".//mei:note[@dur='dragma']", namespaces=ns):
        stem_down = ET.Element("stem", attrib={"dir": "down"})
        stem_up = ET.Element("stem", attrib={"dir": "up"})
        note.append(stem_down)
        note.append(stem_up)
        note.set("dur", "minima")

    for note in root.findall(".//mei:note[@dur='caudata 1']", namespaces=ns):
        stem_down = ET.Element("stem", attrib={"dir": "down"})
        stem_up = ET.Element("stem", attrib={"dir": "up", "flag.form": "curled", "flag.pos":"right"})
        note.append(stem_down)
        note.append(stem_up)
        note.set("dur", "semibrevis")

    for note in root.findall(".//mei:note[@dur='caudata 2']", namespaces=ns):
        stem_down = ET.Element("stem", attrib={"dir": "down", "flag.form": "curled", "flag.pos":"right"})
        stem_up = ET.Element("stem", attrib={"dir": "up"})
        note.append(stem_down)
        note.append(stem_up)
        note.set("dur", "semibrevis")

    for note in root.findall(".//mei:note[@dur='semibrevis maior']", namespaces=ns):
        note.set("dur", "semibrevis")
        stem_down = ET.Element("stem", attrib={"dir": "down"})
        note.append(stem_down)

    for note in root.findall(".//mei:note[@colored='red']", namespaces=ns):
        note.set("color", "rgba(252,0,0,1)")
        del note.attrib["colored"]

    for note in root.findall(".//mei:note[@colored='red and hollowed']", namespaces=ns):
        note.set("color", "rgba(252,0,0,1)")
        del note.attrib["colored"]
        note.set("colored", "true")

    for note in root.findall(".//mei:note[@colored='hollowed']", namespaces=ns):
        del note.attrib["colored"]
        note.set("colored", "true")

    for elem in root.iter():
        if elem.tag.startswith("{http://www.music-encoding.org/ns/mei}"):
            elem.tag = elem.tag.replace("{http://www.music-encoding.org/ns/mei}", "")

    for elem in root.iter():
        for key in list(elem.keys()):
            if key.startswith("{http://www.music-encoding.org/ns/mei}"):
                if key.endswith("stem.dir"):
                    elem.set(key.replace("{http://www.music-encoding.org/ns/mei}", ""), elem.attrib[key])
                del elem.attrib[key]

    output_file = "accurateMEI.xml"
    tree.write(output_file, encoding="utf-8")
    return output_file

output_file = modify(root, ns)
tk= verovio.toolkit()
tk.loadFile(output_file)
tk.getPageCount()
svg_string = tk.renderToSVG(1)
veroviosvg="verovio.svg"
tk.renderToSVGFile(veroviosvg,1)

tree = ET.parse(args.input_file)
root = tree.getroot()

minimae = root.findall(".//{http://www.music-encoding.org/ns/mei}note[@dur='minima']", namespaces=ns)
semimaior = root.findall(".//{http://www.music-encoding.org/ns/mei}note[@dur='semibrevis maior']", namespaces=ns)
caudata_1 = root.findall(".//{http://www.music-encoding.org/ns/mei}note[@dur='caudata 1']", namespaces=ns)
caudata_2 = root.findall(".//{http://www.music-encoding.org/ns/mei}note[@dur='caudata 2']", namespaces=ns)

semiho =[]
semib = []
if semimaior:
   for note in semimaior:
      coloured_value = note.get("colored")
      note_id = note.get("{http://www.w3.org/XML/1998/namespace}id")
      if coloured_value == "hollowed" or coloured_value == "red and hollowed":
           semiho.append(note_id)
      else:
         semib.append(note_id)

caudaho = []
caudab = []
if caudata_1:
   for note in caudata_1:
      coloured_value = note.get("colored")
      note_id = note.get("{http://www.w3.org/XML/1998/namespace}id")
      if coloured_value == "hollowed" or coloured_value == "red and hollowed":
           caudaho.append(note_id)
      else:
         caudab.append(note_id)

cauda2ho = []
cauda2b = []
if caudata_2:
   for note in caudata_2:
      coloured_value = note.get("colored")
      note_id = note.get("{http://www.w3.org/XML/1998/namespace}id")
      if coloured_value == "hollowed" or coloured_value == "red and hollowed":
           cauda2ho.append(note_id)
      else:
         cauda2b.append(note_id)

l_minimae=[]
for minima in minimae:
   coloured_value = minima.get("colored")
   note_id = minima.get("{http://www.w3.org/XML/1998/namespace}id")
   if coloured_value == "red and hollowed" or coloured_value == "hollowed":
        l_minimae.append(note_id)

with open(veroviosvg, "r") as svg_file:
    svg_content = svg_file.read()
    soup = BeautifulSoup(svg_content, "xml")

for text_element in soup.find_all('text'):
    text_element['fill'] = 'black'

for rect_element in soup.find_all('rect'):
    if 'rx' not in rect_element.attrs:
        rect_element['fill'] = 'black'

for g_id in caudaho:
    g_element = soup.find("g", id=g_id)
    if g_element:
        use_elements = g_element.find_all("use")
        for use_element in use_elements:
            use_element["xlink:href"] = "#K001"

for g_id in caudab:
    g_element = soup.find("g", id=g_id)
    if g_element:
        use_elements = g_element.find_all("use")
        for use_element in use_elements:
            use_element["xlink:href"] = "#K006"

for g_id in cauda2ho:
    g_element = soup.find("g", id=g_id)
    if g_element:
        use_elements = g_element.find_all("use")
        for use_element in use_elements:
            use_element["xlink:href"] = "#K002"

for g_id in cauda2b:
    g_element = soup.find("g", id=g_id)
    if g_element:
        use_elements = g_element.find_all("use")
        for use_element in use_elements:
            use_element["xlink:href"] = "#K007"

for g_id in l_minimae:
    g_element = soup.find("g", id=g_id)  # Recherche l'élément <g> par ID
    if g_element:
        notehead_elements = g_element.find_all("g", class_="notehead")  # Recherche les éléments <g> avec la classe "notehead"
        for notehead_element in notehead_elements:
            use_element = notehead_element.find("use")  # Recherche l'élément <use> à l'intérieur de <g class="notehead">
            if use_element:
                use_element["xlink:href"] = "#K003"

for g_id in semiho:
    g_element = soup.find("g", id=g_id)  # Recherche l'élément <g> par ID
    if g_element:
        notehead_elements = g_element.find_all("g", class_="notehead")  # Recherche les éléments <g> avec la classe "notehead"
        for notehead_element in notehead_elements:
            use_element = notehead_element.find("use")  # Recherche l'élément <use> à l'intérieur de <g class="notehead">
            if use_element:
                use_element["xlink:href"] = "#K005"

for g_id in semib:
    g_element = soup.find("g", id=g_id)  # Recherche l'élément <g> par ID
    if g_element:
        notehead_elements = g_element.find_all("g", class_="notehead")  # Recherche les éléments <g> avec la classe "notehead"
        for notehead_element in notehead_elements:
            use_element = notehead_element.find("use")  # Recherche l'élément <use> à l'intérieur de <g class="notehead">
            if use_element:
                use_element["xlink:href"] = "#K004"

def load_and_append_symbols(file_paths, defs_element):
    for file_path in file_paths:
        tree = ET.parse(file_path)
        symbols_root = tree.getroot()
        for symbol in symbols_root.findall(".//symbol"):
            symbol_string = ET.tostring(symbol, encoding="unicode")
            symbol_soup = BeautifulSoup(symbol_string, "xml")
            defs_element.append(symbol_soup)

symbols_files = ["Font/hollowed1.xml", "Font/hollowed2.xml", "Font/hollowed3.xml", "Font/semibrevismaior.xml", "Font/semibrevishollow.xml", "Font/cauda1.xml", "Font/cauda2.xml"]
defs_element = soup.find("defs")

if defs_element:
    load_and_append_symbols(symbols_files, defs_element)

with open("subtilior.svg", "w") as output_file:
    output_file.write(str(soup))
