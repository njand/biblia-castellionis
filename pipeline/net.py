"""HTTP downloads with an on-disk cache under sources/."""

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "biblia-castellionis-pipeline/0.1 (https://github.com/njand/biblia-castellionis)"


def get(url, retries=3, timeout=120):
    """Return the body of `url` as bytes. Retries on network errors and 429/5xx."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == retries - 1:
                raise
        except urllib.error.URLError:
            if attempt == retries - 1:
                raise
        time.sleep(2 ** attempt * 5)


def get_json(url, **params):
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    return json.loads(get(url))


def download(url, path: Path, refresh=False):
    """Download `url` to `path` unless it is already there. Returns the path."""
    if path.exists() and not refresh:
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    data = get(url)
    tmp = path.with_suffix(path.suffix + ".part")
    tmp.write_bytes(data)
    tmp.replace(path)
    return path
