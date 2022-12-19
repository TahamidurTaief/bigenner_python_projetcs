import os

def ifnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
files= os.listdir()
files.remove("main.py")
files.remove("Automatic Folder Cleaner.py")
files.remove("venv")
files.remove(".idea")

ifnotexist('Image')
ifnotexist('Docs')
ifnotexist('Media')
ifnotexist('Other')

imgext= ['.png', '.jpeg', '.jpg', 'gif', '.PNG', '.JPEG']
images= [file for file in files if os.path.splitext(file)[1].lower() in imgext]

docext= ['.txt', '.rar', '.zip', '.docx']
docs= [file for file in files if os.path.splitext(file)[1].lower() in docext]

medext= ['mp3', 'mp4']
media= [file for file in files if os.path.splitext(file)[1].lower() in medext]

others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgext) and (ext not in docext) and (ext not in medext) and os.path.isfile(file):
        others.append(file)

for img in images:
    os.replace(img, f"Image/{img}")

for doc in docs:
    os.replace(doc, f'Docs/{doc}')

for med in media:
    os.replace(med, f'Media/{med}')

for oth in others:
    os.replace(oth, f"Other/{oth}")