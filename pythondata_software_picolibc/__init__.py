import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post181"
version_tuple = (1, 7, 9, 181)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post181")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post39"
data_version_tuple = (1, 7, 9, 39)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post39")
except ImportError:
    pass
data_git_hash = "f165dc22f1f67e3e8bdc8edf750ff7dc596de2ff"
data_git_describe = "1.7.9-39-gf165dc22f"
data_git_msg = """\
commit f165dc22f1f67e3e8bdc8edf750ff7dc596de2ff
Author: Keith Packard <keithp@keithp.com>
Date:   Sat Nov 5 19:30:51 2022 -0700

    Switch read/write to posix types
    
    Remove legacy cygwin hacks which set the buffer size and return value
    for read and write to int, switch them to the correct POSIX types,
    size_t for buffer size and ssize_t for the return value.
    
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
