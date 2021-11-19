import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21539"
version_tuple = (0, 0, 21539)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21539")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21427"
data_version_tuple = (0, 0, 21427)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21427")
except ImportError:
    pass
data_git_hash = "0008930811ff6830aa1117068fa9a49fbe0176c4"
data_git_describe = "v0.0-21427-g000893081"
data_git_msg = """\
commit 0008930811ff6830aa1117068fa9a49fbe0176c4
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Nov 18 22:12:26 2021 -0800

    Version 1.7.4
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

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
