import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21372"
version_tuple = (0, 0, 21372)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21372")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21260"
data_version_tuple = (0, 0, 21260)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21260")
except ImportError:
    pass
data_git_hash = "99c17dcf2e387ecd79a76ba409031a7ae119ce98"
data_git_describe = "v0.0-21260-g99c17dcf2"
data_git_msg = """\
commit 99c17dcf2e387ecd79a76ba409031a7ae119ce98
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Tue Oct 12 07:55:11 2021 +0900

    scripts: Fix unclosed string literal typo
    
    Need a closing '.
    
    Signed-off-by: Yasushi SHOJI <yashi@spacecubics.com>

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
