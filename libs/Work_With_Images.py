import numpy as np
from PIL import Image
import time

def cut_image(startimg, img_rows, img_cols, chenals, step, wSteps, hSteps):
    im_width = startimg.shape[0]
    im_height = startimg.shape[1]
    ni = wSteps*hSteps
    imgs = np.zeros((ni, img_rows, img_cols, chenals))
    print(wSteps, hSteps, ': ',imgs.shape)
    for col in range(wSteps):
        for row in range(hSteps):
            start_wp = col*step
            end_wp = start_wp + img_cols 
            start_hp = row*step 
            end_hp = start_hp + img_rows
            if end_wp > im_width  and end_hp > im_height:
                imgs[row + hSteps*col,:(im_width-start_wp),:(im_height-start_hp),:] = startimg[start_wp:end_wp,start_hp:end_hp,:]
            elif end_wp > im_width:
                imgs[row + hSteps*col,:(im_width-start_wp),:,:] = startimg[start_wp:end_wp,start_hp:end_hp,:]
            elif end_hp > im_height:
                imgs[row + hSteps*col,:,:(im_height-start_hp),:] = startimg[start_wp:end_wp,start_hp:end_hp,:]
            else:
                imgs[row + hSteps*col,:,:,:] = startimg[start_wp:end_wp,start_hp:end_hp,:]            

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
    print(step)
    startimg = Image.open(path_to_image + "\\" + name_of_image)
    chenals = Define_Chenal(startimg)
    im_mode = startimg.mode
    print(startimg.size)
    startimg = np.array(startimg).astype('float32')
    im_width = startimg.shape[0]
    im_height = startimg.shape[1]
    wSteps = int(im_width / step ) + 1 #Довольно грубое разрезание, возможно наличие лишней строки/солбца при кратном делении
    hSteps = int(im_height / step) + 1 #но она будет занулённая, так что всё равно..
    start_time = time.time()
    imgs = cut_image(startimg, img_rows, img_cols, chenals, step, wSteps, hSteps) 
    mins,sex = divmod(time.time() - start_time,60)
    print('Изображения нарезаны - потрачено {M}m : {S:.1f}s. Сохраняю в папку: {P}'.format(M = int(mins), S = sex, P = path_to_dir))
    for i in range(imgs.shape[0]):
        if chenals == 1:
            res = imgs[i].reshape(imgs[i].shape[0], imgs[i].shape[1])
        else:
            res = imgs[i]
        resimg = Image.fromarray(res.astype('uint8'), mode = im_mode)
        resimg = resimg.resize((img_rows,img_cols))
        file_name = path_to_dir + '\\' + str(i+1) + "_" + name_of_image
        resimg.save(file_name)
    
    return
