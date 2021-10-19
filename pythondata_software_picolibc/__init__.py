import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21400"
version_tuple = (0, 0, 21400)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21400")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21288"
data_version_tuple = (0, 0, 21288)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21288")
except ImportError:
    pass
data_git_hash = "98160b3b9b8afe955765e14636de7286ff480d15"
data_git_describe = "v0.0-21288-g98160b3b9"
data_git_msg = """\
commit 98160b3b9b8afe955765e14636de7286ff480d15
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Oct 13 15:20:41 2021 -0700

    Avoid creating so many intermediate libraries
    
    Instead of creating an intermediate library for every subdirectory in
    the tree, create lists of files that are grouped in the higher level
    library. This simplifies things quite a bit and should make builds run
    faster.
    
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
