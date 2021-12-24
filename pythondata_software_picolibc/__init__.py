import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post138"
version_tuple = (1, 7, 4, 138)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post138")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post21"
data_version_tuple = (1, 7, 4, 21)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post21")
except ImportError:
    pass
data_git_hash = "e83996113acdaebe1429a2ea82d59c9807651a6c"
data_git_describe = "1.7.4-21-ge83996113"
data_git_msg = """\
commit e83996113acdaebe1429a2ea82d59c9807651a6c
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Dec 23 17:06:29 2021 -0800

    tinystdio: Pull in changes to the ryu code
    
    This brings the ryu code in tinystdio up to
    commit 150d0c87830756d34e76c42f7f33f811d89903a8
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
