x=0
x1=0
score=0
lst=[0,150,320,500,950,2000,5000,10000,40000]
lst2=[200,800,2500,3600,6000]
q=False
w=False
r=False
e=False
t=False
def setup():
    background(0)
    global img,img2,img3,img4,img5
    img = loadImage('1.png')
    img2=loadImage('2.png')
    img3=loadImage('3.png')
    img4=loadImage('4.png')
    img5=loadImage('5.png')
    size(530,530)
def draw():
    global score 
    background(0)
    fill(0,0,255)
    for x in range(0,530,60):
        rect(x,20,50,50,10)
    ##
    stroke(255)
    fill(255)
    for index in range(9):
        text(str(lst[index]),index*61,80)
    line(0,90,530,90)
    stroke(0)
    fill(0)
    ##
    fill(0,255,0)
    for x1 in range(0,500,60):
        rect(x1,100,50,50,10)
    ##
    stroke(255)
    fill(255)
    for index2 in range(5):
        text(str(lst2[index2]),index2*61,160)
    line(0,170,530,170)
    stroke(255)
    fill(255)
    ##
    fill(255)
    text(score,0,10)
    ##
    if q==True:
        image(img,0,360,100,100)
    if w==True:
        image(img2,170,400,100,100) 
    if r==True:
        image(img3,200,270,100,100)
    if e==True:
        image(img4,440,450,100,100)
    if t==True:
        image(img5,70,300,50,50)
def mouseClicked():
    global score,q,w,r,e,t
    if mouseX>0 and mouseX<50 and mouseY>20 and mouseY<70:
        score=score+1
        fill(255)
        text(score,0,10)
    if mouseX>60 and mouseX<110 and mouseY>20 and mouseY<70 and score>=0:
        score=score+1.250
    if mouseX>120 and mouseX<170 and mouseY>20 and mouseY<70 and score>=320:
        score=score+1.800
    if mouseX>180 and mouseX<230 and mouseY>20 and mouseY<70 and score>=500:
        score=score+2
    if mouseX>240 and mouseX<290 and mouseY>20 and mouseY<70 and score>=950:
        score=score+3.100
    if mouseX>300 and mouseX<350 and mouseY>20 and mouseY<70 and score>=2000:
        score=score+4
    if mouseX>360 and mouseX<410 and mouseY>20 and mouseY<70 and score>=5000:
        score=score+5.500
    if mouseX>420 and mouseX<470 and mouseY>20 and mouseY<70 and score>=10000:
        score=score+8 
    if mouseX>480 and mouseX<530 and mouseY>20 and mouseY<70 and score>=40000:
        score=score+10
    ##
    if mouseX>0 and mouseX<50 and mouseY>100 and mouseY<150 and score>=0:#200
        q=True
    if mouseX>60 and mouseX<110 and mouseY>100 and mouseY<150 and score>=0:#800
        w=True
    if mouseX>120 and mouseX<170 and mouseY>100 and mouseY<150 and score>=0:#2500
        r=True
    if mouseX>180 and mouseX<230 and mouseY>100 and mouseY<150 and score>=0:#3600
        e=True
    if mouseX>240 and mouseX<290 and mouseY>100 and mouseY<150 and score>=0:#6000
        t=True
