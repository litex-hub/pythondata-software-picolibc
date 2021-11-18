import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21532"
version_tuple = (0, 0, 21532)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21532")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21420"
data_version_tuple = (0, 0, 21420)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21420")
except ImportError:
    pass
data_git_hash = "1fcf6015d45f5f0101e8a3cb64605c04430c7428"
data_git_describe = "v0.0-21420-g1fcf6015d"
data_git_msg = """\
commit 1fcf6015d45f5f0101e8a3cb64605c04430c7428
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Nov 18 10:35:36 2021 -0800

    doc: Provide command line examples for linker script usage
    
    Explain how custom linker scripts can override picolibc built-in
    linker scripts by using the -T option on the command line.
    
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
