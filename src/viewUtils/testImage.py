from PIL import Image
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
img = Image.open(BASE_DIR + '/images/1.JPG', 'r')
# img.show()
'''save(filename,format)(保存指定格式的图像)'''
# img.save(BASE_DIR + '/images/1.png', 'png')
'''thumbnail(size,resample)(创建缩略图)'''
# img.thumbnail((50,50),resample=Image.BICUBIC)
# img.show()
'''crop(box)(裁剪矩形区域)'''
# box = (100,100,200,200)
# region = img.crop(box)
# region.show()
# img.crop()
'''point(lut,mode)(对图像像素操作)'''
source = img.split();
R, G, B =0, 1, 2
mask = source[R].point(lambda x: x<100 and 255)
# x<100,return 255,otherwise return 0
out_G = source[G].point(lambda x:x*0.7)
# 将out_G粘贴回来，但是只保留'R'通道像素值<100的部分
source[G].paste(out_G,None,mask)
# 合并成新的图像
im_new = Image.merge(img.mode,source)
im_new.show()
img.show()