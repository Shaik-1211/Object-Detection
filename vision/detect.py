import json,os
from gtts import gTTS
from ultralytics import YOLO 
from emotions import detect_emotions
from activity import detect_action

def process_image(image_path):
    model = YOLO('yolov8n-seg.pt')  
    
    # Process results list
    results = model(image_path)
    json_data = {}
    for result in results:
        res = result
        json_data = res.tojson() # Convert results to JSON
    data = json.loads(json_data) # Convert JSON to python dictionary
    name_count = {}
    # extract object names and count the objects
    for obj in data:
        name = obj['name']
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    # filename = os.path.splitext(os.path.basename(image_path))[0]
    # result.save(f'static/results/{filename}.jpg')  # save to disk
    # result.show()
    del model
    return name_count

def text_to_speech(filename):
    objects = process_image(filename)
    if 'person' in objects.keys() :
        emotion = detect_emotions(filename)
        print(emotion)
        action = detect_action(filename)
        print(action)
    results = {
        'objects': objects,
        'emotion': emotion,
        'action': action
    }
    return results
    # my_text = ''
    
    # # convert dictionary to string
    # for key, value in objects.items():
    #     verb = 'is'
    #     plural = ''
    #     if value>1:
    #         verb = 'are'
    #         plural = 's'
    #     my_text = my_text +'There '+ verb+ ' ' + str(value) + ' ' + key + plural + '\n'
    # language = 'en'

    # myobj = gTTS(text=my_text, lang=language, slow=False)

    # filename = os.path.splitext(os.path.basename(filename))[0]
    # audio_file = 'static/results/audio/' + filename + '.mp3'
    # myobj.save(audio_file)


