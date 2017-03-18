# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.filmelozetesek'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

AddonPath = addon.get_path()
IconPath = os.path.join(AddonPath , "resources/media/")
fanart = os.path.join(AddonPath + "/fanart.png")
def icon_path(filename):
    if 'http://' in filename:
        return filename
    return os.path.join(IconPath, filename)


YOUTUBE_CHANNEL_ID1 = "acompanyhungary"
YOUTUBE_CHANNEL_ID2 = "ADSService1"
YOUTUBE_CHANNEL_ID3 = "bigbang201111"
YOUTUBE_CHANNEL_ID4 = "CinetelHungary"
YOUTUBE_CHANNEL_ID5 = "cgzir2010"
YOUTUBE_CHANNEL_ID6 = "ForumHungary"
YOUTUBE_CHANNEL_ID7 = "freemanfilmhun"
YOUTUBE_CHANNEL_ID8 = "InterComHun"
YOUTUBE_CHANNEL_ID9 = "mozinet"
YOUTUBE_CHANNEL_ID10 = "PARLUXFILM"
YOUTUBE_CHANNEL_ID11 = "ProVideoFilmHUN"
YOUTUBE_CHANNEL_ID12 = "Michele0222"
YOUTUBE_CHANNEL_ID13 = "VertigoMediaKft"

# Entry point
def run():
    plugintools.log("filmelozetesek.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
		action = params.get("action")
		exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("filmelozetesek.main_list "+repr(params))

    plugintools.add_item( 
		#action="", 
		title="A Company Hungary",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail=icon_path('acompany.png'),
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="ADS Service",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail=icon_path('ads.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Big Bang Media",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail=icon_path('bigbang.jpg'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Cinetel",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail=icon_path('cinetel.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Cirko Gejzir",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail=icon_path('cirko.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Forum Hungary",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID6+"/",
		thumbnail=icon_path('forumhungary.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Freeman Film",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID7+"/",
		thumbnail=icon_path('freeman.jpg'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="InterCom",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID8+"/",
		thumbnail=icon_path('intercom.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Mozinet Youtube",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID9+"/",
		thumbnail=icon_path('mozinet.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="PARLUX Entertainment Magyarország",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID10+"/",
		thumbnail=icon_path('parlux.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Pro Video Film (BD/DVD)",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID11+"/",
		thumbnail=icon_path('provideo.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="UIP-Duna Film",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID12+"/",
		thumbnail=icon_path('uipduna.png'), fanart=fanart,
		folder=True )

    plugintools.add_item( 
		#action="", 
		title="Vertigo Média",
		url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID12+"/",
		thumbnail=icon_path('vertigo.png'), fanart=fanart,
		folder=True )

run()