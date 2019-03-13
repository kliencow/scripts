import re
import sys
import os

matcher = r'<mode>.*?</mode>'
findLetter = r'G'
replacementLetter = r'N'

directory = sys.argv[1]
for filename in os.listdir(directory):
    filename = directory+"/"+filename.strip()
    if not(filename.endswith(".xml")):
        continue

    with open(filename, 'r') as inf:
        lines = [line.strip() for line in inf]
    inf.close()
     
    with open(filename, 'w') as outf:
        for line in lines:
            if re.match(matcher,line):
                line = re.sub(findLetter,replacementLetter,line)

            outf.write(line+"\n")
            
        
   
