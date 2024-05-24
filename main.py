import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
from kivy.graphics.texture import Texture

class ImageLoaderApp(App):
    def build(self):
        # Layout utama
        layout = BoxLayout(orientation='vertical')

        # Button untuk memilih gambar
        button = Button(text='Pilih Gambar', size_hint_y=None, height=50)
        button.bind(on_press=self.load_image)

        # Image widget untuk menampilkan gambar
        self.image_widget = Image()

        # Tambahkan widget ke layout
        layout.add_widget(button)
        layout.add_widget(self.image_widget)

        return layout

    def load_image(self, instance):
        # Tampilkan file chooser untuk memilih gambar
        file_chooser = FileChooserListView()
        file_chooser.bind(on_submit=self.load_image_from_path)
        self.root.add_widget(file_chooser)

    def load_image_from_path(self, instance, selection, touch):
        # Ambil path gambar dari objek selection
        path = selection[0]

        # Baca gambar menggunakan OpenCV
        img = cv2.imread(path)
        
        # Konversi gambar menjadi format Kivy Texture
        texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture.blit_buffer(img.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        # Update gambar di widget Image
        self.image_widget.texture = texture

        # Hapus file chooser setelah memilih gambar
        self.root.remove_widget(instance)

        #ekstraksi fitur dari inputan gambar
        print(img)
        # jadikan datanya sebagai inputan X

        # lakukan prediksi di sini

if __name__ == '__main__':
    ImageLoaderApp().run()
