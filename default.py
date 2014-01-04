#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2012-2013 Team-XBMC
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    This script is based on script.randomitems & script.wacthlist
#    Thanks to their original authors

import os
import sys
import xbmcaddon
import xbmcgui
import xbmc

__addon__    = xbmcaddon.Addon()
__addonid__  = __addon__.getAddonInfo('id')
__setting__  = __addon__.getSetting
scriptPath   = __addon__.getAddonInfo('path')
dialog       = xbmcgui.Dialog()
new_file     = os.path.join(scriptPath, 'resources', 'media','IncludesHomeMenuItems.xml')
new_location = "/opt/xbmc-bcm/xbmc-bin/share/xbmc/addons/skin.confluence/720p/"

def copy_file():
    os.system('sudo cp -rf %s %s' % (new_file, new_location))
    dialog.ok('remove browser', 'Reloading skin to apply change')
    xbmc.executebuiltin('XBMC.ReloadSkin()')

if (__name__ == "__main__"):
    copy_file()
