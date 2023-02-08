import fsystem, console

def run(filepath):
    content = fsystem.rF(filepath)
    if type(content) == str:
        content_split = content.split(';')
    else:
        console.write('EXEC: could not run file! ' + filepath)
        return -1
    for i in range(len(content_split)):
        if content_split[i][0] == '#':
            continue
        elif content_split[i][0] == '>':
            console.write(content_split[i][1:])
    
