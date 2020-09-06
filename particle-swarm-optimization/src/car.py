# basic lib
import os,sys
import time
import math
import random
# plot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# self define file
import rbfn
parent = os.path.dirname(os.getcwd())


def dist2line_intersection(line1Car, line1p2, line2p1, line2p2):
    xdiff = (line1Car[0] - line1p2[0], line2p1[0] - line2p2[0])
    ydiff = (line1Car[1] - line1p2[1], line2p1[1] - line2p2[1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return math.inf
    # no intersection

    d = (det(line1Car, line1p2), det(line2p1, line2p2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    if (line1Car[0]-x) * (line1Car[0]-line1p2[0]) < 0 or (line1Car[1]-y) * (line1Car[1]-line1p2[1]) < 0:
        return math.inf
    # opposite direction
    right, left, up, down = 0, 0, 0, 0
    if line2p1[0] > line2p2[0]:
        right, left = line2p1[0], line2p2[0]
    else:
        right, left = line2p2[0], line2p1[0]
    if line2p1[1] > line2p2[1]:
        up, down = line2p1[1], line2p2[1]
    else:
        up, down = line2p2[1], line2p1[1]
    if not(((right+1>=x)) and ((x>=left-1)) and ((up+1>=y)) and ((y>=down-1))):
        return math.inf
    # not reach the line segment
    ret = math.sqrt((line1Car[0]-x)*(line1Car[0]-x)+(line1Car[1]-y)*(line1Car[1]-y))
    if ret < 3:
        return math.inf
    # car reach something (wall or endline)
    return ret


class Car():
    def __init__(self):
        super(Car, self).__init__()
        # init params
        self.turn_deg = 45
        self.rad_car = 3.0
        self.deg_dir = 0.0
        self.x_rec, self.y_rec, self.f_rec, self.r_rec, self.l_rec, self.dir_rec = [], [], [], [], [], []
        # init map, engine
        self.loadMap()
        self.engine = rbfn.RBFN(3, 12)

    def loadMap(self, path='case01.txt'):
        with open(path, 'r') as f:
            lines = f.readlines()
            lines = [line.replace('\n', '').split(',') for line in lines]
            lines = [[int(j) for j in line] for line in lines]
            self.x_car, self.y_car, self.deg_x_axis= lines[0][0], lines[0][1], float(lines[0][2])
            self.end1, self.end2 = lines[1], lines[2]
            self.walls = lines[3:]

    def loadRecord(self, path=os.path.dirname(os.getcwd()) + '/outputs/train6D.txt'):
        with open(path, 'r') as f:
            lines = f.readlines()
            lines = [line.replace('\n', '').split() for line in lines]
            lines = [[float(j) for j in line] for line in lines]
            for i in range(len(lines)):
                self.x_rec.append(lines[i][0])
                self.y_rec.append(lines[i][1])
                self.f_rec.append(lines[i][2])
                self.r_rec.append(lines[i][3])
                self.l_rec.append(lines[i][4])
                self.dir_rec.append(lines[i][5])

    def draw(self):
        fig = plt.figure()

        # start point
        plt.scatter(0, 0, s = 300, color = 'c')
        # end
        end = list(zip(self.end1, self.end2))
        plt.plot(end[0], end[1], color = 'r')
        # start
        start = list(zip(self.walls[-1], self.walls[-2]))
        plt.plot(start[0], start[1], color = 'k')
        # walls
        for i in range(len(self.walls)-2):
            wall = list(zip(self.walls[i], self.walls[i+1]))
            plt.plot(wall[0], wall[1], color = 'b')

        # animation
        ims = []
        moves = len(self.x_rec)-1 if len(self.x_rec) != 0 else 0
        for i in range(moves):
            move = list(zip([self.x_rec[i],self.y_rec[i]], [self.x_rec[i+1],self.y_rec[i+1]]))
            if self.dir_rec[i] > 0:
                im = plt.plot(move[0], move[1], marker='o', markersize=20, color = 'c')
            else:
                im = plt.plot(move[0], move[1], marker='o', markersize=20, color = 'b')
            ims.append(im)
        self.ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=1000)
        plt.gca().set_aspect('equal', adjustable='box')
        # plt.savefig('autoCar_e4.png')
        # plt.show()
        return fig
    
    def saveDraw(self):
        assert isinstance(self.ani, animation.ArtistAnimation)
        # t = time.strftime('_%Y%m%d_%H%M%S')
        self.ani.save('autoCar.gif',writer='pillow')

    def saveResult(self):
        parent = os.path.dirname(os.getcwd())
        with open(parent + '/outputs/train4D.txt', 'w') as train4D, open(parent + '/outputs/train6D.txt', 'w') as train6D:
            for i in range(len(self.x_rec)):
                a = self.x_rec[i]
                b = self.y_rec[i]
                c = self.f_rec[i]
                d = self.r_rec[i]
                e = self.l_rec[i]
                f = self.dir_rec[i]
                str4 = '{:8.2f} {:8.2f} {:8.2f} {:8.2f}'.format(c, d, e, f)
                str6 = '{:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f}'.format(a, b, c, d, e, f)

                train4D.write(str4+'\n')
                train6D.write(str6+'\n')

    def setEngine(self, engine):
        self.engine = engine

    def getDeg(self, inp):
        lower, upper = 0, 80
        assert isinstance(self.engine, rbfn.RBFN)
        inp = [rbfn.normalization(i, lower, upper) for i in inp]
        deg = self.engine.output(inp)
        lower, upper = -40, 40
        deg = rbfn.denormalization(deg, lower, upper)
        if deg > 40:
            deg = 40
        elif deg < -40:
            deg = -40
        return deg

    def run(self):
        # 0 not see end, 1 see end, 2 near end
        flag = 0
        for _ in range(100):
            # print(j)
            dist_f, dist_r, dist_l = math.inf, math.inf, math.inf
            for i in range(len(self.walls)-2):
                l1p1, l1p2 = [self.x_car,self. y_car], [self.x_car+1*math.cos(math.radians(self.deg_x_axis+self.turn_deg)), self.y_car+1*math.sin(math.radians(self.deg_x_axis+self.turn_deg))]
                dist = dist2line_intersection(l1p1, l1p2, self.walls[i], self.walls[i+1])
                if dist < dist_l:
                    dist_l = dist
                
                l1p1, l1p2 = [self.x_car, self.y_car], [self.x_car+1*math.cos(math.radians(self.deg_x_axis)), self.y_car+1*math.sin(math.radians(self.deg_x_axis))]
                dist = dist2line_intersection(l1p1, l1p2, self.walls[i], self.walls[i+1])
                if dist < dist_f:
                    dist_f = dist
                
                l1p1, l1p2 = [self.x_car, self.y_car], [self.x_car+1*math.cos(math.radians(self.deg_x_axis-self.turn_deg)), self.y_car+1*math.sin(math.radians(self.deg_x_axis-self.turn_deg))]
                dist = dist2line_intersection(l1p1, l1p2, self.walls[i], self.walls[i+1])
                if dist < dist_r:
                    dist_r = dist
            # use x_car, y_car, deg_x_axis
            # to calculate dist_f, dist_r, dist_l

            self.x_rec.append(self.x_car)
            self.y_rec.append(self.y_car)
            self.f_rec.append(dist_f)
            self.r_rec.append(dist_r)
            self.l_rec.append(dist_l)
            self.dir_rec.append(self.deg_dir)
            # record

            # 0 not see end, 1 see end, 2 near end
            l1p1, l1p2 = [self.x_car, self.y_car], [self.x_car+1*math.cos(math.radians(self.deg_x_axis)), self.y_car+1*math.sin(math.radians(self.deg_x_axis))]
            dist = dist2line_intersection(l1p1, l1p2, self.end1, self.end2)
            if flag == 0 and dist_f > dist:
                flag = 1
            elif flag == 1 and dist == math.inf:
                flag = 2
            elif flag == 2:
                if (l1p1[0]-self.end1[0]) * (l1p1[0]-l1p2[0]) < 0 or (l1p1[1]-self.end1[1]) * (l1p1[1]-l1p2[1]) < 0:
                    flag = 0
                    break
            if dist_f==math.inf or dist_r==math.inf or dist_l==math.inf:
                break
            # ending
        
            ################################################################################################
            ##################################           engine           ##################################
            ##################################      set self.deg_dir      ##################################
            ################################################################################################
            inp = []
            if self.engine.num_inp == 3:
                inp = dist_f, dist_r, dist_l
            elif self.engine.num_inp == 5:
                inp = [self.x_car, self.y_car, dist_f, dist_r, dist_l]
            else:
                print('engine input error')
            self.deg_dir = self.getDeg(inp)
            ################################################################################################
            ##################################           engine           ##################################
            ################################################################################################
            
            # move the car (get new point and deg)
            x_next = self.x_car + (math.cos(math.radians(self.deg_dir+self.deg_x_axis)) + math.sin(math.radians(self.deg_dir)) * math.sin(math.radians(self.deg_x_axis)))
            y_next = self.y_car + (math.sin(math.radians(self.deg_dir+self.deg_x_axis)) - math.sin(math.radians(self.deg_dir)) * math.cos(math.radians(self.deg_x_axis)))
            deg_x_axis_next  = self.deg_x_axis - (math.degrees(math.asin(2*math.sin(math.radians(self.deg_dir))/self.rad_car)))
            self.x_car, self.y_car, self.deg_x_axis = x_next, y_next, deg_x_axis_next

        
if __name__ == "__main__":
    pass

    # c = Car()
    # c.engine.loadParams('RBFN_params_3_12.txt')
    # c.run()
    # c.saveResult()

    # c.engine.loadParams('RBFN_params.txt')
    # c.run()
    # c.draw()


