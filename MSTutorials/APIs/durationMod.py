import math


def getDuration(duration_ms):
    seconds = math.floor((duration_ms / 1000) % 60)
    minutes = math.floor((duration_ms / (1000*60)) % 60)
    return f"{minutes} minutes, {seconds} seconds"
