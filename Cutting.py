import os
from libs.Work_With_Images import Processing


path_to_image = "D:\\TrainSet\\Sew-Net\\Data-Set Sew\\Cyparis\\m3on2w3_test" #Расположение изображения
name_of_image = "_sewed_cy2_m3_0088.jpg"
path_to_dir = "D:\\TrainSet\\Sew-Net\\Data-Set Sew\\Cyparis\\m3on2w3_test\\cy2_2w3_0088" #Папка, куда сохранять нарезанные изображения
image_size = 150 #Размер получившегося изображения
borderdelta = 0 #Ширина поля перекрытия фрагментов


if not os.path.exists(path_to_image + "\\" + name_of_image):
    print("Изображение " + name_of_image + " не найдено")
else:
    if not os.path.exists(path_to_dir):
        path_to_dir = path_to_image + "\\" + name_of_image[:-4] + "_cut"
        os.mkdir(path = path_to_image + "\\" + name_of_image[:-4] + "_cut")
        
    Processing(path_to_image,name_of_image,path_to_dir,image_size,borderdelta)
