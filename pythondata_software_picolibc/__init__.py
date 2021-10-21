import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "data")
src = "https://github.com/picolibc/picolibc"

# Module version
version_str = "0.0.post21411"
version_tuple = (0, 0, 21411)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post21411")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post21299"
data_version_tuple = (0, 0, 21299)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post21299")
except ImportError:
    pass
data_git_hash = "65c6534b82332f2c969882b960756410bda1474f"
data_git_describe = "v0.0-21299-g65c6534b8"
data_git_msg = """\
commit 65c6534b82332f2c969882b960756410bda1474f
Author: Yasushi SHOJI <yashi@spacecubics.com>
Date:   Wed Oct 20 19:57:17 2021 +0900

    test: semihost: i386: Depends on bios.bin
    
    i386 and x86_64 semihost targets need "bios.bin" to run the tests with
    QEMU but no tests depend on it.  bios.bin is "build_by_default: true"
    so that you have to tell meson to build the default targets before
    running tests, as you can see in .github/do-test:
    
        ninja && meson test
    
    Instead, make all tests depends on bios.bin, which is "bios_bin" in
    meson, so that meson can figure out what to build when it runs tests.
    Now, you can just do
    
        meson test -C builddir
           or
        meson test -C builddir malloc
    
    to build and run all tests without building the default targets
    first.
    
    Other arches don't need bios to run, so the "bios_bin" is an empty
    list except for Intel arches.
    
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
