import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.5.post137"
version_tuple = (1, 7, 5, 137)
try:
    from packaging.version import Version as V
    pversion = V("1.7.5.post137")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.5.post11"
data_version_tuple = (1, 7, 5, 11)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.5.post11")
except ImportError:
    pass
data_git_hash = "bad9f5b1b3d50cdcf80281b4f3a66a7232531f11"
data_git_describe = "1.7.5-11-gbad9f5b1b"
data_git_msg = """\
commit bad9f5b1b3d50cdcf80281b4f3a66a7232531f11
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Mar 23 13:23:22 2022 -0700

    arm/risc-v: Move FAST_FMA defines to installed machine/math.h files
    
    This makes the inline fma functions available for applications using
    picolibc, not just for internal use. At the same time, add leading _
    to the HAVE_FAST_FMA macros so that they don't potentially conflict
    with application symbols.
    
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
