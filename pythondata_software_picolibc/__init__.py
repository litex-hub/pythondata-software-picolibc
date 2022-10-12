import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post142"
version_tuple = (1, 7, 9, 142)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post142")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post0"
data_version_tuple = (1, 7, 9, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post0")
except ImportError:
    pass
data_git_hash = "b92edfda8ac6853772d87cadaeeeaa21b78609b6"
data_git_describe = "1.7.9-0-gb92edfda8"
data_git_msg = """\
commit b92edfda8ac6853772d87cadaeeeaa21b78609b6
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 10 22:04:40 2022 -0700

    Version 1.7.9
    
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
