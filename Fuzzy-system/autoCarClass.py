import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os,sys

class autoCar():
    def __init__(self, filename = 'case01.txt'):
        super(autoCar, self).__init__()
        self.turn_deg = 45
        self.rad_car = 3.0
        self.deg_dir = 0.0
        self.x_rec, self.y_rec, self.f_rec, self.r_rec, self.l_rec, self.dir_rec = [], [], [], [], [], []
        self.loadMap(filename = 'case01.txt')

    def loadMap(self, filename = 'case01.txt'):
        readFile = open('case/'+filename,'r')
        lines = readFile.readlines()
        lines = [line.replace('\n', '').split(',') for line in lines]
        lines = [[int(j) for j in line] for line in lines]

        self.x_car, self.y_car, self.deg_x_axis= lines[0][0], lines[0][1], float(lines[0][2])
        self.end1, self.end2 = lines[1], lines[2]
        self.walls = lines[3:]
    
    def dist2line_intersection(self, line1Car, line1p2, line2p1, line2p2):
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

        # print(('{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(line2p1[0], line2p2[0], line2p1[1], line2p2[1], x, y)))
        # print('{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(line1Car[0], line1Car[1], line1p2[0], line1p2[1]))
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
        # print(('{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(right, left, up, down, x, y)))
        if not(((right+1>=x)) and ((x>=left-1)) and ((up+1>=y)) and ((y>=down-1))):
            return math.inf
        # not reach the line segment
        ret = math.sqrt((line1Car[0]-x)*(line1Car[0]-x)+(line1Car[1]-y)*(line1Car[1]-y))
        if ret < 3:
            return math.inf
        # print(line2p1, line2p2, x, y, ret)
        return ret

    def run(self):
        flag = 0
        # 0 not see end, 1 see end, 2 near end
        for j in range(120):
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
            # print('dist::: {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(dist_l, dist_f, dist_r, deg_dir))
            # use x_car, y_car, deg_x_axis
            # to calculate dist_f, dist_r, dist_l

            self.x_rec.append(self.x_car)
            self.y_rec.append(self.y_car)
            self.f_rec.append(dist_f)
            self.r_rec.append(dist_r)
            self.l_rec.append(dist_l)
            self.dir_rec.append(self.deg_dir)
            # record

            l1p1, l1p2 = [self.x_car, self.y_car], [self.x_car+1*math.cos(math.radians(self.deg_x_axis)), self.y_car+1*math.sin(math.radians(self.deg_x_axis))]
            dist = dist2line_intersection(l1p1, l1p2, self.end1, self.end2)
            if flag == 0 and dist_f > dist:
                flag = 1
            elif flag == 1 and dist == math.inf:
                flag = 2
            elif flag == 2:
                if (l1p1[0]-self.end1[0]) * (l1p1[0]-l1p2[0]) < 0 or (l1p1[1]-self.end1[1]) * (l1p1[1]-l1p2[1]) < 0:
                    break
            # 0 not see end, 1 see end, 2 near end
            # ending
            # print('{:8.2f} {:8.2f} {:8.2f}'.format(dist_f, dist_r, dist_l))
            if dist_f==math.inf or dist_r==math.inf or dist_l==math.inf:
                break

            max_diff = 10
            diff = abs(dist_l-dist_r)
            if dist_r > dist_l:
                if diff > max_diff:
                    self.deg_dir = 40
                else:
                    self.deg_dir = 40 * diff / max_diff
            if dist_l > dist_r:
                if diff > max_diff:
                    self.deg_dir = -40
                else:
                    self.deg_dir = -40 * diff / max_diff
            # Fuzzy systemz
            # print('abs::: {:5.2f}   {:5.2f}'.format(abs(dist_l-dist_r), deg_dir))
            # print('dist::: {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(dist_l, dist_f, dist_r, deg_dir))

            x_next = self.x_car + (math.cos(math.radians(self.deg_dir+self.deg_x_axis)) + math.sin(math.radians(self.deg_dir)) * math.sin(math.radians(self.deg_x_axis)))
            y_next = self.y_car + (math.sin(math.radians(self.deg_dir+self.deg_x_axis)) - math.sin(math.radians(self.deg_dir)) * math.cos(math.radians(self.deg_x_axis)))
            deg_x_axis_next  = self.deg_x_axis - 10*(math.degrees(math.asin(math.radians(2*math.sin(math.radians(self.deg_dir))/self.rad_car))))
            # print('{:5.2f}   {:5.2f}   {:5.2f}'.format(x_next, y_next, deg_x_axis_next))
            self.x_car, self.y_car, self.deg_x_axis = x_next, y_next, deg_x_axis_next
            # plt.scatter(x_car,y_car, s = 600, color = 'c')
            # move the car (get new point and deg)

    def draw(self):
        fig = plt.figure()

        plt.scatter(0, 0, s = 400, color = 'c')
        # start point
        temp = list(zip(self.end1, self.end2))
        plt.plot(temp[0], temp[1], color = 'r')
        # end
        temp = list(zip(self.walls[-1], self.walls[-2]))
        plt.plot(temp[0], temp[1], color = 'k')
        # start
        for i in range(len(self.walls)-2):
            temp = list(zip(self.walls[i], self.walls[i+1]))
            plt.plot(temp[0], temp[1], color = 'b')
        # walls

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
        # t = time.strftime('_%Y%m%d_%H%M%S')
        # ani.save('autoCar'+t+'.gif',writer='pillow')
        # plt.show()
        return fig
        # animation
    
    def saveResult(self):
        train4D = open("train4D.txt", "w")
        train6D = open("train6D.txt", "w")
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

        train4D.close()
        train6D.close()

    def retResultLFR(self):
        return self.l_rec, self.f_rec, self.r_rec

    def loadRecord(self, filename = 'train6D.txt'):
        readFile = open('../outputs/'+filename,'r')
        lines = readFile.readlines()
        lines = [line.replace('\n', '').split() for line in lines]
        # print(lines)
        lines = [[np.float64(j) for j in line] for line in lines]

        for i in range(len(lines)):
            self.x_rec.append(lines[i][0])
            self.y_rec.append(lines[i][1])
            self.f_rec.append(lines[i][2])
            self.r_rec.append(lines[i][3])
            self.l_rec.append(lines[i][4])
            self.dir_rec.append(lines[i][5])


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

    # print(('{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(line2p1[0], line2p2[0], line2p1[1], line2p2[1], x, y)))
    # print('{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(line1Car[0], line1Car[1], line1p2[0], line1p2[1]))
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
    # print(('{:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(right, left, up, down, x, y)))
    if not(((right+1>=x)) and ((x>=left-1)) and ((up+1>=y)) and ((y>=down-1))):
        return math.inf
    # not reach the line segment
    ret = math.sqrt((line1Car[0]-x)*(line1Car[0]-x)+(line1Car[1]-y)*(line1Car[1]-y))
    if ret < 3:
        return math.inf
    # print(line2p1, line2p2, x, y, ret)
    return ret

def tempFunc():
    readFile = open('case01.txt','r')
    lines = readFile.readlines()
    lines = [line.replace('\n', '').split(',') for line in lines]
    lines = [[int(j) for j in line] for line in lines]

    turn_deg = 45
    x_car, y_car, deg_x_axis, rad_car = lines[0][0], lines[0][1], float(lines[0][2]), 3.0
    end1, end2 = lines[1], lines[2]
    walls = lines[3:]
    x_rec, y_rec, f_rec, r_rec, l_rec, xdeg_rec = [], [], [], [], [], []
    # prepare map



    flag = 0
    # 0 not see end, 1 see end, 2 near end
    deg_dir = 0.0
    for j in range(88):
        dist_f, dist_r, dist_l = math.inf, math.inf, math.inf
        for i in range(len(walls)-2):
            l1p1, l1p2 = [x_car, y_car], [x_car+1*math.cos(math.radians(deg_x_axis+turn_deg)), y_car+1*math.sin(math.radians(deg_x_axis+turn_deg))]
            dist = dist2line_intersection(l1p1, l1p2, walls[i], walls[i+1])
            if dist < dist_l:
                dist_l = dist
            
            l1p1, l1p2 = [x_car, y_car], [x_car+1*math.cos(math.radians(deg_x_axis)), y_car+1*math.sin(math.radians(deg_x_axis))]
            dist = dist2line_intersection(l1p1, l1p2, walls[i], walls[i+1])
            if dist < dist_f:
                dist_f = dist
            
            l1p1, l1p2 = [x_car, y_car], [x_car+1*math.cos(math.radians(deg_x_axis-turn_deg)), y_car+1*math.sin(math.radians(deg_x_axis-turn_deg))]
            dist = dist2line_intersection(l1p1, l1p2, walls[i], walls[i+1])
            if dist < dist_r:
                dist_r = dist
        # print('dist::: {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(dist_l, dist_f, dist_r, deg_dir))
        # use x_car, y_car, deg_x_axis
        # to calculate dist_f, dist_r, dist_l

        x_rec.append(x_car)
        y_rec.append(y_car)
        f_rec.append(dist_f)
        r_rec.append(dist_r)
        l_rec.append(dist_l)
        xdeg_rec.append(deg_dir)
        # record

        l1p1, l1p2 = [x_car, y_car], [x_car+1*math.cos(math.radians(deg_x_axis)), y_car+1*math.sin(math.radians(deg_x_axis))]
        dist = dist2line_intersection(l1p1, l1p2, end1, end2)
        if flag == 0 and dist_f > dist:
            flag = 1
        elif flag == 1 and dist == math.inf:
            flag = 2
        elif flag == 2 and dist_f < 8:
            dist2line_intersection(l1p1, l1p2, end1, end2)
            break
        # 0 not see end, 1 see end, 2 near end
        # ending
        if dist_f==math.inf or dist_r==math.inf or dist_l==math.inf:
            break


        max_diff = 10
        diff = abs(dist_l-dist_r)
        if dist_r > dist_l:
            if diff > max_diff:
                deg_dir = 40
            else:
                deg_dir = 40 * diff / max_diff
        if dist_l > dist_r:
            if diff > max_diff:
                deg_dir = -40
            else:
                deg_dir = -40 * diff / max_diff
        # Fuzzy systemz
        # print('abs::: {:5.2f}   {:5.2f}'.format(abs(dist_l-dist_r), deg_dir))
        # print('dist::: {:5.2f}   {:5.2f}   {:5.2f}   {:5.2f}'.format(dist_l, dist_f, dist_r, deg_dir))

        x_next = x_car + (math.cos(math.radians(deg_dir+deg_x_axis)) + math.sin(math.radians(deg_dir)) * math.sin(math.radians(deg_x_axis)))
        y_next = y_car + (math.sin(math.radians(deg_dir+deg_x_axis)) - math.sin(math.radians(deg_dir)) * math.cos(math.radians(deg_x_axis)))
        deg_x_axis_next  = deg_x_axis - (math.degrees(math.asin(2*math.sin(math.radians(deg_dir)/rad_car))))
        # print('{:5.2f}   {:5.2f}   {:5.2f}'.format(x_next, y_next, deg_x_axis_next))
        x_car, y_car, deg_x_axis = x_next, y_next, deg_x_axis_next
        # plt.scatter(x_car,y_car, s = 600, color = 'c')
        # move the car (get new point and deg)



    fig = plt.figure()

    plt.scatter(0, 0, s = 400, color = 'c')
    # start point
    temp = list(zip(end1, end2))
    plt.plot(temp[0], temp[1], color = 'r')
    # end
    temp = list(zip(walls[-1], walls[-2]))
    plt.plot(temp[0], temp[1], color = 'k')
    # start
    for i in range(len(walls)-2):
        temp = list(zip(walls[i], walls[i+1]))
        plt.plot(temp[0], temp[1], color = 'b')
    # walls
    for i in range(len(x_rec)-1):
        temp = list(zip([x_rec[i],y_rec[i]], [x_rec[i+1],y_rec[i+1]]))
        if xdeg_rec[i] > 0:
            im = plt.plot(temp[0], temp[1], marker='o', markersize=20, color = 'c')
        else:
            im = plt.plot(temp[0], temp[1], marker='o', markersize=20, color = 'b')
    # temp
    # draw result
    plt.show()
    # draw


    # ims = []
    # for i in range(len(x_rec)-1):
    #     temp = list(zip([x_rec[i],y_rec[i]], [x_rec[i+1],y_rec[i+1]]))
    #     if xdeg_rec[i] > 0:
    #         im = plt.plot(temp[0], temp[1], marker='o', markersize=20, color = 'c')
    #     else:
    #         im = plt.plot(temp[0], temp[1], marker='o', markersize=20, color = 'b')
    #     ims.append(im)
    # ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=1000)
    # ani.save("test.gif",writer='pillow')
    # plt.show()
    # # animation

if __name__ == '__main__':
    # str = '{:5.2f}   {:5.2f}   {:5.2f}'.format(1.111111111111111111111111111, 1.111111111111111111111111111, 1.111111111111111111111111111)
    # print(str)
    car1 = autoCar()
    car1.loadMap(filename = 'case01.txt')
    # car1.run()
    car1.loadRecord()
    car1.draw()
    # car1.saveResult()
