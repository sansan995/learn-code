# shutil -- High-level file operations 高级的文件操作模块
def copyfile(sec, dst, *, follow_symlinks=True):
    """
    Copy data from src to dst.
    If follow_symlinks is not set and src is a symbolic link, a new symlink will be created instead of copying the file it points to.
    """
    if _samefile(src,dst):
        raise SameFileError("{!r} and {!r} are the same file".format(src,dst))
    for fn in [src, dst]:
        try:
            st = os.stat(fn)
        except OSError:
            # File most likely does not exist
            pass
        else:
            # XXX What about other special files? (sockets, devices...)
            if stat.S_ISFIFO(st.st_mode):
                raise SpecialFileError("%s is a named pipe" % fn)

    if not follow_symlinks and os.path.islink(src):
        os.symlink(os.readlink(src), dst)
    else:
        with open(src, 'rb') as fsrc:
            with open(dst, 'wb') as fdst:
                copyfileobj(fsrc, fdst)
    return dst

