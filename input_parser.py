
# logChecker.py -m monpoly.sign monpoly.formula monpoly.log -s stream.script stream1.dat stream2.dat
# logChecker.py -m monpoly.sign monpoly.formula monpoly.log -s stream.script \streamlogs


def get_param(inp: [str]) -> dict:
    param = {}
    stdin = [("-" + e).split(" ") for e in (" ".join(inp)).strip().split("-")]

    for t in stdin:
        param.update({
            '-m': {
                'monpoly': {
                    'signature': [e for e in t[1:] if e.split(".")[-1] == "sign"][0],
                    'formula': [e for e in t[1:] if e.split(".")[-1] == "formula"][0],
                    'log': [e for e in t[1:] if e.split(".")[-1] == "log"][0]
                }
                },
            '-s': {
                'stream': {
                    'script': [e for e in t[1:] if e.split(".")[-1] == "script"][0],
                    'logs': [e for e in t[1:] if e.split(".")[-1] == "dat"]
                }
            }
        }).get(t[0])
    return param
