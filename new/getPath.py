import os
import linecache
import codecs
import time
import re
import json

file_path = './media/'
nameList = {}
for i in os.walk(file_path):
    files = i[2]
    f = open('./result.json', 'w', encoding = 'utf-8')    
    for j in range(len(files)):
        print(files[j])
        author = files[j].split('_')[2].split('.')[0]
        cipai = files[j].split('_')[0]
        content = files[j].split('_')[1]
        if cipai in nameList: 
            nameList[cipai].append({
                "author": author,
                content: files[j]
            })
        else:
            nameList[cipai]=[{
                "author": author,
                content: files[j]
            }]

    json.dump(nameList, f, ensure_ascii = False, indent=4)
    f.close()
    
