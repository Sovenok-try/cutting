import os
from libs.Work_With_Images import Processing


path_to_image = "D:\\Cutting" #Расположение изображения
name_of_image = "HP_220126.ALL_01.JPG"
path_to_dir = "D:\\Cutting\\Cut_images2" #Папка, куда сохранять нарезанные изображения
image_size = 256 #Размер получившегося изображения
borderdelta = 64 #Ширина поля перекрытия фрагментов


if not os.path.exists(path_to_image + "\\" + name_of_image):
    print("Изображение " + name_of_image + " не найдено")
else:
    if not os.path.exists(path_to_dir):
        path_to_dir = path_to_image + "\\" + name_of_image[:-4] + "_cut"
        os.mkdir(path = path_to_image + "\\" + name_of_image[:-4] + "_cut")
        
    Processing(path_to_image,name_of_image,path_to_dir,image_size,borderdelta)