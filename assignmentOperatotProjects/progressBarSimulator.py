# 28.Progress Bar Simulator: Simulate a file download where a variable is incremented by a certain percentage (+=) until it reaches 100%.

# Progress Bar Simulator

import time

print("----- Progress Bar Simulator -----")

progress = 0

while progress < 100:
    progress += 10  # increment by 10%
    if progress > 100:
        progress = 100  # cap at 100%
    print(f"Downloading... {progress}%")
    time.sleep(0.5)  # simulate delay

print("Download Complete!")
