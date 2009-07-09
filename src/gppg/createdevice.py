# GnuPPG - Create GnuPPG device
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
import shutil

from gppg.configparser import GppgHomedir
from gppg.mounter import cryptopen
from gppg.utils import run_cryptsetup, run_mkfs

def create_lv(vgname, lvname, size, *args):
    # We may want to support extends down the road.
    SIZE_UNITS = 'kKmMgGtT'
    EXTENTS_UNITS = ['%VG', '%FREE']
    cargs = ['lvcreate', '-n %(lvname)' % {'lvname':lvname}]
    for arg in args:
        cargs.append(arg)
    if size[-1:] in SIZE_UNITS:
        cargs += ['-l %(size)' % {'size':size}]
        cargs += [vgname]
    elif (size[-3:] or size[-5:]) in EXTENTS_UNITS:
        cargs += ['-L %(size)' % {'size':size}]
        cargs += [vgname]
    else:
        raise ValueError("Invalid size %s, unit must be one of kKmMgGtT, %VG "
            "or %FREE." % size)
    retcode = subprocess.call(cargs)
    if retcode < 0:
        raise ValueError("%s was killed by signal %d" % (' '.join(cargs),
            retcode))


def create(name, decrypted_name, mount_point, config_file, unmount_time='',
        device='', lvm=False, vgname='', lvname='', size='', fstype='',
        homedir='', cryptsetup_args=[], mkfs_args=''):
    """ Will create the GnuPPG device.
    If not using LVM, device is a block device.
    If using LVM, lvm will be True. We require:
        vgname: name of the volume group
        lvname: name of the logical volume
        size: size of the logical volume
    In both cases, we require:
        fstype: filesystem type, there must be a mkfs.fstype
        homedir: path to the GnuPG homedir
    Optional arguments:
        cryptsetup_args: extra cryptsetup arguments
        mkfs_args: extra mkfs arguments
    """

    assert fstype, "Please provide a filesystem type"
    assert homedir, "Please provide a path to a GnuPG homedir"
    assert config, "Please provide a path to a GnuPPG configuration file"

    if (device and lvm) or (not device and (lvm == False)):
        raise ValueError("Please provide either device or a True value to lvm")

    homedir = GppgHomedir(section=name, config=config_file)
    try:
        homedir.config.set(homedir.section, 'decrypted_name', decrypted_name)
    except ConfigParser.NoSectionError:
        homedir.config.add_section(homedir.section)
        homedir.config.set(homedir.section, 'decrypted_name', decrypted_name)

    if device:
        # We want to ask for the passphrase twice.
        run_cryptsetup('luksFormat', ['-y'] + cryptsetup_args, device)
        homedir.config.set(homedir.section, 'encrypted_device', device)
        # Do we need the next line?
        cryptopen(homedir)
        run_mkfs(fstype, '/dev/mapper/%s' % decrypted_name, mkfs_args)
    else:
        create_lv(vgname, lvname, size, ['-y'] + cryptsetup_args)
        lv =  '/dev/mapper/%(vgname)s-%(lvname)s' % {'vgname': vgname, 'lvname': lvname}
        run_cryptsetup('luksFormat', ['-y'] + cryptsetup_args, lv)
        homedir.config.set(homedir.section, 'encrypted_device', lv)
        cryptopen(homedir)
        run_mkfs(fstype, '/dev/mapper/%s' % decrypted_name, mkfs_args)

    run_mount('/dev/mapper/%s' % decrypted_name, mount_point)
    shutil.copytree(homedir, os.path.join(mount_point, '.gnupg'))
    os.symlink(os.path.join(mount_point, '.gnupg'), homedir)

    homedir.config.set(homedir.section, 'mount_point', mount_point)
    if unmount_time:
        homedir.config.set(homedir.section, 'unmount_time', unmount_time)

    return homedir
