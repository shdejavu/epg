# File paths for input and output
file1 = 'live.xml'
file2 = 'guide.xml'
output_file = 'epg.xml'

# Step 1: Read the contents of both files
with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
    content1 = f1.read()
    content2 = f2.read()

# Step 2: Ensure file1 has the XML declaration
if not content1.startswith('<?xml'):
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
    content1 = xml_declaration + content1

# Step 3: Remove the XML declaration and root tags from the second file
content2 = content2.replace('<?xml version="1.0" encoding="UTF-8"?>', '').strip()

# Remove opening and closing <tv> tags from content2
content2 = content2.replace('<tv>', '').replace('</tv>', '').strip()

# Step 4: Merge the content inside the <tv> root element
combined_content = content1.rstrip('</tv>') + '\n' + content2 + '\n</tv>'

# Step 5: Write the combined content to a new file with UTF-8 encoding
with open(output_file, 'w', encoding='utf-8') as out:
    out.write(combined_content)

print(f"Combined EPG file saved as: {output_file}")
