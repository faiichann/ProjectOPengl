if __name__ == '__build__':
	raise Exception
import sys
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ('''
ERROR: PyOpenGL not installed properly.  
        ''')
  sys.exit()

w,h=1280, 720
rot = 0
speed = 20
sum_rot_updown = 0
current_mv_mat = (GLfloat * 16)()

def init():
   mat_ambient =[0.7,0.7,0.7,0.1]
   mat_diffuse =[0.5,0.5,0.5,1.0]
   mat_specular =[1.0,1.0,1.0,1.0]
   mat_shininess =[50.0]

   glMaterialfv(GL_FRONT,GL_AMBIENT,mat_ambient)
   glMaterialfv(GL_FRONT,GL_SPECULAR,mat_specular)
   glMaterialfv(GL_FRONT,GL_SHININESS,mat_shininess)

   light_ambient =  [0.0, 0.0, 0.0, 1.0]
   light_diffuse =  [1.0, 1.0, 1.0, 1.0]
   light_specular =  [1.0, 1.0, 1.0, 1.0]
   light_position =  [1.0, 1.0, 1.0, 0.0]

   glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
   glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
   glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
   glLightfv(GL_LIGHT0, GL_POSITION, light_position)
   
   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_LIGHT1)
   glEnable(GL_LIGHT2)
   glEnable(GL_LIGHT3)
   glEnable(GL_LIGHT4)
   glEnable(GL_LIGHT5)
   glEnable(GL_DEPTH_TEST)
   glEnable(GL_NORMALIZE)
   glEnable(GL_TEXTURE_2D)

def set_texture():
    #	glTexImage2D(GL_TEXTURE_2D,0,3,11,12,0,GL_RGB,GL_UNSIGNED_BYTE, image)
	glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)

def wall(thickness) :   
#function to create the walls with given thickness
    
    glScalef(5,5,5)
    glPushMatrix()
    glTranslated(0.5,0.5*thickness,0.5)
    glScaled(1.0,thickness,1.0)
    glutSolidCube(1.0)
    glPopMatrix()

def table():
   glPushMatrix()
     #ขาโต๊ะ 1
   glPushMatrix()
   glTranslatef(2.5,0.12,2.5)
   glRotate(360,1,0,0)
   glScalef(0.5,2.0,0.5)
   glColor3f(0.1,0,0)
   glutSolidCube (1)
   glPopMatrix ()

   #ขาโต๊ะ 2
   glPushMatrix()
   glTranslatef(-1.5,0.12,2.5)
   glRotate(360,1,0,0)
   glScalef(0.5,2.0,0.5)
   glColor3f(0.1,0,0)
   glutSolidCube (1)
   glPopMatrix ()

   #ขาโต๊ะ 3
   glPushMatrix()
   glTranslatef(2.5,0.12,-1.5)
   glRotate(360,1,0,0)
   glScalef(0.5,2.0,0.5)
   glColor3f(0.1,0,0)
   glutSolidCube (1)
   glPopMatrix ()

   #ขาโต๊ะ 4
   glPushMatrix()
   glTranslatef(-1.5,0.12,-1.5)
   glRotate(360,1,0,0)
   glScalef(0.5,2.0,0.5)
   glColor3f(0.1,0,0)
   glutSolidCube (1)
   glPopMatrix ()
 

   #พื้นโต๊ะ
   glPushMatrix()
   glTranslated(0.5,1.2,0.5)
   glScaled(3,0.2,3)
   glColor3f(0,0.5,0.5)
   glutSolidCube(1.5)
   glPopMatrix()

   glPopMatrix()

def chair():
   glPushMatrix()
   #ขาเก้าอี้ 1
   glPushMatrix()
   glScalef(0.5,1,0.5)
   glColor3f(2,0.5,1)
   glutSolidCube (1)
   glPopMatrix ()

   #ขาเก้าอี้ 3
   glPushMatrix()
   glTranslatef(1,0,0)
   glScalef(0.5,1,0.5)
   glColor3f(2,0.5,1)
   glutSolidCube (1)
   glPopMatrix ()

   #ขาเก้าอี้ 3
   glPushMatrix()
   glTranslatef(1,0,1)
   glScalef(0.5,1,0.5)
   glColor3f(2,0.5,1)
   glutSolidCube (1)
   glPopMatrix ()

   #ขาเก้าอี้ 4
   glPushMatrix()
   glTranslatef(0,0,1)
   glScalef(0.5,1,0.5)
   glColor3f(2,0.5,1)
   glutSolidCube (1)
   glPopMatrix ()

   #พื้นเก้าอี้
   glPushMatrix()
   glTranslated(0.5,0.5,0.5)
   glScaled(3,0.2,3)
   glColor3f(0,0.5,1)
   glutSolidCube(0.5)
   glPopMatrix()

   #ฝาเก้าอี้
   glPushMatrix()
   glTranslated(0.5,1,-0.125)
   glRotatef(90,1,0,0)
   glScaled(3,0.5,3)
   glColor3f(0.5,0.5,0.5)
   glutSolidCube(0.5)
   glPopMatrix()
   glPopMatrix()

def closet():
   
   glPushMatrix()
   glColor(0.5,0.5,0.1)
   glTranslated(0.605,0.78,0.5)
   glRotate(30,0,1,0)
   glScalef(0.5,0.84,0.05)
   glutSolidCube (1)
   glPopMatrix()
   
   glPushMatrix()
   glColor(1,0,0.5)
   glTranslated(0.6644,1.18,0.605)
   glRotate(30,0,1,0)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(1,0,0.5)
   glTranslated(0.6644,1.02,0.605)
   glRotate(30,0,1,0)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(1,0,0.5)
   glTranslated(0.6644,0.86,0.605)
   glRotate(30,0,1,0)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(1,0,0.5)
   glTranslated(0.6644,0.7,0.605)
   glRotate(30,0,1,0)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(1,0,0.5)
   glTranslated(0.6644,0.54,0.605)
   glRotate(30,0,1,0)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(1,0,0.5)
   glTranslated(0.6644,0.38,0.605)
   glRotate(30,0,1,0)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(0.5,0.5,0.1)
   glTranslated(0.866,0.785,0.48)
   glRotate(30,0,1,0)
   glScalef(0.03,0.846,0.27)
   glutSolidCube (1)
   glPopMatrix()

   glPushMatrix()
   glColor(0.5,0.5,0.1)
   glTranslated(0.449,0.785,0.72)
   glRotate(30,0,1,0)
   glScalef(0.03,0.846,0.27)
   glutSolidCube (1)
   glPopMatrix()

def rubber():
   glPushMatrix()
   glColor(1,0,0)
   glTranslated(0.605,0.78,0.5)
   glRotate(30,0,1,0)
   glScalef(0.05,0.05,0.05)
   glutSolidTorus(0.8,2,30,30)
   glPopMatrix()

   glPushMatrix()
   glColor(1,1,1)
   glTranslated(0.605,0.88,0.5)
   glRotate(110,0,1,0)
   glScalef(0.05,0.05,0.05)
   glutSolidTorus(0.5,0.5,15,30)
   glPopMatrix()

   glPushMatrix()
   glColor(1,1,1)
   glTranslated(0.605,0.68,0.5)
   glRotate(110,0,1,0)
   glScalef(0.05,0.05,0.05)
   glutSolidTorus(0.5,0.5,15,30)
   glPopMatrix()

   glPushMatrix()
   glColor(1,1,1)
   glTranslated(0.69,0.79,0.45)
   glRotate(100,1,0,0)
   glScalef(0.05,0.05,0.05)
   glutSolidTorus(0.5,0.5,15,30)
   glPopMatrix()

   glPushMatrix()
   glColor(1,1,1)
   glTranslated(0.52,0.79,0.55)
   glRotate(100,1,0,0)
   glScalef(0.05,0.05,0.05)
   glutSolidTorus(0.5,0.5,15,30)
   glPopMatrix()

def lamp():
   #ฐานรอง
   glPushMatrix()
   glTranslatef(0,0,0)
   glRotatef(90,0.5,0,0)
   glScalef(0.2,0.2,0.1)
   glColor3f(2,0.5,1)
   glutSolidCylinder(1,1,32,1)
   glPopMatrix ()

   #แท่น
   glPushMatrix()
   glTranslatef(0,0.7,0)
   glRotatef(90,0.5,0,0)
   glScalef(0.04,0.04,0.7)
   glColor4f(1,1,0,0)
   glutSolidCylinder(1,1,32,1)
   glPopMatrix ()

   #โคม
   glPushMatrix()
   glTranslatef(0,1,0)
   glRotatef(90,0.5,0,0)
   glScalef(0.3,0.3,0.4)
   glColor4f(1,0.5,0,0)
   glutSolidCylinder(1,1,32,1)
   glPopMatrix ()

def window():
        #บน
   glPushMatrix()
   glColor(1,0,0.5)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.67,1.2,0.61)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

   #ล่าง
   glPushMatrix()
   glColor(1,0,0.5)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.67,0.54,0.61)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

    
   #ขวา
   glPushMatrix()
   glColor(0.5,0.5,0.1)
   glTranslated(1,0.95,0.69)
   glScalef(0.03,0.7,0.2)
   glutSolidCube (1)
   glPopMatrix()
#ซ้าย
   glPushMatrix()
   glColor(0.5,0.5,0.1)
   glTranslated(0.5,0.95,0.69)
   glScalef(0.03,0.7,0.2)
   glutSolidCube (1)
   glPopMatrix()

   #กลางตั้ง
   glPushMatrix()
   glColor(0.5,0.5,0.1)
   glTranslated(0.75,0.95,0.69)
   glScalef(0.03,0.7,0.2)
   glutSolidCube (1)
   glPopMatrix()

   #กลางนอน
   glPushMatrix()
   glColor(1,0,0.5)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.67,0.85,0.61)
   glScalef(0.5,0.04,0.2)
   glutSolidCube(1)
   glPopMatrix()

def cup():
             #แก้ว
   glPushMatrix()
   glTranslatef(0,1,1)
   glRotatef(90,0.5,0,0)
   glScalef(0.2,0.2,0.4)
   glColor4f(0,1,1,1)
   glutSolidCylinder(1,1,32,1)
   glPopMatrix ()
   
       #หูแก้ว
   glPushMatrix()
   glTranslatef(0.1,0.8,1)
   glScalef(0.3,0.2,0.4)
   glColor3f(0.5,1,1)
   glutSolidTorus(0.1,0.5,20,30)
   glPopMatrix ()

def sleep():
   glPushMatrix()
   glColor(1,0,1)
   glTranslated(0.5,0.9,0.6)
   glRotate(90,0,1,0)
   glScalef(0.2,0.05,0.5)
   glutSolidCylinder(1,1,30,30)
   glPopMatrix()

   glPushMatrix()
   glColor(1,1,0)
   glTranslated(0.68,0.83,0.6)
   glRotate(90,0,1,0)
   glScalef(0.5,0.15,0.7)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(0,1,0)
   glTranslated(0.38,0.91,0.6)
   glRotate(90,0,1,0)
   glScalef(0.1,0.03,0.1)
   glutSolidCylinder(1,1,30,30)
   glPopMatrix()

   glPushMatrix()
   glColor(1,0,0)
   glTranslated(0.5,0.9,0.6)
   glRotate(90,0,1,0)
   glScalef(0.21,0.06,0.2)
   glutSolidCylinder(1,1,30,30)
   glPopMatrix()

def tv():
       
   glPushMatrix()
   glColor(1,0,1)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.605,0.78,0.5)
   glRotate(90,1,0,0)
   glScalef(0.5,0.02,0.3)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(1,1,0)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.605,0.6,0.5)
   glRotate(90,1,0,0)
   glScalef(0.3,0.05,0.02)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(0,1,1)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.605,0.62,0.5)
   glRotate(90,1,0,0)
   glScalef(0.05,0.02,0.02)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor(0.5,0.5,0.5)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.605,0.78,0.49)
   glRotate(90,1,0,0)
   glScalef(0.48,0.02,0.25)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor3f(0.1,0,0)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.605,0.55,0.5)
   glRotate(90,1,0,0)
   glScalef(0.55,0.2,0.05)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor3f(0,0.1,0.1)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.605,0.55,0.5)
   glRotate(90,1,0,0)
   glScalef(0.02,0.2,0.02)
   glutSolidCube(1)
   glPopMatrix()

   glPushMatrix()
   glColor3f(2,0.5,1)
   glTranslatef(0.08,0.08,0.08)
   glTranslated(0.605,0.52,0.5)
   glRotate(90,1,0,0)
   glScalef(0.5,0.15,0.15)
   glutSolidCube(1)
   glPopMatrix()

def sofa():
       #พื้นโซฟา
   glPushMatrix()
   glTranslated(0.5,0.3,0.5)
   glScaled(3,0.6,3)
   glColor3f(1,0.5,0)
   glutSolidCube(0.5)
   glPopMatrix()

        #ฝาโซฟา
   glPushMatrix()
   glTranslated(0.5,1,-0.125)
   glRotatef(90,1,0,0)
   glScaled(3,0.5,3)
   glColor3f(0.5,0.5,0.5)
   glutSolidCube(0.5)
   glPopMatrix()

       #พื้นโซฟา2
   glPushMatrix()
   glTranslated(-0.5,0.3,0.5)
   glScaled(3,0.6,3)
   glColor3f(1,0.5,0)
   glutSolidCube(0.5)
   glPopMatrix()

        #ฝาโซฟา2
   glPushMatrix()
   glTranslated(-0.5,1,-0.125)
   glRotatef(90,1,0,0)
   glScaled(3,0.5,3)
   glColor3f(0.5,0.5,0.5)
   glutSolidCube(0.5)
   glPopMatrix()

        #ซ้าย
   glPushMatrix()
   glTranslated(-1.4,0.3,0.5)
   glRotatef(90,0,0,1)
   glScaled(3,0.6,3)
   glColor3f(1,0,1)
   glutSolidCube(0.5)
   glPopMatrix()

        #ขวา
   glPushMatrix()
   glTranslated(1.4,0.3,0.5)
   glRotatef(90,0,0,1)
   glScaled(3,0.6,3)
   glColor3f(1,0,1)
   glutSolidCube(0.5)
   glPopMatrix()

def bun6():
       glColor3f(0.1,0,0.1)
       wall(0.1)
   
def bun2():
       glColor3f(0.5,0.5,0.5)
       wall(0.1)

def tree():
       #ต้นไม้
   glPushMatrix()
   glTranslatef(0,0.7,0)
   glRotatef(90,0.5,0,0)
   glColor3f(0,1,0)
   glutSolidSphere(0.27,15,15)
   glPopMatrix ()

   #ต้นไม้
   glPushMatrix()
   glTranslatef(0,0.8,0.2)
   glRotatef(90,0.5,0,0)
   glColor3f(0.0,0.2,0.0)
   glutSolidSphere(0.23,15,15)
   glPopMatrix ()

   #ต้นไม้
   glPushMatrix()
   glTranslatef(0,0.62,-0.2)
   glRotatef(90,0.5,0,0)
   glColor3f(0.0,0.5,0.0)
   glutSolidSphere(0.18,15,15)
   glPopMatrix ()

   #ฐานรองล่าง
   glPushMatrix()
   glTranslatef(0,-0.2,0)
   glRotatef(90,0.5,0,0)
   glScalef(0.3,0.25,0.1)
   glColor3f(0.5,1,1)
   glutSolidCylinder(0.8,1,32,1)
   glPopMatrix ()

   #ฐานรองบน
   glPushMatrix()
   glTranslatef(0,0.2,0)
   glRotatef(90,0.5,0,0)
   glScalef(0.3,0.3,0.1)
   glColor3f(0.5,0.5,0.5)
   glutSolidCylinder(0.85,1,32,1)
   glPopMatrix ()

   #แท่น
   glPushMatrix()
   glTranslatef(0,0.7,0)
   glRotatef(90,0.5,0,0)
   glScalef(0.04,0.04,0.5)
   glColor3f(1,0,1)
   glutSolidCylinder(1,1,32,1)
   glPopMatrix ()

   #โคม
   glPushMatrix()
   glTranslatef(0,0.2,0)
   glRotatef(90,0.5,0,0)
   glScalef(0.5,0.5,0.4)
   glColor3f(0.1,0.1,0)
   glutSolidCylinder(0.4,1,32,1)
   glPopMatrix ()
   
def first():
       glColor3f(0,0.2,0.3)
       wall(0.2)

def display():
   global rot,speed,sum_rot_updown,current_mv_mat,clock

   glPushMatrix()
   glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
   glLoadIdentity()
   glRotatef(sum_rot_updown, 1, 0, 0)
   glMultMatrixf(current_mv_mat)
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   gluLookAt(2.0,2.0,2.0,0.0,0.2,0.0,0.0,1.0,0.0)

   glPushMatrix()

   glPushMatrix() #table

   glTranslated(0.5,1,4.3)
   glRotated(0,0,0,0)
   glScalef(0.2,0.2,0.2)
   table()
   glPopMatrix()

   glPushMatrix() #chair 1
   glTranslated(1.3,1.1,4.3)
   glRotated(-90,0,1,0)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #chair 2
   glTranslated(0.5,1.1,3.7)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #teapot
   glTranslated(0.5,1.35,2.5)
   glColor3f(0.1,0.1,0.1)
   glutSolidTeapot(0.15)
   glPopMatrix()

   glPushMatrix() #table 2
   glTranslated(0.5,1,2.4)
   glScalef(0.2,0.2,0.2)
   table()
   glPopMatrix()

   glPushMatrix() #chair 2.1
   glTranslated(1.3,1.1,2.4)
   glRotated(-90,0,1,0)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #chair 2.2
   glTranslated(0.5,1.1,1.9)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #chair 2.3
   glTranslated(0.7,1.1,3.1)
   glRotated(-180,0,1,0)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()
   

   glPushMatrix() #table 3
   glTranslated(2.5,1,2.4)
   glScalef(0.2,0.2,0.2)
   table()
   glPopMatrix()

   glPushMatrix() #chair 3.1
   glTranslated(3.3,1.1,2.4)
   glRotated(-90,0,1,0)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #chair 3.2
   glTranslated(2.5,1.1,1.9)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #chair 3.3
   glTranslated(2.7,1.1,3.1)
   glRotated(-180,0,1,0)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #cup
   glTranslated(2.9,1,4)
   glScalef(0.5,0.5,0.5)
   cup()
   glPopMatrix()

   glPushMatrix() #cup 2
   glTranslated(2.9,1,2.3)
   glScalef(0.5,0.5,0.5)
   cup()
   glPopMatrix()

   
   glPushMatrix() #table 4
   glTranslated(2.5,1,4.3)
   glRotated(0,0,0,0)
   glScalef(0.2,0.2,0.2)
   table()
   glPopMatrix()

   glPushMatrix() #chair 4.1
   glTranslated(3.3,1.1,4.3)
   glRotated(-90,0,1,0)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #chair 4.2
   glTranslated(2.5,1.1,3.7)
   glScalef(0.2,0.2,0.2)
   chair()
   glPopMatrix()

   glPushMatrix() #closet
   glTranslated(-1.0,0.5,0.75)
   glRotated(60,0,1,0)
   glScalef(1.3,1.3,1.3)
   closet()
   glPopMatrix()

   glPushMatrix() #rubber
   glTranslated(-1.6,2.8,2.5)
   glRotated(60,0,1,0)
   glScalef(2.2,2.2,2.2)
   rubber()
   glPopMatrix()

   glPushMatrix() #sleep
   glTranslated(2,1.6,-0.1)
   glRotated(270,0,1,0)
   glScalef(2.2,2.2,2.2)
   sleep()
   glPopMatrix()

   glPushMatrix() #TV
   glTranslated(4,2,1.5)
   glRotated(180,0,1,0)
   glScalef(2.2,2.2,2.2)
   tv()
   glPopMatrix()

   glPushMatrix() #Sofa
   glTranslated(2.8,3.4,2.2)
   glRotated(180,0,1,0)
   glScalef(0.3,0.3,0.3)
   sofa()
   glPopMatrix()


   glPushMatrix() #lamp
   glTranslated(0.5,1.35,4.4)
   glRotated(60,0,1,0)
   glScalef(0.5,0.5,0.5)
   lamp()
   glPopMatrix()


   glPushMatrix()
   glTranslated(0.25,0.42,0.35)
   glPopMatrix()

   glPushMatrix()
   glTranslated(0.4,0,0.4)   
   glPopMatrix()

   glPushMatrix() #tree
   glTranslated(4.5,3.4,0.2)
   glRotated(-90,0,1,0)
   glScalef(0.5,0.5,0.5)
   tree()
   glPopMatrix()

   glPushMatrix() #tree2
   glTranslated(4.5,1.25,0.3)
   glRotated(-90,0,1,0)
   glScalef(0.5,0.5,0.5)
   tree()
   glPopMatrix()

   glPushMatrix() #tree3
   glTranslated(3.5,1.25,0.3)
   glRotated(-90,0,1,0)
   glScalef(0.5,0.5,0.5)
   tree()
   glPopMatrix()

   glPushMatrix() #tree4
   glTranslated(2.5,1.25,0.3)
   glRotated(-90,0,1,0)
   glScalef(0.5,0.5,0.5)
   tree()
   glPopMatrix()
   
   glPushMatrix() #tree5
   glTranslated(1.5,1.25,0.3)
   glRotated(-90,0,1,0)
   glScalef(0.5,0.5,0.5)
   tree()
   glPopMatrix()

   glPushMatrix() #tree6
   glTranslated(1.2,3.4,0.3)
   glRotated(-90,0,1,0)
   glScalef(0.5,0.5,0.5)
   tree()
   glPopMatrix()

   glPushMatrix() #บันได 1
   glTranslated(3.95,2.8,0)
   glScalef(0.2,1,0.5)
   glColor3f(0,0.5,1)
   wall(0.1)
   glPopMatrix()

   glPushMatrix() #บันได 2
   glTranslated(3.95,2.4,1.9)
   glScalef(0.2,1,0.2)
   bun6()
   glPopMatrix()

   glPushMatrix() #บันได 3
   glTranslated(3.95,2.1,2.3)
   glScalef(0.2,1,0.2)
   glColor3f(0,0.5,1)
   bun2()
   glPopMatrix()

   glPushMatrix() #บันได 4
   glTranslated(3.95,1.8,2.7)
   glScalef(0.2,1,0.2)
   bun6()
   glPopMatrix()

   glPushMatrix() #บันได 5
   glTranslated(3.95,1.4,3.1)
   glScalef(0.2,1,0.2)
   glColor3f(0,0.5,1)
   bun2()
   glPopMatrix()

   glPushMatrix() #บันได 6
   glTranslated(3.95,1.0,3.5)
   glScalef(0.2,1,0.2)
   bun6()
   glPopMatrix()

   glPushMatrix() #second floor
   glColor3f(0.5,1,1)
   glTranslated(0,3.2,0)
   glScalef(0.8,1,0.5)
   wall(0.025)
   glPopMatrix()
   
   glPushMatrix() #first floor
   first()
   glPopMatrix()

   glPushMatrix()  #window1
   glTranslated(-0.6,1.35,5)
   glRotated(90,0,1,0)
   glScalef(1,1,1)
   window()
   glPopMatrix()

   glPushMatrix()  #window2
   glTranslated(-0.6,1.35,3.3)
   glRotated(90,0,1,0)
   glScalef(1,1,1)
   window()
   glPopMatrix()
   
   glPushMatrix()  #wall left
   glColor3f(0,0.5,0.5)
   glRotated(-90.0,1.0,0.0,0.0)
   wall(0.05)
   glPopMatrix()

   glRotated(90.0,0.0,0.0,180.0)  #wall right
   glColor3f(0,0.1,0.1)
   wall(0.05)
   glPopMatrix()

   glPopMatrix()

   glFlush()


def reshape(w, h):
   glViewport(0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()
   # winlet=1.0
   gluPerspective(45, (w/h), 0.1, 50.0)
   # glOrtho(-winlet*64/48,winlet*64/48.0,-winlet*64/48,winlet*64/48,0.6,100.0)
   # if w <= h:
   #    glOrtho(-2.5, 2.5, -2.5*h/w, 
   #             2.5*h/w, -10.0, 10.0)
   # else: 
   #    glOrtho(-2.5*w/h, 
   #             2.5*w/h, -2.5, 2.5, -10.0, 10.0)
   # glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
   # glLoadIdentity()

   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()


def keyboard(key, x, y):
   global rot,speed,sum_rot_updown,current_mv_mat
   #WASD
   if key == b'w':
        glTranslate(0, 0, 2 / speed)
   if key == b'a':
        glTranslate(1 / speed, 0, 0)
   if key == b's':
        glTranslate(0, 0, -2 / speed)
   if key == b'd':
        glTranslate(-1 / speed, 0, 0)
   #UP/Down
   if key == b'm':
        glTranslate(0, -1 / speed, 0)
   if key == b'n':
        glTranslate(0, 1 / speed, 0)
   
   # glMultMatrixf(current_mv_mat)
   #rotate
   if key == b'i':
       sum_rot_updown -= speed / 10
   if key == b'k':
       sum_rot_updown += speed / 10
   if key == b'j':
       glRotatef(speed / 10, 0, -1, 0)
       rot += 1
   if key == b'l':
       glRotatef(speed / 10, 0, 1, 0)
       rot -= 1

   glutPostRedisplay()
   

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(w,h)
glutCreateWindow('rommtour')
init()
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutDisplayFunc(display)
glutMainLoop()