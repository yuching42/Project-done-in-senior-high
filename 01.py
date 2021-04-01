#設計者：北一女中(TFGSH) 10730914 洪于晴(Hung Yu-Ching)
#作品名稱：似是煙火亦似是球，實為天地間的塵埃(Firework?Ball?In fact, it's the dust in the universe.)
#創作理念：想到龍貓動畫中的灰塵精靈，又想到跨年時炫麗的煙火，於是發想出現在這個作品。
#版本：2.8.1
#創作日期：2019/01/06
#授權方式：姓名標示─非商業性─相同方式分享 (http://creativecommons.tw/explore)

#-------START HERE---------------#
from turtle import * 
from random import randint
#-------DEFINE FUNCIOTN----------#
def jump(x,y):
  penup()
  goto(x,y)
  pendown()
def ball(u,n):
  for i in range(360/n):
    fd(u)
    lt(180-n)
#-------MAIN TASK----------------#
speed(0)
Screen().bgcolor('black')
x=-300
y=100
jump(x,y)
#-------START DRAWING------------#
for i in range(4):
  for j in range(6):
    k=randint(1,5)
    if k==1:
      pencolor(236,111,111)
      ball(175,4)
      x=x+150
    elif k==2:
      pencolor(163,123,202)
      ball(175,5)
      x=x+150
    elif k==3:
      pencolor(89,131,217)
      ball(175,6)
      x=x+150
    elif k==4:
      pencolor(242,201,117)
      ball(175,9)
      x=x+150
    else:
      pencolor(106,185,130)
      ball(175,10)
      x=x+150
    jump(x,y)
  y=y-150
  x=-300
  jump(x,y)
#-------END DRAWING--------------#
hideturtle()
done()