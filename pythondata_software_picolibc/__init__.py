import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post449"
version_tuple = (1, 7, 8, 449)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post449")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post307"
data_version_tuple = (1, 7, 8, 307)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post307")
except ImportError:
    pass
data_git_hash = "95b1921f928ee5e373419dcf6a9706e1e6049228"
data_git_describe = "1.7.8-307-g95b1921f9"
data_git_msg = """\
commit 95b1921f928ee5e373419dcf6a9706e1e6049228
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Sep 12 16:21:42 2022 +0100

    reent: Eliminate reent.h and sys/reent.h
    
    Clean up the last few files using these headers, then
    remove them entirely.
    
    This removes a bunch of unused powerpc code as that
    also used reent, but gcc no longer supports the SPE option
    needed to use any of it.
    
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
