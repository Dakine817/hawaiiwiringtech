@echo off
cd C:\Users\eykgo\Downloads\hawaiian-wiring-tech

echo Checking current files...
dir *.png

echo.
echo Renaming electrician.png.png to electrician.png...
ren "electrician.png.png" "electrician.png"

if exist "electrician.png" (
    echo File renamed successfully!
    dir electrician.png
) else (
    echo ERROR: Rename failed!
    pause
    exit /b 1
)

echo.
echo Running git commands...
git add -A
if errorlevel 1 (
    echo Git add failed
    pause
    exit /b 1
)

git commit -m "Fix: rename electrician.png.png to electrician.png"
if errorlevel 1 (
    echo Git commit failed
    pause
    exit /b 1
)

git push origin main
if errorlevel 1 (
    echo Git push failed
    pause
    exit /b 1
)

echo.
echo Success! Changes pushed to GitHub.
pause
