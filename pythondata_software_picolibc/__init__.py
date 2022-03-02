import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post499"
version_tuple = (1, 7, 4, 499)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post499")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post373"
data_version_tuple = (1, 7, 4, 373)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post373")
except ImportError:
    pass
data_git_hash = "8359908e586e838cc1562df36e784fce489c058d"
data_git_describe = "1.7.4-373-g8359908e5"
data_git_msg = """\
commit 8359908e586e838cc1562df36e784fce489c058d
Author: Keith Packard <keithp@keithp.com>
Date:   Tue Mar 1 17:32:24 2022 -0800

    Add '-Dbuild-type-subdir' to meson and '--picolibc-buildtype' to gcc
    
    These two options let picolibc be built with multiple configuration options and
    installed in the same target directory. At application compile time, the build type
    can be selected via the GCC --picolibc-buildtype option which selects which target
    path to use for headers and binaries.
    
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
