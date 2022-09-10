import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post173"
version_tuple = (1, 7, 8, 173)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post173")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post31"
data_version_tuple = (1, 7, 8, 31)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post31")
except ImportError:
    pass
data_git_hash = "569e2895a300237c5aae75c78c79daa74b09a11a"
data_git_describe = "1.7.8-31-g569e2895a"
data_git_msg = """\
commit 569e2895a300237c5aae75c78c79daa74b09a11a
Author: Keith Packard <keithp@keithp.com>
Date:   Fri Aug 26 16:39:18 2022 -0700

    .github: Test non-picoexit configuration
    
    Looks like there's a bug here, so let's test it and make sure it fails before
    adding a fix.
    
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
