import pandas as pd
import re

data = pd.read_csv('C:\\Users\\Sultan\\Рабочий стол\\Git_dir\\Repo\\CSS-\\assignment-01-Wran9ler\\data\\StateGrants.csv', header=None, names=['ns'])

f_pattern = [r'[вн]а\b', r'[қгк]ызы\b']
m_pattern = [r'[ео]в\b', r".*вич", r'[ұу]лы\b']

pattern = f_pattern + m_pattern

data = data.reset_index(drop=True)

compiled_f_patterns = [re.compile(p) for p in f_pattern]
compiled_m_patterns = [re.compile(p) for p in m_pattern]

data_gender = []

for i in data['ns']:
    match = False
    for p in compiled_f_patterns:
        if p.search(i.lower()):
            data_gender.append("F")
            match = True
            break
    if not match:
        for p in compiled_m_patterns:
            if p.search(i.lower()):
                data_gender.append("M")
                match = True
                break
    if not match:
        data_gender.append("N")

data["gender"] = data_gender

