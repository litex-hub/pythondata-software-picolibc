import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21432"
version_tuple = (0, 0, 21432)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21432")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21320"
data_version_tuple = (0, 0, 21320)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21320")
except ImportError:
    pass
data_git_hash = "daa2e04a3c65555ae45c68d6601a5f571e50eac2"
data_git_describe = "v0.0-21320-gdaa2e04a3"
data_git_msg = """\
commit daa2e04a3c65555ae45c68d6601a5f571e50eac2
Author: Keith Packard <keithp@keithp.com>
Date:   Tue Oct 26 16:43:37 2021 -0700

    test: Add memset/bzero test
    
    Also tests ARM aeabi versions.
    
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
