import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21371"
version_tuple = (0, 0, 21371)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21371")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21259"
data_version_tuple = (0, 0, 21259)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21259")
except ImportError:
    pass
data_git_hash = "7aa4c6803aca089dcbf8f9dfbb853b2691cfd520"
data_git_describe = "v0.0-21259-g7aa4c6803"
data_git_msg = """\
commit 7aa4c6803aca089dcbf8f9dfbb853b2691cfd520
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 11 09:27:53 2021 -0700

    test: Make sure strchr and strrchr handle weird params correctly
    
    strchr and strrchr are defined to take 'int' parameters for the needle
    value (presumably due to legacy pre-ANSI C definitions). Internally,
    they need to ignore everything above the low 8 bits. Make sure they do
    by checking various combinations of values.
    
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
