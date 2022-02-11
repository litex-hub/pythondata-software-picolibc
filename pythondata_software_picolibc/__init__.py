import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post358"
version_tuple = (1, 7, 4, 358)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post358")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post234"
data_version_tuple = (1, 7, 4, 234)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post234")
except ImportError:
    pass
data_git_hash = "d79f1d606a71147ef8c1ed36594b5ed6a2e96122"
data_git_describe = "1.7.4-234-gd79f1d606"
data_git_msg = """\
commit d79f1d606a71147ef8c1ed36594b5ed6a2e96122
Author: Keith Packard <keithp@keithp.com>
Date:   Thu Feb 10 15:53:40 2022 -0800

    Update build status link to use new 'Linux' workflow
    
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
