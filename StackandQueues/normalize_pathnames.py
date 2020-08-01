
def normalizePathname(pathname):
    if not pathname:
        raise ValueError("Path is empty !!")
    
    ## if it is absolute path then it will start with '/' so handling it
    path_names = []
    if pathname[0] == "/":
        path_names.append('/')

    tokens = pathname.split('/')

    for token in tokens:
        if token in ["", "."]:
            continue
        elif token == "..":
            if not path_names or path_names[-1] == "..":
                path_names.append(token)
            else:
                if path_names[-1] =="/":
                    raise ValueError("Path error")
                path_names.pop()
        else: ## must be a name
            path_names.append(token)
    
    answer = "/".join(path_names)
    return answer[answer.startswith('//'):]



pathname = 'sc//./../tc/awk/././'
required_path = normalizePathname(pathname)
print(required_path)