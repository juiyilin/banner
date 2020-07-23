from PIL import Image, ImageDraw, ImageFont
import os
from time import sleep

# 檢查輸入之資訊檔是否存在
if not os.path.exists('setting.txt'):
    print('setting.txt不存在\n建立檔案(內容如下1-6)')
    sleep(2)
    with open('setting.txt','w',encoding='utf8') as txt:
        txt.write('1. 出刊年分(ex:一○九):一○九\n')
        txt.write('2. 出刊月分(ex:5):5\n') 
        txt.write('3. 單or雙月刊(單月刊1，雙月刊2，只產生單張0):0\n') 
        txt.write('4. 發行人:XXX\n')
        txt.write('5. 總編輯:XXX\n')
        txt.write('6. 主編:XXX\n')
        txt.write('7. 開始期數(ex:247):247\n')
    

with open('setting.txt','r',encoding='utf8') as txts:
    txts=txts.readlines()

#確認內容
for t in txts:
    print(t,end='')
check = input('以上內容正確嗎?[y/n]')
while check!='y' and check!='n':
    print('請輸入 "y" 或 "n"')
    check = input('內容正確嗎?[y/n]')
    
if check=='n':
    print('內容不正確，請修改setting.txt再重新執行')
    input('按Enter結束程式')
else:
    if check=='y':
        #字串處理
        for i in range(len(txts)):
            txts[i]=txts[i].strip().split(':')[-1]

        #阿拉伯數字轉換
        arabic_num=list(range(1,13))
        chinese='一二三四五六七八九十'
        chinese_num=[]
        for c in chinese:
            chinese_num.append(c)
        chinese_num.extend(['十一','十二'])
        convert=dict(zip(arabic_num,chinese_num))

        #單月或雙月刊list
        release=[]
        if txts[2]=='0':
            endmonth=int(txts[1])+1
            step=1
        else:
            endmonth=13
            step=int(txts[2])
        for i in range(int(txts[1]),endmonth,step):
            release.append(convert[i])

        #寫入圖片
        for i,n in enumerate(release):
            image=Image.open('APECEpaperTitle (空白).png')
            imdr=ImageDraw.Draw(image)

            #出刊日
            date_font=ImageFont.truetype(font='msjh.ttc', size=13)
            imdr.text(xy=(418, 195), text=txts[0]+'年'+n+'月出刊', fill='white',font = date_font)


            human_name_font = ImageFont.truetype(font='msjhbd.ttc', size=11)
            #發行人
            imdr.text(xy=(86, 271), text=txts[3], fill='white',font=human_name_font)
            #總編輯
            imdr.text(xy=(180, 271), text=txts[4], fill='white',font=human_name_font)
            #主編
            imdr.text(xy=(267, 271), text=txts[5], fill='white',font=human_name_font)


            #期數
            issue_font = ImageFont.truetype(font='ARIALN.TTF', size=39)
            imdr.text(xy=(677, 278), text=str(int(txts[-1])+i), fill='white',font=issue_font)

            #存檔
            if not os.path.exists('banner'):
                os.mkdir('banner')
            image.save('banner/'+str(int(txts[1])+int(txts[2])*i)+'月banner.png')
            print('saved 內文banner',str(int(txts[1])+int(txts[2])*i)+'月.png')
        
        print('儲存於banner資料夾')
        sleep(2)
        input('按Enter關閉程式')
