import os
from libs.Work_With_Images import Processing


path_to_image = "D:\\TrainSet\\DataSet - Sew [2022]\\Cyparis\\3w4onm3_test" #Расположение изображения
name_of_image = "cy2_3w4_0316_sewed.jpg"
path_to_dir = "D:\\Cutting\\Try" #Папка, куда сохранять нарезанные изображения
image_size = 150 #Размер получившегося изображения
borderdelta = 0 #Ширина поля перекрытия фрагментов


if not os.path.exists(path_to_image + "\\" + name_of_image):
    print("Изображение " + name_of_image + " не найдено")
else:
    if not os.path.exists(path_to_dir):
        path_to_dir = path_to_image + "\\" + name_of_image[:-4] + "_cut"
        if not os.path.exists(path_to_dir):
            os.mkdir(path = path_to_image + "\\" + name_of_image[:-4] + "_cut")
        
    Processing(path_to_image,name_of_image,path_to_dir,image_size,borderdelta)
