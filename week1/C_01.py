import os
import re
import pandas as pd

directory = r"C:\Users\Sultan\kat\dev"

all_results = []
for file in os.listdir(directory):
    with open(os.path.join(directory, file), 'r') as f:
        content = f.read()

        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        mail_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        phones = re.findall(phone_pattern, content)
        emails = re.findall(mail_pattern, content)

        for phone in phones:
            all_results.append({'File': file, 'Type': 'Phone', 'Value': phone, 'P/M': 'p'})
        for email in emails:
            all_results.append({'File': file, 'Type': 'Email', 'Value': email, 'P/M': 'm'})

df = pd.DataFrame(all_results)
df.to_csv('./result/C_01.csv', index=False)

print(all_results)
