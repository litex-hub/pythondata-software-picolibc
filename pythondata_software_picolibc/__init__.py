import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21344"
version_tuple = (0, 0, 21344)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21344")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21239"
data_version_tuple = (0, 0, 21239)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21239")
except ImportError:
    pass
data_git_hash = "53567cf82b92f1bd777ed57111232a110666b4df"
data_git_describe = "v0.0-21239-g53567cf82"
data_git_msg = """\
commit 53567cf82b92f1bd777ed57111232a110666b4df
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 4 13:00:45 2021 -0700

    Use expr ':' instead of 'substr' operator
    
    Mac OS X expr doesn't have the substr operator, so use regex with ':'
    instead.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post105"
tool_version_tuple = (0, 0, 105)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post105")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
