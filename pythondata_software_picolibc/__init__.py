import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post345"
version_tuple = (1, 7, 4, 345)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post345")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post221"
data_version_tuple = (1, 7, 4, 221)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post221")
except ImportError:
    pass
data_git_hash = "ac37cb52519af888fe1255375c3ed95fe8ed4bcd"
data_git_describe = "1.7.4-221-gac37cb525"
data_git_msg = """\
commit ac37cb52519af888fe1255375c3ed95fe8ed4bcd
Author: Keith Packard <keithp@keithp.com>
Date:   Wed Jan 19 22:01:59 2022 -0800

    libm: Make long double cast explicit in frexpl
    
    Not sure this wouldn't be better as a long double constant, but I
    don't want to change the code.
    
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
