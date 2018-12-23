import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as cm
import numpy as np


def createdata():
    maxdepth = [
        7, 8, 9
    ]
    alpha = [
        1, 2, 3, 4, 5
    ]
    beta = [
        1, 2, 3, 4, 5
    ]
    score = [3]*24+[4] +\
            [3.5]*25 +\
            [4]*25
    return np.array(maxdepth),\
           np.array(alpha),\
           np.array(beta),\
           np.array(score)


def plot3D(alpha, beta, score, maxdepth=np.array([1]), figsize=[15,15], elev=45, azim=45):
    lenalpha = alpha.size
    lenbeta = beta.size
    X, Y = np.meshgrid(alpha, beta)
    numdepth = maxdepth.size
    fig = plt.figure(figsize=figsize)
    ax = Axes3D(fig)
    for depth in range(numdepth):
        numscore = score.size/numdepth
        Z = score[int(numscore*depth): int(numscore*(depth+1))].\
            reshape(lenbeta, lenalpha)
        print(X.shape, Y.shape, Z.shape)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.7, cmap=plt.get_cmap())
        ax.view_init(elev=elev, azim=azim)
    plt.show()



if __name__ == '__main__':
    maxdepth, alpha, beta, score = createdata()
    plot3D(alpha, beta, score[:25])
