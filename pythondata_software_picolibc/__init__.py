import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.7.post150"
version_tuple = (1, 7, 7, 150)
try:
    from packaging.version import Version as V
    pversion = V("1.7.7.post150")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.7.post8"
data_version_tuple = (1, 7, 7, 8)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.7.post8")
except ImportError:
    pass
data_git_hash = "7a3c2973a5cac20b01a9dd683198147d71547460"
data_git_describe = "1.7.7-8-g7a3c2973a"
data_git_msg = """\
commit 7a3c2973a5cac20b01a9dd683198147d71547460
Author: Keith Packard <keithp@keithp.com>
Date:   Sun Jun 19 11:31:52 2022 -0700

    .github: Test all available cmake configurations
    
    Make sure the library is built correctly in all modes.
    
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
