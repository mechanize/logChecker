from os import listdir


def parse_package(tool:str, path:str) -> dict:
    files = listdir(path)
    return {
        'monpoly': {
            'formula':  path + '/' + [e for e in files if e.endswith(".formula")][0],
            'signaure': path + '/' + [e for e in files if e.endswith(".sign")][0],
            'log':      path + '/' + [e for e in files if e.endswith(".log")][0],
        },
        'stream': {
            'script':   path + '/' + [e for e in files if e.endswith(".script")][0],
            'logs':     [path + '/' + e for e in files if e.endswith(".dat")].sort()
        }
    }.get(tool)


