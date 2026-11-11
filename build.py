"""Rebuilds ZoomBoom.html with every current upload from the channels below.

Run:  python build.py     (needs:  python -m pip install yt-dlp)
Then commit and push index.html.
"""
import json, os, time

# ---- Edit this list to add/remove channels -------------------------------
CHANNELS = [
    "https://www.youtube.com/@lostmemory.mp3",
    "https://www.youtube.com/channel/UCkQTBxYmJRcDz1LVmh92HOA",  # Noumena
    "https://www.youtube.com/@thisneverhappened",
    "https://www.youtube.com/@Anjunadeep",
    "https://www.youtube.com/@Arcologies",
]
# --------------------------------------------------------------------------

ROOT = os.path.dirname(os.path.abspath(__file__))


def fetch():
    import yt_dlp
    names, rows, seen = [], [], set()
    opts = {"extract_flat": "in_playlist", "quiet": True, "skip_download": True, "ignoreerrors": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        for ch in CHANNELS:
            url = ch.rstrip("/")
            if not url.endswith("/videos"):
                url += "/videos"
            print(f"fetching {url} ...", flush=True)
            info = ydl.extract_info(url, download=False) or {}
            names.append(info.get("channel") or info.get("uploader") or info.get("title") or ch)
            n = 0
            for e in info.get("entries") or []:
                if not e or not e.get("id") or e["id"] in seen:
                    continue
                seen.add(e["id"])
                rows.append([e["id"], e.get("title") or e["id"], len(names) - 1, e.get("duration") or 0])
                n += 1
            print(f"  {names[-1]}: {n} videos", flush=True)
    return [names, int(time.time()), rows]


if __name__ == "__main__":
    data = fetch()
    with open(os.path.join(ROOT, "template.html"), encoding="utf-8") as f:
        html = f.read()
    # "</" escaped so a track title can never close the <script> tag
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = os.path.join(ROOT, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html.replace("/*__DATA__*/null", blob))
    print(f"wrote {out} ({len(data[2])} tracks, {os.path.getsize(out) // 1024} KB)")
