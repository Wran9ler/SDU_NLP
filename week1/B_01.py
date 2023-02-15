import os
import glob
import re
import pandas as pd


folder_list = ['business', 'entertaiment', 'politics', 'sport', 'tech']
parent_folder = 'C:\\Users\\Sultan\\Рабочий стол\\Git_dir\\Repo\\CSS-\\assignment-01-Wran9ler\\data\\bbc'

proper_names = []

for folder in folder_list:
    folder_path = os.path.join(parent_folder, folder)
    for file in glob.glob(os.path.join(folder_path, "*.txt")):
        with open(file, 'r', encoding='cp1252') as f:
            names = re.findall(r'\b(?!Mr\.|Dr\.|Ms\.)[A-Z]\w+\b', f.read())
            proper_names.extend(names)

proper_names = list(set(proper_names))

data = pd.DataFrame({'proper_names': proper_names})


