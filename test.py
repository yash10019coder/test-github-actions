import re
import sys

if (len(sys.argv) == 3):
  issue_title = sys.argv[1]
  issue_content = sys.argv[2]
  print('issue_title', issue_title)
  print('issue_content', issue_content)

# will check if the issue title is a temp or permanent transfer
# if (issue_title has temp)
# put the todo comment.
# else if (issue_title has perm)
# don't put todo comment

import os

stream = os.popen('gh issue list')
output = stream.read()
print('ISSUE_LIST:', repr(output))


filename = '.github/CODEOWNERS'

my_file = open(filename, "+r")

content = my_file.read()

if re.search('ran', content):
  content = re.sub('ran', 'gp201', content)
else:
  content = re.sub('gp201', 'ran', content)

my_file.seek(0)
my_file.write(content)
my_file.truncate()

my_file.seek(0)

print(my_file.read())

my_file.close()
