import serial
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numpy import *

class Quadchannel:

    def __init__(self, port_name='COM4', baud_rate=9600):
        self.baud = baud_rate
        self.port = port_name

    # Initiate the serial reading
    def read_serial(self):
        try:
            ser = serial.Serial(self.port, self.baud)
            self.ser = ser
            print("Port has been found successfully!")
            ser.close()
        except:
            raise Exception('Check the Port')

    # 2D Gaussian distribution function
    def gaussian_2Ddist(self, x, y, mx=0, my=0, sx=1, sy=1):
        res = 1/(2*pi*sx*sy) * exp(-((x-mx)**2/(2*sx**2) + (y-my)**2/(2* sy**2)))
        return res

    # Convert serial data to actual values
    def data_decoder(self, n=4):
        data = str((self.ser.readline()).decode())
        data = data.split("-")
        v =  [float(x)/1024 for x in data]
        return v

    # Plotter function
    def plotter(self, v, axix, r=3, n=75, amp=4, sig=0.8):

        # making the meshgrid
        x = linspace(-r, r, n)
        y = linspace(-r, r, n)
        X, Y = meshgrid(x, y)

        # Combining the distributions of each valeu in a circle (radius=r/2)
        n = len(v)
        Z = zeros_like(X)
        for i, value in enumerate(v):
            Z = Z + value*self.gaussian_2Ddist(X, Y,
                                          mx=r/2*cos(2*pi/n*i),
                                          my=r/2*sin(2*pi/n*i),
                                          sx=sig, sy=sig)

        # amplifying the answer for better visualization
        Z = amp*Z

        # surface plot
        axix.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
        axix.set_xlim(-r, r)
        axix.set_ylim(-r, r)
        axix.set_zlim(0, 1.2)
        plt.pause(0.0001)
        plt.show()
        axix.cla()


def main():

    # Calling the class
    QC = Quadchannel()
    QC.read_serial()
    QC.ser.open()

    plt.ion()
    fig=plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # Start reading
    while True:
        v = QC.data_decoder()
        print(v)
        QC.plotter(v, ax)


if __name__ == '__main__':
  main()
