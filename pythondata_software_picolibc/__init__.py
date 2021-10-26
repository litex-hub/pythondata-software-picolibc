import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21427"
version_tuple = (0, 0, 21427)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21427")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21315"
data_version_tuple = (0, 0, 21315)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21315")
except ImportError:
    pass
data_git_hash = "028e4c9ba654e0c0dfd62f1e9139ff159fdd69a4"
data_git_describe = "v0.0-21315-g028e4c9ba"
data_git_msg = """\
commit 028e4c9ba654e0c0dfd62f1e9139ff159fdd69a4
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 25 14:40:56 2021 -0700

    scripts: Use canonical 'ppc64' cpu family for powerpc64le sample
    
    ppc64 is what meson wants to see, so lets just use that directly.
    
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
