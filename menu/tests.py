from django.test import TestCase
from django.core.files import File
from .models import Menu
import os
# Create your tests here.

    # class ImageModelTest(TestCase):

    # def test_image_model_save_and_retrieve(self):
    #     image1 = Image(
    #         title='burger1',
    #         image=File(open('static/images/burger/1.png','rb'))
    #     )
        
    #     image1.save()
    #     print("image1.image: ", image1)
    #     image2 = Image(
    #         title='burger2',
    #         image=File(open('static/images/burger/2.png','rb'))
    #     )
    #     image2.save()

    #     # все картинки из бд
    #     all_images = Image.objects.all()

    #     #проверка что картинок 2 
    #     self.assertEqual(len(all_images), 2)

    #     #первая картинка это имейдж1
    #     self.assertEqual(all_images[0].title, 
    #                         image1.title
    #                         )
    #     #первая картинка это имейдж1
    #     self.assertEqual(all_images[0].image, 
    #                         image1.image
    #                         )     

    #     #вторая картинка это имейдж1
    #     self.assertEqual(all_images[1].title, 
    #                         image2.title
    #                         )
    #     #вторая картинка это имейдж1
    #     self.assertEqual(all_images[1].image, 
    #                         image2.image
    #                         )   
        
    #     os.remove('media/'+str(image1.image))
    #     os.remove('media/'+str(image2.image))