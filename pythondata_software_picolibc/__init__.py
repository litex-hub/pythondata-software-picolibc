import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21530"
version_tuple = (0, 0, 21530)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21530")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21418"
data_version_tuple = (0, 0, 21418)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21418")
except ImportError:
    pass
data_git_hash = "da94a0d3a28a1d5d75ca00b2de182f4f0db391d2"
data_git_describe = "v0.0-21418-gda94a0d3a"
data_git_msg = """\
commit da94a0d3a28a1d5d75ca00b2de182f4f0db391d2
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Nov 15 22:02:20 2021 -0800

    math: Use current rounding mode directly for sqrt
    
    This queries the current rounding mode rather than using computations
    to figure out what it is. For hardware without rounding modes, all of this
    gets short-circuited.
    
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
