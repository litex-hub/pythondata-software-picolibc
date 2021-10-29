import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21452"
version_tuple = (0, 0, 21452)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21452")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21340"
data_version_tuple = (0, 0, 21340)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21340")
except ImportError:
    pass
data_git_hash = "59075484682d63f4589eb49afe59e89b27e89115"
data_git_describe = "v0.0-21340-g590754846"
data_git_msg = """\
commit 59075484682d63f4589eb49afe59e89b27e89115
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Oct 28 11:55:30 2021 -0700

    Update COPYING.picolibc
    
    Add musl test suite
    Rename arm-specific files
    Add more POSIX bits
    
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
