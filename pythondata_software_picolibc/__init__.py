import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.6.post130"
version_tuple = (1, 7, 6, 130)
try:
    from packaging.version import Version as V
    pversion = V("1.7.6.post130")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.6.post4"
data_version_tuple = (1, 7, 6, 4)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.6.post4")
except ImportError:
    pass
data_git_hash = "b3a735784c3f9fe45721f7caea88fccee16ea922"
data_git_describe = "1.7.6-4-gb3a735784"
data_git_msg = """\
commit b3a735784c3f9fe45721f7caea88fccee16ea922
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Mar 28 11:32:16 2022 -0700

    test/semihost: Add test for gettimeofday
    
    Make sure this function returns reasonable values:
    
     * After september 2020 (unix time 1,600,000,000)
     * Values never decrease
     * New values are within 1000 seconds of original value
     * Eventually changes after no more than 1000 iterations
    
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
