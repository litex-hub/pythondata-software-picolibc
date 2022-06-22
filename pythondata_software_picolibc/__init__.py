import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.7.post155"
version_tuple = (1, 7, 7, 155)
try:
    from packaging.version import Version as V
    pversion = V("1.7.7.post155")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.7.post13"
data_version_tuple = (1, 7, 7, 13)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.7.post13")
except ImportError:
    pass
data_git_hash = "bbcbb51c17bc9afbae9e1683ac4c7b3e740bf2c8"
data_git_describe = "1.7.7-13-gbbcbb51c1"
data_git_msg = """\
commit bbcbb51c17bc9afbae9e1683ac4c7b3e740bf2c8
Author: Keith Packard <keithp@keithp.com>
Date:   Tue Jun 21 14:09:49 2022 -0700

    test: Add test for malloc(PTRDIFF_MAX)
    
    This can have a different failure mode than malloc(SIZE_MAX), so test
    it explicitly
    
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
