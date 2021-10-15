import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21392"
version_tuple = (0, 0, 21392)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21392")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21280"
data_version_tuple = (0, 0, 21280)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21280")
except ImportError:
    pass
data_git_hash = "fa6eba747f3593fc75caa79b76d230fbce106bc6"
data_git_describe = "v0.0-21280-gfa6eba747"
data_git_msg = """\
commit fa6eba747f3593fc75caa79b76d230fbce106bc6
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Oct 14 09:36:49 2021 -0700

    Rename amd64 stuff to x86_64
    
    This makes this architecture have a consistent name in the system.
    
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
