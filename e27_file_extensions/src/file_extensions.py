#!/usr/bin/env python3

def file_extensions(filename=r"e27_file_extensions\src\filenames.txt"):
    fileList = [] # files with no extension
    extDict = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line[:-1]
            sl = line.split('.')
            if len(sl) > 1:
                ext = sl[-1]
                if ext in extDict:
                    extDict[ext].append(line)
                else:
                    extDict[ext] = [line]
            else:
                fileList.append(line)    
    return (fileList, extDict)

def main():
    list, dict = file_extensions(r"e27_file_extensions\src\filenames.txt")
    print(len(list), "files with no extension")
    for exten in sorted(dict):
        print(exten, len(dict[exten]))

if __name__ == "__main__":
    main()
