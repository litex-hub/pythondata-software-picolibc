import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post156"
version_tuple = (1, 7, 9, 156)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post156")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post14"
data_version_tuple = (1, 7, 9, 14)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post14")
except ImportError:
    pass
data_git_hash = "c32f242ea9e636c48b0189d0f4c4f127d2263dd0"
data_git_describe = "1.7.9-14-gc32f242ea"
data_git_msg = """\
commit c32f242ea9e636c48b0189d0f4c4f127d2263dd0
Author: David Green <david.green@arm.com>
Date:   Wed Oct 19 21:26:16 2022 +0100

    [ARM] Fix FPSCR initial state for Arm8.1-M low overhead loops.
    
    The Arm8.1-m architecture added Low Overhead Loops and tail predication,
    controlled by the LTPSIZE bits of FPSCR. Unfortunately 0 is an invalid
    value, with values other than 0x4 causing an LE instructions to throw a
    UsageFault. This alters the initial reset value in _start to 0x40000 to
    ensure it is initialized correctly.

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
