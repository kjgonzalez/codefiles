'''
projectile trajectory
'''

import numpy as np
import matplotlib.pyplot as plt

g = -9.81 # m/s^s
# g = -2
tmax = 300 # s
dt = 0.001

def kph2mps(kph):
    return kph*1000/3600

class CarePackage:
    def __init__(self,x,y,vx,vy,timestep,gravity,coeff_drag=0.0,mass=1,area=1):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.dt = timestep
        self.g = gravity
        self.cd = coeff_drag
        self.m = mass
        self.area=area
        self.is_activated=False
    @property
    def vel_magnitude(self):
        return (self.vx**2+self.vy**2)**0.5
    @property
    def vel_angle(self):
        return np.arctan2(self.vy,self.vx) # radians

    def run_timestep(self):
        f_drag = 1.293/2*self.vel_magnitude**2*self.cdrag*self.area
        fd_x = f_drag*np.cos(self.vel_angle)*-1
        fd_y = f_drag*np.sin(self.vel_angle)*-1

        ax = fd_x/self.m
        ay = (self.m*self.g + fd_y)/self.m
        self.vy += ay*self.dt
        self.vx += ax*self.dt
        self.y += self.vy*self.dt
        self.x += self.vx*self.dt

    def activate_parachute(self):
        self.is_activated = True

    @property
    def cdrag(self):
        if(self.is_activated):
            return self.cd
        else:
            return 0.1

def run_sim(t_activate=0):
    t = 0
    arr_t = []
    arr_x = []
    arr_y = []
    d_parachute=11 # m
    ob = CarePackage(0, 300, kph2mps(100), 0, dt, gravity=g, coeff_drag=1.75, mass=200,
                     area=np.pi / 4 * d_parachute ** 2)
    arr_t.append(t)
    arr_x.append(ob.x)
    arr_y.append(ob.y)
    flag_onground = False
    # t_activate=3
    while(not flag_onground):

        if(t>=t_activate):
            ob.activate_parachute()
        ob.run_timestep()
        t+=dt
        arr_t.append(t)
        arr_x.append(ob.x)
        arr_y.append(ob.y)
        if(ob.y<=0 or t>tmax): flag_onground = True # end sim

    arr_t = np.array(arr_t)
    arr_x = np.array(arr_x)
    arr_y = np.array(arr_y)

    print('t_activate:',t_activate)
    print('drop time:',arr_t[-1])
    print('dist_x:',arr_x[-1])
    print('vy_max:',ob.vy)
    print('  (kph): ',ob.vy*3600/1000)
    return arr_t,arr_x,arr_y



if(__name__ == '__main__'):
    for t in range(0,15):
        print('-'*20)
        array_t,array_x,array_y = run_sim(t_activate=t)

    # f,p = plt.subplots(3,1)
    # array_t,array_x,array_y = run_sim(t_activate=100)
    # p[0].plot(array_x,array_y,'-x')
    # p[0].set_title('y over x')
    # p[1].plot(array_t,array_x)
    # p[1].set_title('x over t')
    # p[2].plot(array_t,array_y)
    # p[2].set_title('y over t')
    # f.tight_layout()
    # plt.show()



