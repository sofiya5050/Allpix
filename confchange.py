import sys
import getopt
import re

# [filename, currentV]
_, filename, currentV = sys.argv
currentV = int(currentV)

with open(filename, 'r+') as f:
    lines = f.read().split('\n')

    for num, line in enumerate(lines):
        if line.startswith('bias_voltage'):
            lines[num] = re.sub(r'\d+', str(currentV), line, count=1)

        elif line.startswith('file_name'):
            match_obj = re.search(r'bias.*\d+', line)
            txt = re.sub(r'\d+', str(currentV), match_obj.group(0), count=1)
            lines[num] = re.sub(match_obj.group(0), txt, line, count=1)

    f.seek(0)
    f.truncate()
    f.write('\n'.join(lines))
