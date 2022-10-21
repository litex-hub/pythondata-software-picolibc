import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post155"
version_tuple = (1, 7, 9, 155)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post155")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post13"
data_version_tuple = (1, 7, 9, 13)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post13")
except ImportError:
    pass
data_git_hash = "e4714f3bef99de28bd17d3e43c1cd2bb6dc41994"
data_git_describe = "1.7.9-13-ge4714f3be"
data_git_msg = """\
commit e4714f3bef99de28bd17d3e43c1cd2bb6dc41994
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Oct 20 10:52:16 2022 -0700

    libc/stdlib: Implement locale-free versions of strto* functions
    
    Use code from tinystdio scanf to build small versions of these
    functions that don't depend on the locale code for 'isspace'.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
