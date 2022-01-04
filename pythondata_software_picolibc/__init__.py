import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post143"
version_tuple = (1, 7, 4, 143)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post143")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post26"
data_version_tuple = (1, 7, 4, 26)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post26")
except ImportError:
    pass
data_git_hash = "32a0dfa218c13b1fa5c02465d00d42abc8d520bb"
data_git_describe = "1.7.4-26-g32a0dfa21"
data_git_msg = """\
commit 32a0dfa218c13b1fa5c02465d00d42abc8d520bb
Author: Vincent Palatin <vpalatin@rivosinc.com>
Date:   Mon Jan 3 18:41:01 2022 +0100

    Fix newlib version macros
    
    Newlib is defining the `__NEWLIB__` and `__NEWLIB_MINOR__` macros to export
    the library version.
    The current meson build in picolibc is exporting `_NEWLIB__` and
    `_NEWLIB_MINOR__` (with only one initial underscore).
    Align the picolibc behavior on the newlib one.
    
    This fixes the build of LLVM libcxx which is using those macros to pick
    the right headers in the following file:
    https://github.com/llvm/llvm-project/blob/main/libcxx/include/__support/newlib/xlocale.h

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
