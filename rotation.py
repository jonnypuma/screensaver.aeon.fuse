"""The screensaver's rounds (no Kodi imports: testable).

1.3.0 (skin 0.56.22): the user: "every item displayed is one dot in the sequence and it does 10 items at a time or
whatever the user has set it to and then it just goes back to the first dot and does 10 random more from the sources
the user has set to use". A round is one list from script.aeon.helper (?info=ssround): N items drawn at random from the
switched-on sources (films, TV shows, albums, in the cinemas now, airing today, airing tomorrow), mixed. The skin's list
steps through it (one item every ITEM_SECONDS, its autoscroll) and its pager shows one dot per item; when the round has
gone through, the next round is asked for. Without the helper: films from the library."""

HELPER = 'plugin://script.aeon.helper/'
KINDS = ('movies', 'tvshows', 'music', 'cinema', 'today', 'tomorrow')
ITEM_SECONDS = 10           # Custom_1156_Screensaver.xml, list 9701: <autoscroll time="10000" delay="10000" ...>
FALLBACK = 'videodb://movies/titles/'
MIN_COUNT, MAX_COUNT, DEFAULT_COUNT = 3, 10, 10     # the skin draws ten dots at most


def kinds_on(enabled):
    """The switched-on sources in their usual order; none -> films."""
    return [k for k in KINDS if enabled.get(k, True)] or ['movies']


def count_of(value):
    try:
        n = int(value)
    except (TypeError, ValueError):
        return DEFAULT_COUNT
    return max(MIN_COUNT, min(MAX_COUNT, n)) if n else DEFAULT_COUNT


def round_path(enabled, count, number):
    """The helper list for round `number` (the number makes each round a new list, so Kodi loads it again)."""
    return HELPER + '?info=ssround&n=%d&kinds=%s&r=%d' % (count_of(count), ','.join(kinds_on(enabled)), number)


def round_seconds(pages, count):
    """How long a round lasts: one step of the list per item it holds (the count asked for while that is unknown)."""
    n = pages if pages and pages > 0 else count_of(count)
    return n * ITEM_SECONDS
