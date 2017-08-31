from conans import ConanFile, tools
from conans.errors import ConanException
from conans.model.version import Version
import os, shutil


class IdealcouscousConan(ConanFile):
    name = "IdealCouscous"
    version = "devel"
    license = "Apache-2.0"
    url = "https://github.com/maxis11/ideal-couscous"
    settings = "os", "compiler", "build_type", "arch"
    #generators = "qbs"
    description = "compile-time reflection header-only library for c++1z"
    build_policy = "missing"
    
    def configure(self):
        v = Version(str(self.settings.compiler.version))
        if self.settings.compiler == "gcc" and v < "7.0":
            raise ConanException("GCC >= 7.0 is required")
        if self.settings.compiler == "clang" and v < "5.0":
            raise ConanException("clang >= 5.0 is required")
        

    def source(self):
        tools.download("https://github.com/maxis11/ideal-couscous/archive/master.tar.gz", "ic.tar.gz")
        tools.untargz("ic.tar.gz")
        os.unlink("ic.tar.gz")
        shutil.move("ideal-couscous-master", "IdealCouscous")
        

    def package(self):
        self.copy("*.hpp", dst="include", src="IdealCouscous/src")
