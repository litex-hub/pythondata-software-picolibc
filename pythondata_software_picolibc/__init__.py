import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post136"
version_tuple = (1, 7, 6, 136)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post136")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post10"
data_version_tuple = (1, 7, 6, 10)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post10")
except ImportError:
    pass
data_git_hash = "9120e6333f88f5bdefad013b24ad8ecfd4e3a5f1"
data_git_describe = "1.7.6-10-g9120e6333"
data_git_msg = """\
commit 9120e6333f88f5bdefad013b24ad8ecfd4e3a5f1
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Apr 4 12:11:19 2022 -0700

    Require newlib-multithread and newlib-retargetable-locking to match
    
    I'm still not sure why there are two options, but mixing values seems
    like a bad idea as they both control whether the library performs
    locking or not.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
