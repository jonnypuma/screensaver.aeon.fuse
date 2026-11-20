"""Aeon Fuse screensaver. Kodi starts this script when its screensaver timer runs out and stops it on any input.
Under the Aeon Fuse skin it shows the skin's own screensaver window (Custom_1156_Screensaver.xml) and tells it which
library section to show through Window(Home).Property(aeon.ss.path) / aeon.ss.kind; under another skin it shows a black
screen.

1.2.0: besides the library sections, a film in the cinemas now and what the Planner (script.aeon.helper) has airing
today and tomorrow. Those lists are asked for in the background when the screensaver starts and join the rotation once
they are known to hold something.

1.2.2: the pager's dots stand for the sections of the rotation, not the items of one list.

1.3.0 (skin 0.56.22): rounds instead of sections. Each round is one list of script.aeon.helper (?info=ssround): N
items (Items per round, 10) drawn at random from the switched-on sources and mixed; one dot per item; when the round
has gone through, N new ones (rotation.py).

The window is opened from here as a Python window. The ActivateWindow builtin must not be used: Kodi treats it as user
activity and wakes up, which ended the screensaver (and its preview) the moment it started."""
import os
import time

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

from rotation import FALLBACK, ITEM_SECONDS, KINDS, count_of, round_path, round_seconds

ADDON = xbmcaddon.Addon()
SKIN = 'skin.aeon.fuse'
WINDOW_XML = 'Custom_1156_Screensaver.xml'
PROPS = ('aeon.ss.kind', 'aeon.ss.path', 'aeon.ss.zoom', 'aeon.ss.pages', 'aeon.ss.page', 'aeon.ss.ready')


class Monitor(xbmc.Monitor):
    def __init__(self):
        super(Monitor, self).__init__()
        self.done = False

    def onScreensaverDeactivated(self):
        self.done = True


def run_skin(monitor):
    home = xbmcgui.Window(10000)
    enabled = dict((kind, ADDON.getSettingBool(kind)) for kind in KINDS)
    count = count_of(ADDON.getSettingInt('count'))
    helper = xbmc.getCondVisibility('System.AddonIsEnabled(script.aeon.helper)')
    # the skin zooms and slides the fanart backgrounds while this is set (Custom_1156_Screensaver.xml)
    home.setProperty('aeon.ss.zoom', 'true' if ADDON.getSettingBool('zoom') else '')
    for prop in ('aeon.ss.kind', 'aeon.ss.page'):
        home.clearProperty(prop)                      # 1.3.0: the item's own kind and the list position drive the skin
    window = None
    number = 0
    next_round = 0
    asked = None                 # when the round on its way was asked for
    try:
        while not monitor.done and not monitor.abortRequested():
            now = time.time()
            if asked is None and now >= next_round:
                number += 1
                home.clearProperty('aeon.ss.ready')
                if helper:
                    home.setProperty('aeon.ss.path', round_path(enabled, count, number))
                else:
                    home.setProperty('aeon.ss.path', FALLBACK)
                    home.setProperty('aeon.ss.pages', str(count))
                if window is None:
                    window = xbmcgui.WindowXMLDialog(WINDOW_XML, xbmcvfs.translatePath('special://skin/'), 'default', '1080i')
                    window.show()
                asked = now
            # the helper says when the round is built (aeon.ss.ready = its number); the old round stays on screen until
            # then. The new one starts at its first item, and the next one is asked for early by the time this one took
            # to build, so the last item keeps its time and the list does not wrap back to the first one meanwhile.
            if asked is not None and (not helper or home.getProperty('aeon.ss.ready') == str(number) or now - asked > 40):
                build = now - asked
                asked = None
                if number > 1:
                    xbmc.executebuiltin('SetFocus(9701,0,absolute)')
                pages = home.getProperty('aeon.ss.pages')
                next_round = now + round_seconds(int(pages) if pages.isdigit() else 0, count) - min(build, ITEM_SECONDS - 1) - 0.5
            monitor.waitForAbort(0.25)
    finally:
        if window is not None:
            window.close()
            del window
        for prop in PROPS:
            home.clearProperty(prop)


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
