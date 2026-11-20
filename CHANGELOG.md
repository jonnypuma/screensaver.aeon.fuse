# Aeon Fuse Screensaver changelog

Released together with the skin. Each version below names the skin version it came with.

## 1.3.0 (skin 0.56.22)
- Rounds instead of sections (the user: one dot per item, N items, then N new random ones from the switched-on
  sources): each round is one list of Aeon Fuse Helper (?info=ssround, helper 0.3.98), its items drawn at random from
  films, TV shows, albums, in the cinemas now, airing today and tomorrow, mixed (never the same source twice in a row
  while another has items). The skin's pager shows one dot per item, the one on show ringed; when the round has gone
  through, the next one is asked for. Setting "Items per round" (3-10, 10) replaces "Seconds before switching to the
  next kind". The old round stays on screen while the next one is built, the next one is asked for early by the time
  the last one took to build, and each round starts at its first item. Tests: tests/test_rotation.py.

## 1.2.2 (skin 0.56.20)

- The pager is the rotation: Window(Home).Property(aeon.ss.pages) (how many sections) and aeon.ss.page (the one on
  show) replace aeon.ss.dots (rotation.pager, tests). Airing today with one episode showed a single ring and no dots.

## 1.2.1 (skin 0.56.20)
- The pager's dots no longer vanish while the list reloads (a switch to another list, an add-on list that takes a few
  seconds): the last count the list had is kept in Window(Home).Property(aeon.ss.dots) for the skin.

## 1.2.0 (skin 0.45.1)
- Three new slides, each with its own switch (on): a film in the cinemas now (TMDb Helper's "In cinemas now", through
  Aeon Fuse Helper), what the Planner has airing today, and what airs tomorrow. They are fetched in the background when
  the screensaver starts and join the rotation only when they hold something.
- The rotation moves on section by section, so a list that turns up later fits in without a jump.

## 1.1.2 (skin 0.28.0)
- Settings translated into the skin's 22 languages.

## 1.1.1 (skin 0.27.1)
- Icon and fanart.

## 1.1.0 (skin 0.27.0)
- Renamed: Aeon Fuse Screensaver, `screensaver.aeon.fuse` (was `screensaver.glass.aeon`), for the skin
  `skin.aeon.fuse`. A chosen screensaver moves to the new id.

## 1.0.2 (skin 0.21.0)
- New setting: zoom and slide the fanart backgrounds, starting again with every title.

## 1.0.1 (skin 0.12.8)
- It no longer closes the moment it starts, and the preview works: the window is opened as a Python window, not with
  `ActivateWindow` (which Kodi counts as user activity).

## 1.0.0 (skin 0.11.0)
- The skin's screensaver as its own add-on and a regular Kodi screensaver, with its on / off switch and wait time in
  Settings > Interface > Screensaver. It cycles through random films, TV shows and albums; each can be switched off.
