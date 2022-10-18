import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post149"
version_tuple = (1, 7, 9, 149)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post149")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post7"
data_version_tuple = (1, 7, 9, 7)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post7")
except ImportError:
    pass
data_git_hash = "975d41b7fdf044ba917fa836f77df786c205d4e3"
data_git_describe = "1.7.9-7-g975d41b7f"
data_git_msg = """\
commit 975d41b7fdf044ba917fa836f77df786c205d4e3
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 17 13:51:00 2022 -0700

    picolibc/arc: Add _set_tls support for ARC targets
    
    Use the __ARC_GLS_REGNO__ define for this code. This requires
    that the configuration specify -mtp-regno= correctly.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
