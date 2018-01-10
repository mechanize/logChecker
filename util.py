from shutil import move
from os import remove


def stream_set_src(src: str, params: [str]):
    src_temp = '/'.join(src.split('/')[:-1] + ["temp.dat"])  # creates a tmp file at the same location as src
    f_src = open(src, 'w')
    f_temp = open(src_temp, 'w+')
    i = 0
    for line in f_src.readlines():
        if line.startswith("source:"):
            f_temp.write("source: " + params[i])
            i += 1
        else:
            f_temp.write(line)
    f_temp.close()
    f_src.close()
    remove(src)
    move(src_temp, src)







