import shutil
try:
    shutil.copy2('text_ny.txt', 'backup/text_ny.old')
    print('Filen har kopierats till backup mappen')
except FileNotFoundError:
    print('Filen du vill kopiera hittas ej.')
    print('Kontrolera filnamnet och försök igen')
    