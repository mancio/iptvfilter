def replacegroup(line, text):
    start = line.find('group-title="')
    end = line.find('",')
    return line.replace(line[start + 13:end], text)  # replace the string between two delimiters
