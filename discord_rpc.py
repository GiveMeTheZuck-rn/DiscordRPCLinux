

from pypresence import Presence
import subprocess
import time

CLIENT_ID = "YOUR_CLIENT_ID_HERE"

rpc = Presence(CLIENT_ID)
rpc.connect()


def get_active_app():
    try:
        window_id = subprocess.check_output(
            ["xdotool", "getwindowfocus"]
        ).decode().strip()

        wm_class = subprocess.check_output(
            ["xprop", "-id", window_id, "WM_CLASS"]
        ).decode().lower()

        if "=" not in wm_class:
            return "Unknown", "output"

        raw = wm_class.split("=")[1].strip()

        # ─────────────────────────────
        # If you would like to add images to ur rich prescence, 
        # Upload image files and use the provided list below or copy and paste 
        # and change the name to match ur application, the last word in each must be 
        # put to exactly what the name is in discord rich presence
        # ─────────────────────────────

        if "firefox" in raw:
            return "Firefox", "firefox"

        if "discord" in raw:
            return "Discord", "discordlogo"

        if "tor" in raw:
            return "Tor Browser", "torlogo"

        # terminals
        if any(x in raw for x in ["alacritty", "kitty", "xterm", "foot"]):
            return "Linux terminal", "output"

        if "code" in raw:
            return "VS Code", "vscode"

        return raw.title(), "output"

    except:
        return "Unknown", "output"


while True:
    app_name, asset = get_active_app()

    rpc.update(
        details=app_name,
        large_image=asset
    )

    time.sleep(5)
