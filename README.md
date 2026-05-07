Please follow these instructions 

ensure you are using Xorg (x11)
python is installed and updated
-------------------------------
# install pypresence 
pip install pypresence 
-------------------------------
# intall xdotool & wmctrl
https://github.com/jordansissel/xdotool
https://github.com/dancor/wmctrl
# (may be available by your package manager) 
-------------------------------
# creating a discord application 
Head over to https://discord.com/developers/applications

Make a new application 
Copy the application ID 

nano discord_rpc.py (or vim) 
Paste the application id into the placeholder at the top of the text
-------------------------------
if you would like to add images to rich prescence, follow the guide at the bottom of the code.
-------------------------------
# To run the command:
python discord_rpc.py (discord must be open)
-------------------------------
