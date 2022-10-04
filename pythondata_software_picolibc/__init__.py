import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.8.post477"
version_tuple = (1, 7, 8, 477)
try:
    from packaging.version import Version as V
    pversion = V("1.7.8.post477")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.8.post335"
data_version_tuple = (1, 7, 8, 335)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.8.post335")
except ImportError:
    pass
data_git_hash = "4222758310860d2c65193429655943166c6be400"
data_git_describe = "1.7.8-335-g422275831"
data_git_msg = """\
commit 4222758310860d2c65193429655943166c6be400
Author: Michael Platings <michael.platings@arm.com>
Date:   Mon Oct 3 18:45:41 2022 +0100

    Add mbstate_t.h for compatibility with libc++
    
    tinystdio doesn't provide wide character functions like wcstold.
    Therefore libc++ must be built with wide character support disabled.
    When libc++ wide character support is disabled, it can't include
    wchar.h. However wchar.h is where mbstate_t is defined.
    Several types like std::fpos are defined in terms of mbstate_t so it's
    needed even if wide character support isn't. To get around this, libc++
    attempts to include the non-standard header mbstate_t.h. This change
    adds mbstate_t.h in the location that libc++ expects to find it.

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
