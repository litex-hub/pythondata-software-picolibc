import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21454"
version_tuple = (0, 0, 21454)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21454")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21342"
data_version_tuple = (0, 0, 21342)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21342")
except ImportError:
    pass
data_git_hash = "3fbd7c9979b6cfd073884c874f1b7df8701e1f65"
data_git_describe = "v0.0-21342-g3fbd7c997"
data_git_msg = """\
commit 3fbd7c9979b6cfd073884c874f1b7df8701e1f65
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Sat Oct 30 01:44:20 2021 +0900

    meson.build: Replace explicit warning level with the core option
    
    We can specify a warning level in compiler independent way with the
    option 'warning_level'.  This option can also be specified at the
    command line with -Dwarning_level=.  The default value for
    warning_level is 1.
    
    For GCC and Clang, warning level 1 and 2 are:
    
        level 1: -Wall -Winvalid-pch
        level 2: -Wall -Winvalid-pch -Wextra
    
    So, it's the same as we used to have.
    
    ref: https://mesonbuild.com/Builtin-options.html#core-options
    
    Signed-off-by: Yasushi SHOJI <yashi@spacecubics.com>

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
