import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21498"
version_tuple = (0, 0, 21498)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21498")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21386"
data_version_tuple = (0, 0, 21386)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21386")
except ImportError:
    pass
data_git_hash = "0e99e4a877ec4144c1a9d25f6eb01167812ff723"
data_git_describe = "v0.0-21386-g0e99e4a87"
data_git_msg = """\
commit 0e99e4a877ec4144c1a9d25f6eb01167812ff723
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Nov 1 23:39:05 2021 -0700

    .github: Clean up configuration options
    
    Stop using -Dnewlib-tinystdio.
    Remove some tabs
    Test obsolete double code.
    
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
