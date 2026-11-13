"""Which library sections the screensaver cycles through (no Kodi imports: testable)."""
PATHS = (('movies', 'videodb://movies/titles/'), ('tvshows', 'videodb://tvshows/titles/'), ('music', 'musicdb://albums/'))


def sections(enabled, counts):
    """[(kind, path)] for the kinds that are switched on and not known to be empty.
    enabled: {kind: bool}. counts: {kind: int or None}; None = unknown, keep it.
    Never returns an empty list: with nothing left, movies are shown."""
    out = [(kind, path) for kind, path in PATHS
           if enabled.get(kind, True) and counts.get(kind) != 0]
    return out or [PATHS[0]]


def at(seq, started, now, every):
    """The entry on show `now`, when each one stays `every` seconds, starting at `started`."""
    every = max(1, int(every))
    return seq[int((now - started) // every) % len(seq)]
