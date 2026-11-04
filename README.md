# ZoomBoom

One endless, shuffled YouTube radio built from three music channels:
[lostmemory.mp3](https://www.youtube.com/@lostmemory.mp3),
[Noumena](https://www.youtube.com/channel/UCkQTBxYmJRcDz1LVmh92HOA) and
[This Never Happened](https://www.youtube.com/@thisneverhappened).

**▶ Listen: https://s0lt4u.github.io/zoomboom/**

No ads if you're signed in to YouTube Premium in the same browser.
Keys: Space play/pause · N next · P prev.

## Run it locally

YouTube won't play videos on a page opened straight from a file, so serve the folder instead:

- Windows: double-click `Launch ZoomBoom.bat`
- Anywhere: `python -m http.server 8777`, then open http://localhost:8777

## Update the track list

The track list is a snapshot baked into `index.html`. To pick up new uploads or change channels:

```bash
python -m pip install yt-dlp
python build.py        # edit CHANNELS at the top of build.py first if you like
```

That rebuilds `index.html` from `template.html`. Commit and push it, and the live site updates.
