import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post497"
version_tuple = (1, 7, 4, 497)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post497")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post371"
data_version_tuple = (1, 7, 4, 371)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post371")
except ImportError:
    pass
data_git_hash = "d980f357f4958c4caf4facaca3317fc81ebc6ecb"
data_git_describe = "1.7.4-371-gd980f357f"
data_git_msg = """\
commit d980f357f4958c4caf4facaca3317fc81ebc6ecb
Author: Keith Packard <keithp@keithp.com>
Date:   Fri Feb 18 21:57:50 2022 -0800

    scripts: Switch m68k sample to use do-configure script
    
    There's no reason to have a custom script for this target. At the same
    time, switch from building 68000 code to 68020 as that seems easier to
    link.
    
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
