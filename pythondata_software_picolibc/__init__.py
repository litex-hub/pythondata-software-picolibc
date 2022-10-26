import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.9.post169"
version_tuple = (1, 7, 9, 169)
try:
    from packaging.version import Version as V
    pversion = V("1.7.9.post169")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.9.post27"
data_version_tuple = (1, 7, 9, 27)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.9.post27")
except ImportError:
    pass
data_git_hash = "3cbe38c7914a305e1e7282b5ae4eab706b39db63"
data_git_describe = "1.7.9-27-g3cbe38c79"
data_git_msg = """\
commit 3cbe38c7914a305e1e7282b5ae4eab706b39db63
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Oct 24 09:12:51 2022 -0700

    Add -Werror=double-promotion to default warning set
    
    This will catch places where computations are forced to double instead
    of being done in float, often due to a constant lacking a trailing 'f'.
    
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
