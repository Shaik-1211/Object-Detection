from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import os
from ultralytics import YOLO

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'Open Image'
        size_hint_y: None
        height: '48dp'
        on_release: app.open_filechooser()
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def open_filechooser(self):
        print("Opening file chooser")  # Debug print
        content = FileChooserIconView()

        content.bind(selection=self.file_selected)
        self.popup = Popup(title="Open Image", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def file_selected(self, filechooser, selection):
        print("Selection event triggered")  # Debug print
        print("Selection: ", selection)  # Debug print
        self.load_image(filechooser, selection)

    def load_image(self, filechooser, selection):
        if selection:
            image_path = selection[0]
            print("Loading image: ", image_path)  # Debug print
            self.popup.dismiss()  # Close the popup after selecting it
            self.root.clear_widgets()

            processed_image = self.process_image(image_path)
            print(f'processed image is {processed_image}')

            img = Image(source=processed_image)
            self.root.add_widget(img)
            btn = Button(text='Open Image', size_hint_y=None, height='48dp')
            btn.bind(on_release=self.open_filechooser)
            self.root.add_widget(btn)
        else:
            print("No file selected")  # Debug print
        
    def process_image(self, image_path):
        model = YOLO('yolov8n.pt')
        results = model(image_path)
        results_folder ='results'
        if not os.path.exists(results_folder):
            os.makedirs(results_folder)
        filename = os.path.splitext(os.path.basename(image_path))[0]
        filename = filename + '.jpg'

        for result in results:
            result.save(filename)
        return filename

if __name__ == '__main__':
    MainApp().run()
