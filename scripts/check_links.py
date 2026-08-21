#!/usr/bin/env python3
"""Check unique HTTP links in repository text files without downloading bodies."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


URL_RE = re.compile(r"https?://[^\s)\]>\"']+")
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".cff"}
REACHABLE_HTTP_ERRORS = {401, 403, 405, 406, 418, 429}


def collect_urls(root: Path) -> list[str]:
    urls: set[str] = set()
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in URL_RE.findall(text):
            urls.add(match.rstrip(".,;:!?"))
    return sorted(urls)


def request(url: str, method: str, timeout: float) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        method=method,
        headers={
            "User-Agent": "beauty-product-development-skills-link-check/1.0",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.8,*/*;q=0.5",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.status, response.geturl()


def check(url: str, timeout: float) -> tuple[str, bool, str]:
    try:
        status, final_url = request(url, "HEAD", timeout)
        return url, 200 <= status < 400, f"HTTP {status} -> {final_url}"
    except urllib.error.HTTPError as exc:
        if 300 <= exc.code < 400:
            return url, True, f"HTTP {exc.code} redirect response"
        if exc.code in REACHABLE_HTTP_ERRORS:
            return url, True, f"HTTP {exc.code} (reachable; automated access limited)"
        if exc.code not in {400, 404, 501}:
            return url, False, f"HTTP {exc.code}"
    except Exception:
        pass

    try:
        status, final_url = request(url, "GET", timeout)
        return url, 200 <= status < 400, f"HTTP {status} -> {final_url}"
    except urllib.error.HTTPError as exc:
        if 300 <= exc.code < 400:
            return url, True, f"HTTP {exc.code} redirect response"
        if exc.code in REACHABLE_HTTP_ERRORS:
            return url, True, f"HTTP {exc.code} (reachable; automated access limited)"
        return url, False, f"HTTP {exc.code}"
    except Exception as exc:
        return url, False, f"{type(exc).__name__}: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=10)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    urls = collect_urls(root)
    failures: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(check, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            url, ok, detail = future.result()
            print(f"{'OK' if ok else 'FAIL'}\t{detail}\t{url}")
            if not ok:
                failures.append((url, detail))

    print(f"\nChecked {len(urls)} unique URLs; failures: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
