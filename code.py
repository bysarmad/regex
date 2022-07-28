# Load packages
import re

# Upload your data as a .txt file and load it as a data frame 
with open('placeholder.txt') as txt:      # Replace with the name of your .txt file
    contents = txt.read()       
    print(contents)                       # Uncomment to prevent printing text

    # Works with all email addresses with standard English characters
email_regex = r'[\w\.-]+@[\w\.-]+'        # Specify the regex pattern
matches = re.findall(email_regex,          
                     contents)             

# Print results
for email in matches:
    print(email)       

# Works for most international numbers.
phones = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
matches = re.findall(phones, 
                     contents)

# Print results
for phone in matches:
    print(phone)