import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21534"
version_tuple = (0, 0, 21534)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21534")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21422"
data_version_tuple = (0, 0, 21422)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21422")
except ImportError:
    pass
data_git_hash = "654f5c0a5def9fa433efd0567a9395496dfaf103"
data_git_describe = "v0.0-21422-g654f5c0a5"
data_git_msg = """\
commit 654f5c0a5def9fa433efd0567a9395496dfaf103
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Nov 18 17:32:23 2021 -0800

    Move Documentation in README.me above release notes
    
    There are now a lot of release notes, which makes finding the set of
    documentation links harder.
    
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
