# vim: set filetype=python: 
import subprocess
import urllib

SCRIPT = """
/usr/bin/osascript<<END
tell application "Finder"
    set desktop picture to POSIX file "/tmp/bieber.jpg"
end tell
END"""

urllib.urlretrieve("http://www.frodux.org/bieber/bieber.jpg", "/tmp/bieber.jpg")

subprocess.Popen(SCRIPT, shell=True)
