from pypresence import Presence
import subprocess
import time

CLIENT_ID = "YOUR_CLIENT_ID_HERE"

try:
    rpc = Presence(CLIENT_ID)
    rpc.connect()
except Exception as e:
    print(f"Failed to connect to Discord: {e}")
    exit(1)


def get_active_app():
    try:
        window_id = subprocess.check_output(
            ["xdotool", "getwindowfocus"]
        ).decode().strip()

        wm_class = subprocess.check_output(
            ["xprop", "-id", window_id, "WM_CLASS"]
        ).decode().lower()

        if "=" not in wm_class:
            return "Unknown", None

        raw = wm_class.split("=")[1]
        classes = [x.strip().strip('"') for x in raw.split(",")]

        if not classes:
            return "Unknown", None

        app = classes[-1].lower()

        # optional application image mappings
        # uncomment any you want to enable
        # if u want any, make sure u make a rich presense image corresponding to the 
        # exact names on the right side 

        # if "firefox" in app:
        #     return "Firefox", "firefox" 

        # if "discord" in app:
        #     return "Discord", "discordlogo"

        # if "tor" in app:
        #     return "Tor Browser", "torlogo"

        # if "code" in app:
        #     return "VS Code", "vscode"

        if any(x in app for x in ["alacritty", "kitty", "xterm", "foot"]):
            return "Linux Terminal", None

        return app.title(), None

    except Exception as e:
        print(f"Error detecting active application: {e}")
        return "Unknown", None


last_app = None

while True:
    app_name, asset = get_active_app()

    if app_name != last_app:
        try:
            if asset:
                rpc.update(
                    details=app_name,
                    large_image=asset
                )
            else:
                rpc.update(
                    details=app_name
                )

            last_app = app_name

        except Exception as e:
            print(f"Failed to update Rich Presence: {e}")

    time.sleep(5)
