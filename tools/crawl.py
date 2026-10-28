#!/usr/bin/env python3
"""Polite stdlib-only crawler: sitemap -> plain-text Markdown files + sources.csv.

Usage:
  python3 tools/crawl.py                 # docs.lambda.ai + lambda.ai (blog/site)
  python3 tools/crawl.py --github        # also list public repos for the GitHub orgs
"""
import csv
import json
import re
import subprocess
import sys
import time
import urllib.robotparser
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent / "corpus"
UA = "Mozilla/5.0 (PANW-SE account research; contact mikeovu@gmail.com)"
DELAY = 1.0  # seconds between requests
SITEMAPS = {
    "docs": "https://docs.lambda.ai/sitemap.xml",
    "lambda.ai": "https://lambda.ai/sitemap.xml",
}
GITHUB_ORGS = ["lambdal", "LambdaLabsML"]


def fetch(url):
    # curl uses the macOS keychain for CAs; python.org builds ship without a CA bundle
    r = subprocess.run(["curl", "-sSfL", "--max-time", "30", "-A", UA, url], capture_output=True)
    if r.returncode:
        raise RuntimeError(r.stderr.decode().strip())
    return r.stdout.decode("utf-8", "replace")


class TextExtractor(HTMLParser):
    """Keeps headings, paragraphs, list items, and table cells; drops chrome."""
    SKIP = {"script", "style", "nav", "header", "footer", "svg", "noscript", "form"}
    BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "tr", "pre", "blockquote", "div", "br"}

    def __init__(self):
        super().__init__()
        self.out, self.skip, self.title, self._in_title = [], 0, "", False

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag == "title":
            self._in_title = True
        elif not self.skip:
            if tag in ("h1", "h2", "h3", "h4"):
                self.out.append("\n\n" + "#" * int(tag[1]) + " ")
            elif tag == "li":
                self.out.append("\n- ")
            elif tag in ("td", "th"):
                self.out.append(" | ")
            elif tag in self.BLOCK:
                self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        elif tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self.skip:
            self.out.append(data)

    def text(self):
        t = "".join(self.out)
        t = re.sub(r"[ \t]+", " ", t)
        return re.sub(r"\n\s*\n\s*\n+", "\n\n", t).strip()


def slug(url):
    p = urlparse(url)
    s = (p.netloc + p.path).strip("/").replace("/", "__")
    return re.sub(r"[^A-Za-z0-9_.-]", "-", s) or "index"


def bucket(source, url):
    if source == "docs":
        return "docs"
    return "blog" if "/blog/" in url else "site"


def crawl_sitemap(source, sitemap_url, writer):
    rp = urllib.robotparser.RobotFileParser()
    host = urlparse(sitemap_url)
    rp.parse(fetch(f"{host.scheme}://{host.netloc}/robots.txt").splitlines())
    urls = re.findall(r"<loc>([^<]+)</loc>", fetch(sitemap_url))
    urls = [u for u in urls if not re.search(r"\.(png|jpe?g|gif|svg|webp|pdf|mp4)$", u, re.I)]
    print(f"[{source}] {len(urls)} urls", flush=True)
    for i, url in enumerate(urls, 1):
        dest = ROOT / bucket(source, url) / (slug(url) + ".md")
        if dest.exists():
            continue
        if not rp.can_fetch(UA, url):
            print(f"  skip (robots) {url}")
            continue
        try:
            html = fetch(url)
        except Exception as e:  # keep going on individual page failures
            print(f"  ERR {url}: {e}", flush=True)
            continue
        ex = TextExtractor()
        ex.feed(html)
        title = ex.title.strip()
        dest.write_text(f"# {title}\n\nSource: {url}\n\n{ex.text()}\n")
        writer.writerow([url, title, dest.relative_to(ROOT), datetime.now(timezone.utc).isoformat(timespec="seconds")])
        if i % 25 == 0:
            print(f"  {i}/{len(urls)}", flush=True)
        time.sleep(DELAY)


def list_github(writer):
    for org in GITHUB_ORGS:
        repos, page = [], 1
        while True:
            data = json.loads(fetch(f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}"))
            if not data:
                break
            repos += data
            page += 1
            time.sleep(DELAY)
        keep = [
            {k: r[k] for k in ("name", "full_name", "description", "html_url", "language",
                               "stargazers_count", "pushed_at", "archived", "fork", "topics")}
            for r in repos
        ]
        keep.sort(key=lambda r: r["stargazers_count"], reverse=True)
        out = ROOT / "github" / f"{org}.json"
        out.write_text(json.dumps(keep, indent=2))
        writer.writerow([f"https://github.com/{org}", f"{org} repos ({len(keep)})", out.relative_to(ROOT),
                         datetime.now(timezone.utc).isoformat(timespec="seconds")])
        print(f"[github] {org}: {len(keep)} repos", flush=True)


def main():
    for d in ("docs", "blog", "site", "github"):
        (ROOT / d).mkdir(parents=True, exist_ok=True)
    csv_path = ROOT / "sources.csv"
    new = not csv_path.exists()
    with csv_path.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["url", "title", "file", "fetched_at"])
        if "--github" in sys.argv:
            list_github(w)
        for source, sm in SITEMAPS.items():
            crawl_sitemap(source, sm, w)


if __name__ == "__main__":
    main()
