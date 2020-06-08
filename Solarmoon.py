if __name__ == '__build__':
    	raise Exception
import sys

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print('''
ERROR: PyOpenGL not installed properly.  
        ''')
a =0
dela =0.01
x=0
delx=0.005
def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)
   glEnable(GL_DEPTH_TEST)

def display():
   global day,year
   glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glLoadIdentity ()             

   glPushMatrix()
   glColor3f (1.0, 0.0, 0.0)
   glRotatef(-90,1,0,0)
   glutSolidSphere(1,15,20)  #sun
   glPopMatrix()
    
   glRotatef(a,0,1,0)
   glTranslatef(3,0,0) 

   glPushMatrix()
   glPushMatrix()
   # glTranslatef(1,0,0) 
   glColor3f (0.0, 0.0, 1.0)
   glRotatef(23.12,0,0,1)
   glRotatef(x,0,1,0)
   glRotatef(-90,1,0,0)
   glutWireSphere(0.5,15,20)  #earth
   glPopMatrix()
   
   glPushMatrix()
   glRotatef(x,0,1,0)
   glTranslatef(1,0,0) 
   glColor3f (1.0, 1.0, 1.0)
   glRotatef(x,0,1,0)
   glRotatef(-90,1,0,0)
   glutWireSphere(0.08,15,10)  #moon
   glPopMatrix()
   glPopMatrix()
   glFlush ()

def reshape (w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   glOrtho(-5,5,-5,5,-100,100)
   glMatrixMode (GL_MODELVIEW)

def keyboard(key, x, y):
   if key == chr(27):
      import sys
      sys.exit(0)

def idle():
    global a,dela,delx,x
    a += (dela*360)/365
    x += (delx*360)/30
    glutPostRedisplay()

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize (800, 800)
glutInitWindowPosition (100, 100)
glutCreateWindow ('moon earth by faiichann')
init ()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutIdleFunc(idle)
glutMainLoop()