################################################################################
#
# Copyright (c) 2009 - 2011 Malek Hadj-Ali
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holders nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#
#
# Alternatively, the contents of this file may be used under the terms of the
# GNU General Public License (the GNU GPL) version 3 or (at your option) any
# later version, in which case the provisions of the GNU GPL are applicable
# instead of those of the modified BSD license above.
# If you wish to allow use of your version of this file only under the terms
# of the GNU GPL and not to allow others to use your version of this file under
# the modified BSD license above, indicate your decision by deleting
# the provisions above and replace them with the notice and other provisions
# required by the GNU GPL. If you do not delete the provisions above,
# a recipient may use your version of this file under either the modified BSD
# license above or the GNU GPL.
#
################################################################################


import platform
import os
import os.path
import re
import sys
import subprocess
from distutils.command.build_ext import build_ext
from distutils.core import setup, Extension


curr_py_ver = platform.python_version()
min_py_vers = {
               2: "2.6.5",
               3: "3.1.2",
              }
if curr_py_ver < min_py_vers[int(curr_py_ver[0])]:
    raise SystemExit("Aborted: pyev requires Python2 >= {0[2]} OR "
                     "Python3 >= {0[3]}".format(min_py_vers))


pyev_version = "0.8.1"
pyev_description = open(os.path.abspath("README.txt"), "r").read()
libev_dir = os.path.abspath("src/libev")
libev_configure_ac = open(os.path.join(libev_dir, "configure.ac"), "r").read()
libev_version = re.search("AM_INIT_AUTOMAKE\(libev,(\S+)\)",
                          libev_configure_ac).group(1)


def get_posix_libs():
    libev_config_h = os.path.join(libev_dir, "config.h")
    subprocess.check_call(os.path.join(libev_dir, "configure"), cwd=libev_dir,
                          shell=True)
    libev_config = open(libev_config_h, "r").read()
    return [l.lower() for l in set(re.findall("#define HAVE_LIB(\S+) 1",
                                              libev_config))]


pyev_platforms = {
                  "nt": {
                         "define_fmt": "\\\"{0}\\\"",
                         "libraries": ["ws2_32"],
                        },
                  "posix": {
                            "define_fmt": "\"{0}\"",
                            "libraries": get_posix_libs,
                            "extra_compile_args": ["-fno-strict-aliasing"],
                           },
                 }


class pyev_build_ext(build_ext):

    def finalize_options(self):
        self.pyev_options = {}
        build_ext.finalize_options(self)
        if "sdist" not in sys.argv:
            plat_name = os.name
            if plat_name not in pyev_platforms:
                raise SystemExit("Aborted: platform '{0}' "
                                 "not supported".format(plat_name))
            self.pyev_options.update(pyev_platforms[plat_name])
            # libraries
            libraries = self.pyev_options["libraries"]
            if hasattr(libraries, "__call__"):
                libraries = libraries()
            if libraries:
                if self.libraries:
                    self.libraries.extend(libraries)
                else:
                    self.libraries = libraries
            # define
            define_fmt = self.pyev_options["define_fmt"]
            define = [
                      ("PYEV_VERSION", define_fmt.format(pyev_version)),
                      ("LIBEV_VERSION", define_fmt.format(libev_version)),
                     ]
            if self.define:
                self.define.extend(define)
            else:
                self.define = define

    def build_extension(self, ext):
        # extra_compile_args
        if "extra_compile_args" in self.pyev_options:
            extra_compile_args = self.pyev_options["extra_compile_args"]
            if ext.extra_compile_args:
                ext.extra_compile_args.extend(extra_compile_args)
            else:
                ext.extra_compile_args = extra_compile_args
        build_ext.build_extension(self, ext)


setup(
      name="pyev",
      version="-".join((pyev_version, libev_version)),
      url="http://packages.python.org/pyev/",
      download_url="http://pypi.python.org/pypi/pyev/",
      description="Python libev interface.",
      long_description=pyev_description,
      author="Malek Hadj-Ali",
      author_email="lekmalek@gmail.com",
      platforms=["Microsoft Windows", "POSIX"],
      license="BSD License / GNU General Public License (GPL)",
      cmdclass={"build_ext": pyev_build_ext},
      ext_modules=[
                   Extension("pyev",
                             ["src/pyev.c"],
                             define_macros=[
                                            # uncomment the following
                                            # to modify priorities
                                            #("EV_MINPRI", "-5"),
                                            #("EV_MAXPRI", "5"),
                                           ]
                            ),
                  ],
      classifiers=[
                   "Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Intended Audience :: System Administrators",
                   "License :: OSI Approved :: BSD License",
                   "License :: OSI Approved :: GNU General Public License (GPL)",
                   "Operating System :: Microsoft :: Windows :: Windows NT/2000",
                   "Operating System :: POSIX",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.1",
                   "Programming Language :: Python :: 3.2",
                  ]
     )
