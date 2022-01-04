import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "1.7.4.post142"
version_tuple = (1, 7, 4, 142)
try:
    from packaging.version import Version as V
    pversion = V("1.7.4.post142")
except ImportError:
    pass

# Data version info
data_version_str = "1.7.4.post25"
data_version_tuple = (1, 7, 4, 25)
try:
    from packaging.version import Version as V
    pdata_version = V("1.7.4.post25")
except ImportError:
    pass
data_git_hash = "00a614f794c12e0fb5105a7960fbdbcc13536e50"
data_git_describe = "1.7.4-25-g00a614f79"
data_git_msg = """\
commit 00a614f794c12e0fb5105a7960fbdbcc13536e50
Author: Keith Packard <keithp@keithp.com>
Date:   Mon Jan 3 13:44:45 2022 -0800

    Allow cross-compile files to override has_link_defsym and has_link_alias
    
    When building for rv32imacfdc with clang, we link with ld, which
    requires an additional -melf32lriscv linker parameter. However, meson
    refuses to pass that to the compiler when calling
    compiler.has_link_argument to check for --defsym or --alias linker
    parameters. This causes the options needed to link float-only or
    int-only printf during testing to not be set, making the float-only
    tests fail.
    
    Work around this by allowing the cross-compile file to set values for
    these two variables and skip auto-detecting them.
    
    Signed-off-by: Keith Packard <keithp@keithp.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_software_picolibc."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_software_picolibc".format(f))
    return fn
