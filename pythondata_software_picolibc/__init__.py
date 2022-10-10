import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post526"
version_tuple = (1, 7, 8, 526)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post526")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post384"
data_version_tuple = (1, 7, 8, 384)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post384")
except ImportError:
    pass
data_git_hash = "3e7c697478ecd4575056d7373ed947ded1eddf8e"
data_git_describe = "1.7.8-384-g3e7c69747"
data_git_msg = """\
commit 3e7c697478ecd4575056d7373ed947ded1eddf8e
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Oct 5 10:14:36 2022 -0700

    x86: Build only one bios.bin version. Use -nostdlib
    
    Instead of creating per-target bios.bin files, each of which is
    identical, create just one.
    
    Use -nostdlib instead of -nostartfiles to avoid requiring libc and libgcc
    
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
