import xml.etree.ElementTree as ET

# Function to add encoding declaration if missing
def ensure_encoding(file_path):
    with open(file_path, 'r+', encoding='utf-8') as f:
        content = f.read()

        # Check if encoding declaration exists
        if not content.startswith('<?xml'):
            # Add the encoding declaration at the start of the file
            content = '<?xml version="1.0" encoding="UTF-8"?>\n' + content

            # Move the file pointer to the beginning and overwrite the file
            f.seek(0)
            f.write(content)

# File paths (input and output)
input_file1 = 'guide.xml'  # Replace with the first EPG file path
input_file2 = 'live.xml'  # Replace with the second EPG file path
output_file = 'epg.xml'  # Output file path

ensure_encoding(input_file1)
ensure_encoding(input_file2)

# Parse the first XML file
tree1 = ET.parse(input_file1)
root1 = tree1.getroot()

# Parse the second XML file
tree2 = ET.parse(input_file2)
root2 = tree2.getroot()

# Ensure that both files have the same root element (e.g., <tv>)
if root1.tag != root2.tag:
    raise ValueError("The root elements of the two XML files do not match!")

# Append all the children from root2 into root1
for element in root2:
    root1.append(element)

# Write the combined tree to a new XML file
tree1.write(output_file, encoding='utf-8', xml_declaration=True)

print(f"Combined EPG XML saved as: {output_file}")

