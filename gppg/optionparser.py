# GnuPPG - Option parser
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

import optparse

parser = optparse.OptionParser(version="Pre-Alpha")
parser.add_option("-c", "--create", action="store_true", default=False)
create_group = optparse.OptionGroup(parser, "Create options", 
description="Options for creating a GnuPPG encrypted device.")
create_group.add_option("-l", "--lvm", action="store_true", default=False)
create_group.add_option("-L", "--size")
create_group.add_option("-f", "--fstype")
create_group.add_option("-n", "--lvname", help="Name of the LVM logical "
   "volume.")
parser.add_option_group(create_group)
parser.add_option("-m", "--mount", action="store_true", dest="mount", default=True)
parser.add_option("-u", "--unmount", action="store_false", dest="mount", default=False)
