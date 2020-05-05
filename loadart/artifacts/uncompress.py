import shutil

def uncompress(filename, target_dir):
    shutil.unpack_archive(filename, target_dir)
