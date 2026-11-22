import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL_PATTERN = re.compile(r"!?\[[^\]]*\]\((https?://[^)\s]+)")
HEADERS = {"User-Agent": "Mozilla/5.0 link-checker/1.0"}


def fetch(url, method):
    request = urllib.request.Request(url, headers=HEADERS, method=method)
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.status


def check(url):
    try:
        status = fetch(url, "HEAD")
        if status < 400:
            return None
        return f"HTTP {status}"
    except urllib.error.HTTPError as error:
        if error.code in (403, 405):
            try:
                status = fetch(url, "GET")
                if status < 400:
                    return None
                return f"HTTP {status}"
            except urllib.error.HTTPError as retry_error:
                return f"HTTP {retry_error.code}"
            except Exception as retry_error:
                return str(retry_error)
        return f"HTTP {error.code}"
    except Exception as error:
        return str(error)


def main():
    text = Path("README.md").read_text(encoding="utf-8")
    urls = list(dict.fromkeys(URL_PATTERN.findall(text)))
    failures = []
    for url in urls:
        reason = check(url)
        if reason:
            failures.append((url, reason))

    if failures:
        print("Broken links:")
        for url, reason in failures:
            print(f"- {url}: {reason}")
        sys.exit(1)

    print(f"Checked {len(urls)} unique links.")


if __name__ == "__main__":
    main()
