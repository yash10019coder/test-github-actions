import re
import sys

issue_title = sys.argv[1]
issue_content = sys.argv[2]

print('issue_title', issue_title)
print('issue_content', issue_content)

filename = '.github/CODEOWNERS'

my_file = open(filename, "+r")

content = my_file.read()

if re.search('ran',content):
  content = re.sub('ran', 'gp201', content)
else:
  content = re.sub('gp201', 'ran', content)

my_file.seek(0)
my_file.write(content)
my_file.truncate()

my_file.seek(0)

print(my_file.read())

my_file.close()