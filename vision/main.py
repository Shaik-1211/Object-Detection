from emotions import detect_emotions
from detect import text_to_speech

def main():
    task = str(input(
        'Select the action to be performed: \n 1.Object Detection \n 2.Emotion Detection \n 3.Activity Detection\n'))
    if task == '1':
        text_to_speech('images/cat.jpg')
        print('Object Detection')
    elif task == '2':
        image_path = 'emotions1.webp'
        detect_emotions(image_path)
        print('Emotion Detection')
    elif task == '3':
        print('Activity Detection')
    else:
        print('Invalid Input')
main()