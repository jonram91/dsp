import csv
import advanced_python_regex


with open("emails.csv", "w", newline = '' ) as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerows(advanced_python_regex.emails_data)