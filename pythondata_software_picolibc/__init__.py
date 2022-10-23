import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post162"
version_tuple = (1, 7, 9, 162)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post162")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post20"
data_version_tuple = (1, 7, 9, 20)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post20")
except ImportError:
    pass
data_git_hash = "c2eaa1717f0681de12dc8012bd261dd0ddcf0ade"
data_git_describe = "1.7.9-20-gc2eaa1717"
data_git_msg = """\
commit c2eaa1717f0681de12dc8012bd261dd0ddcf0ade
Author: Keith Packard <keithp@keithp.com>
Date:   Sat Oct 22 13:15:43 2022 -0700

    test: Add 64-bit strtol tests as well and ':' termination test
    
    Strtol was mis-parsing ipv6 addrs as the separating ':' was not
    correctly detected as the end of a hex number. Add a test for this
    case.
    
    Also replicate the overflow tests for 64-bit longs.
    
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
