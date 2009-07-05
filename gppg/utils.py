# GnuPPG - System utilities
# Copyright (C) 2009  Ryan Kavanagh <ryanakca@kubuntu.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess

def run_cryptsetup(action, options=[], *args):
    """ Will run 'cryptsetup options action args', passing args to cryptsetup.

    Can raise either a suprocess.CalledProcessError or an OSError.
    """

    cargs = ['crypsetup']
    for option in options:
        cargs.append(option)
    cargs += [action]
    for arg in args
        cargs.append(arg)

    s = subprocess.call(cargs)
    if retcode < 0:
        raise subprocess.CalledProcessError(s, ' '.join(cargs))


def run_mkfs(fstype, device, *args):
    """ Will format device using '/sbin/mkfs.fstype *args device'.
    
    Can raise either a suprocess.CalledProcessError or an OSError.
    """

    cargs = ['mkfs.' + fstype]
    for arg in args:
        cargs.append(arg)
    cargs.append(device)

    s = subprocess.call(cargs)
    if retcode < 0:
        raise subprocess.CalledProcessError(s, ' '.join(cargs))

def run_mount(device, dir, *args)
    """ Will run 'mount args device dir'. """
    
    cargs = ['mount']
    for arg in args:
        cargs.append(arg)
    cargs += [device, dir]

    s = subprocess.call(cargs)
    if retcode < 0:
        raise subprocess.CalledProcessError(s, ' '.join(cargs))
