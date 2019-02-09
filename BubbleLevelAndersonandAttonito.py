#Microbit Bubble Level Code
#1. Get acceleration
#2. Calculate radians of tilt for both x and y tilt --> may want to make 2 separate functions
#3. Convert to degrees from radians
#4. Print degrees
# !! use microbit.sleep() <-- argument
# use while True:

#Grace Anderson with Alyssa Attonito

import microbit, math #importing math and microbit libraries



def x_angle(x, z):
    x_angle = math.atan2(x, z)
    return (math.degrees(x_angle))


def y_angle(y, z):
    y_angle = math.atan2(y, z)
    return (math.degrees(y_angle))


while True:
    microbit.sleep(200)
    (x, y, z) = microbit.accelerometer.get_values()
    thetaX = x_angle(x, z)
    thetaY = y_angle(y, z)
    print(thetaX, thetaY)

    if (170<=(math.fabs(thetaX))<=190) and (170<=(math.fabs(thetaY))<=190):
        microbit.display.show(microbit.Image.HEART)
    elif (-170<thetaX<-100 and 170<=(math.fabs(thetaY))<=190): #if -170<y<-100: microbit is turned forward
      microbit.display.show(microbit.Image.ARROW_E)  #show arrow south
    elif (100<thetaX<170 and 170<=(math.fabs(thetaY))<=190):
        microbit.display.show(microbit.Image.ARROW_W)
    elif (-170<thetaY<-100 and 170<=(math.fabs(thetaX))<=190):
        microbit.display.show(microbit.Image.ARROW_S)
    elif (100<thetaY<170 and 170<=(math.fabs(thetaX))<=190):
        microbit.display.show(microbit.Image.ARROW_N)
    else:
        microbit.display.show(microbit.Image.SAD)
    #elif (math.fabs(thetaX)) if -170<y<-100: microbit is turned forward need arrow south
    #elif if 100<y<170: microbit is turned backward need arrow north
    #elif if 100<x<170: microbit is turned to the left need arrow west
    #elif if -170<x<100: microbit is turned to the right need arrow east







  #extra stuff
    #angle = math.atan2(z,x)
    #print("angle = math.atan2(x,z)")