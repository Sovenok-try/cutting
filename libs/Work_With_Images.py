import numpy as np
from PIL import Image

def cut_image(startimg, img_rows, img_cols, chenals, step, wSteps, hSteps):
    im_width = startimg.size[0]
    im_height = startimg.size[1]
    imgPix = startimg.load() #Выгружаются значения пикселей
    ni = wSteps*hSteps
    imgs = np.zeros((ni, img_rows, img_cols, chenals))
    print(wSteps, hSteps, ': ',imgs.shape)
    for w in range(wSteps):
        for h in range (hSteps):
            for i in range(img_rows):
                for j in range (img_cols):
                    if ((w*step + j) < im_width):
                        if((h*step + i) < im_height):
                            if chenals == 1:
                                imgs[w + h*wSteps,i,j] = imgPix[w*step + j, h*step + i]
                            else:
                                for k in range(chenals):
                                    a = imgPix[w*step + j, h*step + i]
                                    imgs[w + h*wSteps,i,j,k] = a[k]
    return imgs

def Define_Chenal(startimg):
    mode = startimg.mode
    if (mode == 'L' or mode=='P'):
        chenals = 1
    elif (mode == "RGB" or mode == 'YCbCr' or mode == "LAB" or mode == 'HSV'):
        chenals = 3
    elif (mode == "RGBA" or mode=="CMYK"):
        chenals = 4

    return chenals



def Processing(path_to_image,name_of_image,path_to_dir,image_size,borderdelta):
    img_rows = image_size #Ширина входных изображений НС
    img_cols = img_rows #Высота входных изображений НС

    step = img_rows -  borderdelta #Шаг смещения при разрезании большой картинки на части img_rows, img_cols - step = области_перекрытия

    startimg = Image.open(path_to_image + "\\" + name_of_image)
    chenals = Define_Chenal(startimg)
    print(startimg.size)
    im_width = startimg.size[0]
    im_height = startimg.size[1]
    wSteps = int(im_width / step ) + 1 #Довольно грубое разрезание, возможно наличие лишней строки/солбца при кратном делении
    hSteps = int(im_height / step) + 1 #но она будет занулённая, так что всё равно..
    imgs = cut_image(startimg, img_rows, img_cols, chenals, step, wSteps, hSteps) 
    print("Изображения нарезаны. Сохраняю в папку: ",path_to_dir)
    for i in range(imgs.shape[0]):
        if chenals == 1:
            res = imgs[i].reshape(imgs[i].shape[0], imgs[i].shape[1])
        else:
            res = imgs[i]
        resimg = Image.fromarray(res.astype('uint8'), mode = startimg.mode)
        resimg = resimg.resize((img_rows,img_cols))
        file_name = path_to_dir + '\\' + str(i+1) + "_" + name_of_image
        resimg.save(file_name)
    
    return
