@echo off
rem Fetches the latest uploads from every channel in build.py, rebuilds index.html and pushes it to GitHub.
cd /d "%~dp0"
echo [1/4] Updating yt-dlp...
python -m pip install -q --upgrade --disable-pip-version-check yt-dlp || goto fail
echo [2/4] Pulling latest repo...
git pull -q --rebase || goto fail
echo [3/4] Fetching channel video lists (takes a minute)...
python build.py || goto fail
echo [4/4] Pushing to GitHub...
git add index.html
git diff --cached --quiet && (echo No new videos - already up to date. & goto done)
git commit -q -m "Update track list" || goto fail
git push -q || goto fail
echo.
echo Done! The site updates in a minute or two: https://s0lt4u.github.io/zoomboom/
:done
echo.
pause
exit /b 0
:fail
echo.
echo Something went wrong - see the messages above.
pause
exit /b 1
