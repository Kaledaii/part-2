import os
if os.path.exists("clap.mp3"):
    playsound("clap.mp3")
else:
    print("Sound file not found!")