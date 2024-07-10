from emotions import detect_emotions
from detect import text_to_speech

def main():
    image = 'images/cliff-booth.jpg'
    res = text_to_speech(image)
    print(res)
main()