# import cv2
# import dropbox
# import time 
# import random
# start_time = time.time()
# def take_snapshot():
#     number = random.randint(0,100)
#     videoCaptureObject = cv2.VideoCapture(0)
#     result = True
#     while(result):
#         ret, frame = videoCaptureObject.read()
#         img_name = 'img'+str(number)+'.png'
#         cv2.imwrite(img_name, frame)
#         start_time = time.time()
#         result = False
#     return img_name
#     videoCaptureObject.release()
#     cv2.destroyAllWindows()
# def upload_files(img_name):
#     access_token = 'UiehyGUk8SQAAAAAAAAAAcD2x-Kj2ekufjSahEWBlswTz4NJzy4JjgGv4J_CHMtO'
#     file = img_name
#     file_from = file
#     file_to = '/newfolder/'+(img_name)
#     dbx = dropbox.Dropbox(access_token)
#     with open(file_from, 'rb')as f:
#         dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
#         print('Your desired files have been uploaded to DropBox ')
# def main():
#     while(True):
#         if((time.time()-start_time)>=5):
#             name = take_snapshot()
#             upload_files(name)
# main()