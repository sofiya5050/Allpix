import sys
import getopt
import re

# [filename, currentV]
_, filename, currentV, VFD, fluencePower = sys.argv
currentV, VFD = int(currentV), int(VFD)

with open(filename, 'r+') as f:
    lines = f.read().split('\n')

    for num, line in enumerate(lines):
        if line.startswith('bias_voltage'):
            lines[num] = re.sub(r'\d+', str(currentV), line, count=1)

        elif line.startswith('fluence'):
            lines[num] = re.sub(r'1e\d+', f"1e{fluencePower}", line, count=1)

        if line.startswith('depletion_voltage'):
            lines[num] = re.sub(r'\d+', str(VFD), line, count=1)

        elif line.startswith('file_name'):
            match_obj = re.search(r'bias.*\d+', line)
            txt = re.sub(r'\d+', str(currentV), match_obj.group(0), count=1)
            lines[num] = re.sub(match_obj.group(0), txt, line, count=1)

            print(lines[num])

            match_obj_2 = re.search(r'fluence.*1e\d+neq', lines[num])
            txt_2 = re.sub(r'1e\d+neq', f"1e{fluencePower}neq", match_obj_2.group(0), count=1)
            lines[num] = re.sub(match_obj_2.group(0), txt_2, lines[num], count=1)

            print(lines[num])

            match_obj_3 = re.search(r'VFD.*\d+', lines[num])
            txt_3 = re.sub(r'\d+', str(VFD), match_obj_3.group(0), count=1)
            lines[num] = re.sub(match_obj_3.group(0), txt_3, lines[num], count=1)

            print(lines[num])

    f.seek(0)
    f.truncate()
    f.write('\n'.join(lines))
