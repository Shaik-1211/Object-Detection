from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import os,numpy as np

# Activities that can be detected by the model
# ['applauding', 'blowing_bubbles', 'brushing_teeth', 
# 'cleaning_the_floor', 'climbing', 'cooking', 'cutting_trees', 
# 'cutting_vegetables', 'drinking', 'feeding_a_horse', 
# 'fishing', 'fixing_a_bike', 'fixing_a_car', 'gardening', 'jumping']  


def detect_action(img_path):
    model = load_model('action-detection-model.h5')
    class_labels = ['applauding', 'blowing_bubbles', 'brushing_teeth', 'cleaning_the_floor', 'climbing', 'cooking', 'cutting_trees', 'cutting_vegetables', 'drinking', 'feeding_a_horse', 'fishing', 'fixing_a_bike', 'fixing_a_car', 'gardening', 'jumping']  # Update with your actual class labels

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  

    predictions = model.predict(img_array)
    predicted_class = class_labels[np.argmax(predictions)]
   
    return predicted_class
    # img = Image.open(img_path) 

    # if img.mode == 'RGBA':
    #     img = img.convert('RGB')

    # buffered = BytesIO()
    # img.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue()).decode()

    # image_name = os.path.basename(img_path)
    # Save the result image with the predicted action label
    # draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype("arial.ttf", 24)  
    # draw.rectangle([(10, 10), (150, 50)], fill=(255, 255, 255))  
    # draw.text((10, 10), predicted_class, fill=(0,0,0),font = font)
    # img.save(os.path.join('activity_results',f'result_{image_name}'))

# detect_action('images/cooking_woman.jpg')