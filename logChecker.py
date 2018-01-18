import input_parser
import comparator
import subprocess
import util
import sys

monpoly = ""
stream = ""
stream_config = ""

inp = sys.argv[1:]

param = input_parser.get_param(inp)
for tool, paths in param:
    if tool == 'monpoly':
        popen = subprocess.Popen(monpoly + " -s " + paths.get('signature') + " -f" + paths.get('formula') +
                                 " -l" + paths.get('log') + " > m_out", stdout=True, stderr=False)
        popen.communicate()
        param.get('monpoly').update({'out': 'm_out'})
    elif tool == 'stream':
        s_param = paths.get('stream')
        util.stream_set_src(paths.get('script'), paths.get('logs'))
        dest = util.stream_get_dest(paths.get('script'))
        popen = subprocess.Popen(stream + " -c " + stream_config + s_param.get('script'))
        popen.communicate()
        param.get('stream').update({'out': dest})
comparator.compare(monpoly=param.get('monpoly').get('out'),
                   stream=param.get('stream').get('out'))

