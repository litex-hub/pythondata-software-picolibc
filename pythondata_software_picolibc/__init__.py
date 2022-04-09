import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post138"
version_tuple = (1, 7, 6, 138)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post138")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post12"
data_version_tuple = (1, 7, 6, 12)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post12")
except ImportError:
    pass
data_git_hash = "48527f8f7eb543094a6d4c6f6571b639cd7a1453"
data_git_describe = "1.7.6-12-g48527f8f7"
data_git_msg = """\
commit 48527f8f7eb543094a6d4c6f6571b639cd7a1453
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Apr 7 13:16:36 2022 -0700

    scripts: Re-add -nostdlib to c configurations for meson 0.53.2 support
    
    Meson 0.53.2 doesn't use any cflags when doing basic compiler tests,
    so we have to add -nostdlib to the compiler configuration it self or
    early compiler tests while running meson fail.
    
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
