zfrom visual import * # Vpython for 2.7 needed 


#sys =  # This must contain the system to be visualized?

def pause():
 while True:
     rate(50)
     if scene.kb.keys:
         k = scene.kb.getkey()
         return

# Create sphere for each body in system
for body in sys.bodies:
    body.visual = sphere(radius = 0.2, \
                         pos=body.pos, \
                         color=randRGB(0.2,0.8),\
                         make_trail=False, \
                         interval=1,\
                         retain=250)
# 3 Axis center visualization
L=1 # Length of each axis from origin out
xaxis = curve(pos=[(0,0,0), (L,0,0)], color=(0.5,0.5,0.5))
yaxis = curve(pos=[(0,0,0), (0,L,0)], color=(0.5,0.5,0.5))
zaxis = curve(pos=[(0,0,0), (0,0,L)], color=(0.5,0.5,0.5))


# KEYBOARD INPUT
        if (scene.kb.keys > 0):
            if scene.kb.getkey()==' ':
                pause()
                
            if (time()-c > 1.0/60): # 60Hz framerate
            
        rate(100)
        
        # UPDATE VISUAL
        for body in sys.bodies:
            body.visual.pos = body.pos - sys.getCenter()
        c = time()
