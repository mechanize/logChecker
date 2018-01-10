import input_parser
import subprocess
import util

monpoly = ""
stream = ""
stream_config = ""

# TODO:parse param string @param inp
inp = ""

param = input_parser.get_param(inp)
for tool, paths in param:
    if tool == 'monpoly':
        popen = subprocess.Popen(monpoly + " -s " + paths.get('signature') + " -f" + paths.get('formula') +
                                 " -l" + paths.get('log'), stdout=True, stderr=False)
        m_out = popen.communicate()
    elif tool == 'stream':
        s_param = paths.get('stream')
        util.stream_set_src(paths.get('script'), paths.get('logs'))
        popen = subprocess.Popen(stream + " -c " + stream_config + s_param.get('script'))
        s_out = popen.communicate()
