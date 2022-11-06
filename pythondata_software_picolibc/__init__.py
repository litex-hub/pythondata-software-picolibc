import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post180"
version_tuple = (1, 7, 9, 180)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post180")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post38"
data_version_tuple = (1, 7, 9, 38)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post38")
except ImportError:
    pass
data_git_hash = "07e942e8446cf3d47f9fd3b2ec33c1d39207b978"
data_git_describe = "1.7.9-38-g07e942e84"
data_git_msg = """\
commit 07e942e8446cf3d47f9fd3b2ec33c1d39207b978
Author: Keith Packard <keithp@keithp.com>
Date:   Fri Nov 4 16:38:35 2022 -0700

    test: Switch from unlink to remove
    
    Use the ISO C API instead of the POSIX one to test
    our internal implementation.
    
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
