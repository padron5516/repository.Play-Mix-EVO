# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# ayuda - Videos de ayuda y tutoriales para pelisalacarta
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
# contribuci?n de jurrabi
# ----------------------------------------------------------------------
from core import config
from core import logger
from core.item import Item
from channels import youtube_channel

CHANNELNAME = "ayuda"


def isGeneric():
    return True


def mainlist(item):
    logger.info("pelisalacarta.channels.ayuda mainlist")
    itemlist = []

    cuantos = 0
    if config.is_xbmc():
        itemlist.append(Item(channel=CHANNELNAME, action="force_creation_advancedsettings",
                             title="Crear fichero advancedsettings.xml optimizado"))
        cuantos += cuantos
        
    if config.is_xbmc():
        itemlist.append(Item(channel=CHANNELNAME, action="updatebiblio",
                             title="Buscar nuevos episodios y actualizar biblioteca"))
        cuantos += cuantos

    if cuantos > 0:
        itemlist.append(Item(channel=CHANNELNAME, action="tutoriales", title="Ver guías y tutoriales en vídeo"))
    else:
        itemlist.extend(tutoriales(item))

    return itemlist


def tutoriales(item):
    playlists = youtube_channel.playlists(item,"tvalacarta")

    itemlist = []

    for playlist in playlists:
        if playlist.title == "Tutoriales de pelisalacarta":
            itemlist = youtube_channel.videos(playlist)

    return itemlist


def force_creation_advancedsettings(item):

    # Ruta del advancedsettings
    import xbmc
    import xbmcgui
    import os
    advancedsettings = xbmc.translatePath("special://userdata/advancedsettings.xml")

    # Copia el advancedsettings.xml desde el directorio resources al userdata
    fichero = open(os.path.join(config.get_runtime_path(), "resources", "advancedsettings.xml"))
    texto = fichero.read()
    fichero.close()
    
    fichero = open(advancedsettings, "w")
    fichero.write(texto)
    fichero.close()
                
    dialog2 = xbmcgui.Dialog()
    dialog2.ok("plugin", "Se ha creado un fichero advancedsettings.xml",
               "con la configuración óptima para el streaming.")

    return []


def updatebiblio(item):
    import library_service
    
    itemlist = []
    itemlist.append(Item(channel=CHANNELNAME, action="", title="Actualizacion en curso..."))
    
    return itemlist
