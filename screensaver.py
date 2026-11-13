"""Aeon Fuse screensaver. Kodi starts this script when its screensaver timer runs out and stops it on any input.
Under the Aeon Fuse skin it shows the skin's own screensaver window (Custom_1156_Screensaver.xml) and tells it which
library section to show through Window(Home).Property(aeon.ss.path) / aeon.ss.kind; under another skin it shows a black
screen.

The window is opened from here as a Python window. The ActivateWindow builtin must not be used: Kodi treats it as user
activity and wakes up, which ended the screensaver (and its preview) the moment it started."""
import os
import time

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

from rotation import at, sections

ADDON = xbmcaddon.Addon()
SKIN = 'skin.aeon.fuse'
WINDOW_XML = 'Custom_1156_Screensaver.xml'
COUNT_PROPS = {'movies': 'aeon.count.movies', 'tvshows': 'aeon.count.tvshows', 'music': 'aeon.count.albums'}


class Monitor(xbmc.Monitor):
    def __init__(self):
        super(Monitor, self).__init__()
        self.done = False

    def onScreensaverDeactivated(self):
        self.done = True


def counts(home):
    """Library sizes published by script.aeon.helper; None when not known."""
    out = {}
    for kind, prop in COUNT_PROPS.items():
        value = home.getProperty(prop)
        out[kind] = int(value) if value.isdigit() else None
    return out


def run_skin(monitor):
    home = xbmcgui.Window(10000)
    enabled = {kind: ADDON.getSettingBool(kind) for kind in COUNT_PROPS}
    seq = sections(enabled, counts(home))
    every = ADDON.getSettingInt('switch') or 60
    # the skin zooms and slides the fanart backgrounds while this is set (Custom_1156_Screensaver.xml)
    home.setProperty('aeon.ss.zoom', 'true' if ADDON.getSettingBool('zoom') else '')
    started = time.time()
    shown = None
    window = None
    try:
        while not monitor.done and not monitor.abortRequested():
            kind, path = at(seq, started, time.time(), every)
            if kind != shown:
                home.setProperty('aeon.ss.kind', kind)
                home.setProperty('aeon.ss.path', path)
                if window is None:
                    window = xbmcgui.WindowXMLDialog(WINDOW_XML, xbmcvfs.translatePath('special://skin/'), 'default', '1080i')
                    window.show()
                shown = kind
            monitor.waitForAbort(0.5)
    finally:
        if window is not None:
            window.close()
            del window
        home.clearProperty('aeon.ss.kind')
        home.clearProperty('aeon.ss.path')
        home.clearProperty('aeon.ss.zoom')


def run_black(monitor):
    window = xbmcgui.WindowDialog()
    black = os.path.join(ADDON.getAddonInfo('path'), 'resources', 'black.png')
    window.addControl(xbmcgui.ControlImage(0, 0, window.getWidth(), window.getHeight(), black))
    window.show()
    while not monitor.done and not monitor.abortRequested():
        monitor.waitForAbort(0.5)
    window.close()


if __name__ == '__main__':
    mon = Monitor()
    if xbmc.getSkinDir() == SKIN:
        run_skin(mon)
    else:
        run_black(mon)
