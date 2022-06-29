#!/bin/sh
SET browser_profile=c:\temp\chrome_temp

RMDIR %browser_profile% /s /y
MKDIR %browser_profile%

"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --window-size=1280,1024 --new-window --user-data-dir=%browser_profile% https://hero-wars.com/?hl=en
