import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post480"
version_tuple = (1, 7, 8, 480)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post480")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post338"
data_version_tuple = (1, 7, 8, 338)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post338")
except ImportError:
    pass
data_git_hash = "7beed395a06b5a977dfa4cdcfc13ee4fe8685a71"
data_git_describe = "1.7.8-338-g7beed395a"
data_git_msg = """\
commit 7beed395a06b5a977dfa4cdcfc13ee4fe8685a71
Author: Keith Packard <keithp@keithp.com>
Date:   Tue Oct 4 17:41:43 2022 -0700

    .github: Test x86_64 and multi-lib x86 builds
    
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
