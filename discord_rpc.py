

from pypresence import Presence
import subprocess
import time

CLIENT_ID = "1501721239809560616"

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
        # MATCH YOUR DISCORD ASSETS
        # ─────────────────────────────

        if "firefox" in raw:
            return "Firefox", "firefox"

        if "discord" in raw:
            return "Discord", "discordlogo"

        if "tor" in raw:
            return "Tor Browser", "torlogo"

        # terminals (optional fallback)
        if any(x in raw for x in ["alacritty", "kitty", "xterm", "foot"]):
            return "Arch Terminal", "output"

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
