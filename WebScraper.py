#Function to save HTML locally.
def save_html(html, path):
    with open(path, 'wb') as f: #wb stands for "write bytes. Avoids encoding issues when saving"
        f.write(html)

#Function to open HTML from a local file.
def open_html(path):
    with open(path, 'rb') as f: #rb stands for "read bytes".
        return f.read()