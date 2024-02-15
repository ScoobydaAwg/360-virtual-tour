import webbrowser
import subprocess

def open_orbix_project(url="https://orbix360.com/_3L2pR10y"):
    webbrowser.open(url)

def close_orbix_project():
    # This is specific to Windows. For other OS, you might need a different command.
    subprocess.call(['taskkill', '/F', '/T', '/IM', 'chrome.exe'])
