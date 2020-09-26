# clc() ##command창에 표시된 코드들 사라지게해
#-*- encoding: utf8 -*-
import os
import numpy as np
import struct
# clear(mstring('all'))
# close(mstring('all'))

# This code save already computed C3D features into 32 (video features) segments.
# We assume that C3D features for a video are already computed. We use
# default settings for computing C3D features, i.e., we compute C3D features for
# every 16 frames and obtain the features from fc6.

import struct

def read_bin(input_file):
# input_file = open(r'.\normal_video_001\000032.fc6-1','rb')
    input_file = open(input_file,'rb')
    try:
        sizes = [struct.unpack('i',input_file.read(4))[0] for i in range(5)]
        m = np.prod(sizes)
        data = [struct.unpack('f',input_file.read(4))[0] for i in range(m)]
    finally:
        input_file
    feature_vector = np.array(data)

    return feature_vector, feature_vector.shape

C3D_Path = r'C:\Users\seong\Desktop\32segment\normal_output'
C3D_Path_Seg = r'C:\Users\seong\Desktop\32segment\output'

if not os.path.isdir(C3D_Path_Seg):
    os.mkdir(C3D_Path_Seg)

print('DONE')

All_Folder = os.listdir(C3D_Path)
# All_Folder = All_Folder[3:end]
subcript = '_C.txt'

for ifolder in All_Folder:
    #% START 1 LOOP WITH 1 FC FOLDER, ex: Abuse028 has N=1392 frames

    Folder_Path = str(C3D_Path) + "\\" + str(ifolder)
    #Folder_Path is path of a folder which contains C3D features (for every 16 frames) for a paricular video.
    # N=1392 frames --> it has [1392/16] = 88 fc6-1 files

    AllFiles = os.listdir(Folder_Path) ##"/.fc6-1 확장자 파일 싹다 리스트로 반환"
    # fc6-1 files in feature directory, each file = a clip in video
    # one clip = 16 frames

    if len(AllFiles) == 0:
        print("no fc6-1 file in path")
        continue
        
    feature_vector = np.zeros((len(AllFiles), 4096))
    # each fc6-1 = 1 clips 16 frames = 4096-d ==> Total is [N/16]=88 clips like that
    #% Iterate each fc6-1 file (16 frames each)
    for ifile in range(0,len(AllFiles)):
        FilePath =Folder_Path + '\\' + AllFiles[ifile]

        data,_ = read_bin(FilePath)
        _,s = read_bin(FilePath)
        feature_vector[ifile]=data #% 1 column 4096-d in 88x4096 is assign by 1 clip feature (4096)

        # clear(mstring('data')) # clear라는 변수를 매트랩 내에서 삭제

    #% At this point, Feature vector is filled with all actual data from
    # all 16-frame clips in video, each clip is 4096-d, therefore 88x4096
    # is now filled with actual data
    # if sum(sum(feature_vector, [])) == 0: ## 고쳐야됨 : 각 열의 합인 한 행짜리 행렬로
    #     print('error1')

        # Write C3D features in text file to load in
        # Training_AnomalyDetector_public ( You can directly use .mat format if you want).
        txt_file_name = C3D_Path_Seg + '/' + ifolder +subcript
        # feature txt name i.e Abuse028_x264_C.txt

    # if exist(txt_file_name, 'file'):
    #     continue

    fid1 = open(txt_file_name, 'w')
    ## sum(x,1) = sum vertically (column)
    ## sum(x,2) = sum horizontally (row)
    # if not isempty(find(sum(Feature_vect, 2) == 0)): # sum row --> 88x4096 results in 88 rows
    #     # k = find(X,n)은 X의 0이 아닌 요소에 대응하는 처음 n개의 인덱스를 반환합니다
    #     print('error2')


    # if not isempty(find(isnan(Feature_vect(mslice[:])))):
    #     print('error3')

    # if not isempty(find(Feature_vect(mslice[:]) == Inf)):
    #     print('error4')

        #% 32 Segments

    Segments_Features = np.zeros((32, 4096))    #32 row, 4096 column
    thirty2_shots = np.linspace(1, len(AllFiles), 33).round(0)
    # thirty2shots = divide 88 frames to 33 segment, start from 1 to 88
    # SO: thirty2shots = [1 , 4, 6, 10, ..... 83, 85, 88], total elements
    # is 33, vector 1x33
    count = -1
    #% WRITE 88x4096 TO 32x4096
    for ishots in range(0,len(thirty2_shots) - 1):                                   # ishorts starts from 1 to 32
        ss = int(thirty2_shots[ishots] )                                   # start clip index in 88x4096
        ee = int(thirty2_shots[ishots + 1] - 1)                             # end clip index in 88x4096
        
        # print(ss,ee,'llllll')
        if ishots == len(thirty2_shots):
            ee = int(thirty2_shots[ishots + 1])
            #% THIS IS A FEATURE FOR 1 SEGMENT
            #ALL BELOW CASE, temp_vect is always 4096-d based on value of start ss and end ee index
        if ss == ee:
            temp_vect = feature_vector[ss] ##ss번째 행 벡터 추출     # ss==ee --> get 1 vector 4096-d from 88x4096

        elif ee < ss:
            temp_vect = feature_vector[ss]  # ee < ss --> get 1 vector 4096-d from 88x4096

        else:
            temp_vect = feature_vector[ss:ee].mean(axis=0) ##각 열의 평균값을 가진 1*4096행 추출
            # for i in range(ss,ee):
                # feature_vector
            # ss < ee --> get all clip vectors from ss to ee (ex: 3 vectors) from 88x4096
            # origin feature, than take mean value of all (i.e 3 vectors) that vectors to
            # get a new one has 4096-d (shape of result is shape of row when get mean a
            # matrix)
            #mean a vector = mean of each column = sum column/total row -->
            #shape = number of row (=4096) after this mean operation
        # print(temp_vect.shape)
        #% AFTER HAS 1 SEGMENT FEATURE,  CALCULATE NORM-2 (L2)
        temp_vect = temp_vect / np.linalg.norm(temp_vect)
        # temp_vect = temp_vect / np.norm(temp_vect)   #% divide by norm-2 (L2) of vector (Euclidean norm)=cumsum(sqrt(x[i]^2))                                     # divide by norm-2 (L2) of vector (Euclidean norm)=cumsum(sqrt(x[i]^2))

        # if np.linalg.norm(temp_vect) == 0:
        #     print('error5')

        count = count + 1 # next segment (max=32)
        Segments_Features[count]= temp_vect # push each segment feature to final 32 video segments feature

#verify

    # if not isempty(find(sum(Segments_Features, 2) == 0)):
    #     print('error6')

    # if not isempty(find(isnan(Segments_Features(mslice[:])))):
    #     print('error7')


    # if not isempty(find(Segments_Features(mslice[:]) == Inf)):
    #     print('error8')


        # save 32 segment features in text file ( You can directly save and load .mat file in python as well).
    print(Segments_Features)
    print(Segments_Features.shape)

    for i in range(0,Segments_Features.shape[0]):
        feat_text = str(Segments_Features[i].tolist())
        fid1.write(feat_text)
        fid1.write('\n')

    fid1.close()

