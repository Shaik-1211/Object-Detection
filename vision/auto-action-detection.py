# This script can be used to automatically detect actions in images in the 'images/action' folder
from activity import detect_action
import os

# Save the result and image path as text in a text file
with open('results.txt', 'w') as f:
    for file in os.listdir('images/action'):
        image = os.path.join('images/action', file)
        result = detect_action(image)
        f.write(f'{file}: {result}\n')
