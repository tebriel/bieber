import subprocess
import urllib

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

urllib.urlretrieve("http://www.frodux.org/bieber.jpg", "bieber.jpg")

subprocess.Popen(SCRIPT%'bieber.jpg', shell=True)
