import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21429"
version_tuple = (0, 0, 21429)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21429")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21317"
data_version_tuple = (0, 0, 21317)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21317")
except ImportError:
    pass
data_git_hash = "b9a0142cbf005c874f639fe48e0f57e0f09480b3"
data_git_describe = "v0.0-21317-gb9a0142cb"
data_git_msg = """\
commit b9a0142cbf005c874f639fe48e0f57e0f09480b3
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Wed Oct 27 15:52:04 2021 +0900

    libc: Remove #ifdef check before #undef
    
    C Standards state that
    
       It is ignored if the specified identifier is not currently defined
       as a macro name.
    
    So we don't need to check with #ifdef before #undef.  It seems that
    old compilers might error out, but we specify "c18" in the
    meson.build, anyway.
    
    newlib/libc/reent/getreent.c has the line "#undef __getreent" but it's
    not added by the recent commit c2c593afa60b64bff, so this commit
    doesn't change it.
    
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
