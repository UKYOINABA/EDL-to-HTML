import codecs
import pandas as pd
import cv2
import os
import math
import html
from flask import Flask,render_template,url_for

from pandas.core import frame

pd.set_option('colheader_justify', 'center')



#####
frameRateList = [60,30,24]
file_url = input("EDL file path---> ")

if os.path.exists(file_url):
    pass
else:
    print("FILE DOES NOT EXIST!")
    exit()

videoPath = input("VIDEO file path---> ")

if os.path.exists(videoPath):
    pass
else:
    print("FILE DOES NOT EXIST!")
    exit()

folderPath = os.path.dirname(videoPath)
in_frameRate = input('FrameRate?---> ')
frameRate = int(round(float((in_frameRate))))
if frameRate in frameRateList:
    pass
else:
    print("INVALID FRAME RATE!")
    exit()


prjName = input('Enter Project Name--->')

html_string = '''
<html>
  <head><title>CUTSHEET</title></head>
  <link rel="stylesheet" type="text/css" href="/Users/kinaco/Documents/Python/EDLtoPDF/df_style.css"/>
  <body>
    {table}
  </body>
</html>.
'''
def TCtoFrame(frameRate,time):
    frameNum = 0
    sepTime = time.split(":")
    frameNum = (frameRate * 60 * int(sepTime[1])) +(frameRate*int(sepTime[2])) + int(sepTime[3])
    return frameNum

def EDLParser(edl_file,frameRate):
    #空のデータフレームを作成
    df = pd.DataFrame({
                    'THUMBNAIL':[],
                    'FILE_NAME':[],
                    'IN_TIME':[],
                    'OUT_TIME':[],
                    'IN_FRAME':[],
                    'OUT_FRAME':[]})

    f = codecs.open(edl_file,'r','shift-jis','ignore')
    lines = f.read().split('\n') #改行コードでParse
    for i, line in enumerate(lines):
        if i == 0:
            previous_line = None
        else:
            previous_line = lines[i - 1]

        if i == len(lines) -1:
            next_item = None
        else:
            next_item = lines[i + 1]
        try:
            if lines[i].split()[2] in "V": #ビデオレイヤのデータのみ抽出
                thumbnail_path = None
                file_name = next_item.split(":")[1].strip("\r") #ファイル名
                in_time = lines[i].split()[6]
                out_time = lines[i].split()[7]
                in_frame = TCtoFrame(frameRate,in_time)
                out_frame = TCtoFrame(frameRate,out_time)
                addRow = pd.DataFrame([thumbnail_path,file_name,in_time,out_time,in_frame,out_frame],index=df.columns).T
                df = df.append(addRow,ignore_index=True)
        except IndexError as e:
            pass
    return df

def saveFrame(videoPath, frame_num, result_path):
    cap = cv2.VideoCapture(videoPath)
    
    if not cap.isOpened():
        return
    os.makedirs(os.path.dirname(result_path),exist_ok=True)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()

    if ret:
        cv2.imwrite(result_path,frame)


def executeSaveFrame(dataFrame):
    for i in range(len(dataFrame)):
        result_path = f'{folderPath}/image/{prjName}_{str(i).zfill(4)}.jpg'
        dataFrame.iat[i,0] = f'<img src="{result_path}" width="200" />'
        frame_num = math.floor((dataFrame.iloc[i,4]+dataFrame.iloc[i,5])*0.5)
        saveFrame(videoPath,frame_num,result_path)

df = EDLParser(file_url,frameRate)
executeSaveFrame(df)
# print(df)

with open(f'{folderPath}/myhtml.html', 'w') as f:
    f.write(html_string.format(table=df.to_html(classes='mystyle',escape=False)))
    print("----DONE----")
