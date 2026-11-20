<div align="center">
  <img src="https://jonnypuma.github.io/assets/screensaver.aeon.fuse/icon.webp" width="140" alt="Aeon Fuse Screensaver">
  <h1>Aeon Fuse Screensaver</h1>
  <p><b>Random movies, TV shows and albums from your library, in the Aeon Fuse look.</b></p>
  <p><a href="https://jonnypuma.github.io/#/screensaver.aeon.fuse"><b>Project page</b></a> · <a href="https://jonnypuma.github.io/"><b>All add-ons and apps by jonnypuma</b></a> · <a href="https://jonnypuma.github.io/#/skin.aeon.fuse"><b>Aeon Fuse skin</b></a> · <a href="https://jonnypuma.github.io/#install"><b>Install from the Skippy Repo</b></a></p>
</div>

The screensaver shows random films, TV shows and albums from your library in the skin's own screensaver window. Under another skin it shows a black screen.

- Kodi 21 / 22 / 23 (Python 3, `xbmc.python` 3.0.1)
- Licence: GPL-2.0-or-later
- Needs the Aeon Fuse skin for its picture. The skin's helper (`script.aeon.helper`) supplies the library counts it
  uses to skip empty sections.

## Screenshots

Click a picture for the full size.

<table>
  <tr>
    <td width="33%" align="center" valign="top"><a href="https://jonnypuma.github.io/assets/skin.aeon.fuse/aeon/screensaver.webp"><img src="https://jonnypuma.github.io/assets/skin.aeon.fuse/aeon/t/screensaver.webp" alt="A film from the library"></a><br><sub>A film from the library</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://jonnypuma.github.io/assets/skin.aeon.fuse/aeon/screensaver_airing.webp"><img src="https://jonnypuma.github.io/assets/skin.aeon.fuse/aeon/t/screensaver_airing.webp" alt="On an upcoming episode: Airing today"></a><br><sub>On an upcoming episode: Airing today</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://jonnypuma.github.io/assets/skin.aeon.fuse/aeon/music_screensaver.webp"><img src="https://jonnypuma.github.io/assets/skin.aeon.fuse/aeon/t/music_screensaver.webp" alt="While a song plays: the song and its cover in a corner"></a><br><sub>While a song plays: the song and its cover in a corner</sub></td>
  </tr>
</table>
## Install

Install it from the Skippy Repo: Add-ons > Install from repository > Skippy Repo > Screensavers.

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
