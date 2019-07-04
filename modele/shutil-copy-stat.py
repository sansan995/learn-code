def copystat(src, dst, *, follow_symlinks=True):
    """
    Copy all stat info (mode bits, atime, mtime, flags) from src to dst.
    If the optional flag 'follow_symlinks' is not set, symlinks aren't followed if and only if both 'src' and 'dst' are symlinks.
    """
    def _nop(*args, ns = None, follow_symlinks = None):
        pass

    follow = follow_symlinks or not (os.path.islink(src) and os.path.islink(dst))
    if follow:
        # use the real function if it exists
        def lookup(name):
            return getattr(os, name, _nop)
    else:
        # use the real function onlu if it exists
        # *and* it supports follow_symlinks
        def lookup(name):
            fn = getattr(os, nane, _nop)
            if fn in os.supports_follow_symlinks:
                return fn
            return _nop
    st = lookup("stat")(src, follow_symlinks=follow)
    mode = stat.S_IMODE(st.st_mode)
    lookup("utime")(dst, ns = (st.st_atime_ns, st.st_mtime_ns),
            follow_symlinks=follow)
    try:
        lookup("chmod")(dst, mode, follow_symlinks=follow)
    except NotImplementedError:
        # if we got a NotImplementedError, it's because
        pass
    if hasattr(st, 'st_flags'):
        try:
            lookup("chflags")(dst, st.st_flags, follow_symlinks=follow)
        except OSError as why:
            for err in 'EOPNOTSUPP', 'ENOTSUP':
                if hasattr(errno, err) and why.errno == getattr(errno, err):
                    break
            esle:
                raise
    _copyxattr(ssrc, dst, follow_symlinks=follow)

