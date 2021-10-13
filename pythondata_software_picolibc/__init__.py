import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21380"
version_tuple = (0, 0, 21380)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21380")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21268"
data_version_tuple = (0, 0, 21268)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21268")
except ImportError:
    pass
data_git_hash = "6ce563e9245c4992d2176374af9b93065636166e"
data_git_describe = "v0.0-21268-g6ce563e92"
data_git_msg = """\
commit 6ce563e9245c4992d2176374af9b93065636166e
Author: Keith Packard <keithp@keithp.com>
Date:   Tue Oct 12 22:47:56 2021 -0700

    scripts: Add powerpc64le cross-compile scripts
    
    These use the linux-gnu compiler to build standalone libraries,
    However, picolibc does not have support for bare-metal powerpc yet.
    
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
