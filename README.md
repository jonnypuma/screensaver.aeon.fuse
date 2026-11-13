# Aeon Fuse Screensaver (screensaver.aeon.fuse)

The screensaver of the [Aeon Fuse](../skin.aeon.fuse) skin, as a regular Kodi screensaver. It shows random films, TV
shows and albums from your library in the skin's own screensaver window. Under another skin it shows a black screen.

- Kodi 21 / 22 / 23 (Python 3, `xbmc.python` 3.0.1)
- Licence: GPL-2.0-or-later
- Needs the Aeon Fuse skin for its picture. The skin's helper (`script.aeon.helper`) supplies the library counts it
  uses to skip empty sections.

## Use

Choose it under Settings > Interface > Screensaver; the wait time is set there too. Its settings (the gear next to it):

- Show movies / Show TV shows / Show albums: each section can be switched off.
- Seconds before switching to the next kind.
- Zoom and slide the backgrounds (fanart).

While music plays, the skin's screensaver window shows the song, its cover and a spectrum tile in a corner.

The settings come in English and the skin's 22 languages (`resources/language`).

## How it works

Kodi starts `screensaver.py` when its timer runs out. The script opens the skin's window `Custom_1156_Screensaver.xml`
as a Python window and tells it what to show through `Window(Home).Property(aeon.ss.path)` and `aeon.ss.kind`. It
does not use the `ActivateWindow` builtin, because Kodi counts that as user activity and would wake up at once.
`rotation.py` decides which section comes next; it has no Kodi imports and is tested in `tests/`:

    python -m pytest tests

## Changes

See [CHANGELOG.md](CHANGELOG.md).
