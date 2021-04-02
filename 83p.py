from matplotlib import pyplot as plt


def a():
    xs = [0,1,2,3]
    ys = [0,2,4,6]
    plt.plot(xs, ys, '.')

    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([-5,5])
    axes.set_ylim([-8,8])
    plt.show()

def b():
    xs = [0,2,3,4,5]
    ys = [0,4,1,7,5]
    plt.plot(xs,ys,'-',color="red")

    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([0,5])
    axes.set_ylim([0,8])
    plt.show()

def c(): # 일차함수
    class LinearEquation:
        def __init__(self, a, b, dist=1, size=100):
            self.size = size
            self.xs = []
            self.ys = []

            x = -size
            while True:
                self.xs.append(x)
                self.ys.append((a*x)+b)
                x += dist
                if x > size:
                    break
            
        def show_graph(self):
            plt.grid(True)
            axes = plt.gca()
            axes.set_xlim([-self.size,self.size])
            axes.set_ylim([-self.size, self.size])
            plt.plot(self.xs,self.ys, '.')
            plt.show()

    # linear_eq1 = LinearEquation(-(2/3), 2, 0.1, 4)
    linear_eq1 = LinearEquation(2,3, 0.1, 4) # 89p 문제 1번
    linear_eq1.show_graph()

def d(): # 이차함수
    class QuadraticEquation:
        def __init__(self, a, b, c, dist=1, size=100):
            self.size = size
            self.xs = []
            self.ys = []

            x = -size
            while True:
                self.xs.append(x)
                self.ys.append((a*(x*x))+(b*x)+c)
                x += dist
                if x > size:
                    break

        def show_graph(self):
            plt.grid(True)
            axes = plt.gca()
            axes.set_xlim([-self.size,self.size])
            axes.set_ylim([-self.size, self.size])
            plt.plot(self.xs,self.ys, '.')
            plt.show()

    # quad_eq1 = QuadraticEquation(1,0,0,0.1,10)
    quad_eq1 = QuadraticEquation(-2, 3, 4, 0.1, 6) # 89p 문제 2번
    quad_eq1.show_graph()


if __name__ == "__main__":
    d()