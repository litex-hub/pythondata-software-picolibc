import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21352"
version_tuple = (0, 0, 21352)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21352")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21240"
data_version_tuple = (0, 0, 21240)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21240")
except ImportError:
    pass
data_git_hash = "4b4a69f42f2e6fa5d6e44607adefe10f38d1b51a"
data_git_describe = "v0.0-21240-g4b4a69f42"
data_git_msg = """\
commit 4b4a69f42f2e6fa5d6e44607adefe10f38d1b51a
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Wed Oct 6 13:29:33 2021 +0900

    meson.build: Remove unused POSIX_CONSOLE define from picolibc.h
    
    The definition POSIX_CONSOLE in picolibc.h is not used at all in the
    tree.  In fact, it's never been used since it's introduced in
    the commit 91b5c92e.
    
    The build time option 'posix-console' _is_ in use for checking against
    tinystdio and in newlib/libc/tinystdio/meson.build to enable building
    posixiob.c.  The option itself is, of course, unchanged.
    
    Signed-off-by: Yasushi SHOJI <yashi@spacecubics.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
