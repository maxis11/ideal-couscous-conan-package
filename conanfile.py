from conans import ConanFile, CMake, tools
import os, shutil


class IdealcouscousConan(ConanFile):
    name = "IdealCouscous"
    version = "0.0.4-alpha"
    license = "Apache-2.0"
    url = "https://github.com/maxis11/ideal-couscous"
    settings = "os", "compiler", "build_type", "arch"
    generators = "qbs"
    description = "compile-time reflection header-only library for c++1z"
    build_policy = "missing"
    
    def configure():
        if self.settings.compiler == "gcc" and self.settings.compiler.version < "7.0":
            raise ConanException("GCC >= 7.0 is required")
        if self.settings.compiler == "clang" and self.settings.compiler.version < "5.0":
            raise ConanException("clang >= 5.0 is required")
        

    def source(self):
        tools.download("https://github.com/maxis11/ideal-couscous/archive/v0.0.4-alpha.tar.gz", "ic.zip")
        tools.untargz("ic.zip")
        os.unlink("ic.zip")
        shutil.move("ideal-couscous-0.0.4-alpha", "IdealCouscous")
        

    def package(self):
        self.copy("*.hpp", dst="include", src="IdealCouscous/src")
