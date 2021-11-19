import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21537"
version_tuple = (0, 0, 21537)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21537")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21425"
data_version_tuple = (0, 0, 21425)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21425")
except ImportError:
    pass
data_git_hash = "c5000518c8c258389673701a3ad2476217056e68"
data_git_describe = "v0.0-21425-gc5000518c"
data_git_msg = """\
commit c5000518c8c258389673701a3ad2476217056e68
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Nov 18 22:11:28 2021 -0800

    Update COPYING.picolibc
    
    Some files in hello-world changed names.
    
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
