import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post356"
version_tuple = (1, 7, 4, 356)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post356")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post232"
data_version_tuple = (1, 7, 4, 232)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post232")
except ImportError:
    pass
data_git_hash = "f80f774c3f263c75219d2e90820043369b0b0b34"
data_git_describe = "1.7.4-232-gf80f774c3"
data_git_msg = """\
commit f80f774c3f263c75219d2e90820043369b0b0b34
Author: Keith Packard <keithp@keithp.com>
Date:   Sun Feb 6 20:09:04 2022 -0800

    .github: Add build tests for PowerPC
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
