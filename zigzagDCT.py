import sys
from math import cos,sqrt,pi
import numpy as n_
import pylab as p_
import matplotlib.cm as cm


def dct(x, y, u, v, n):
    # Normalisation
    def alpha(a):
        if a==0:
            return sqrt(1.0/n)
        else:
            return sqrt(2.0/n)
    return alpha(u) * alpha(v) * cos(((2*x+1)*(u*pi))/(2*n)) * cos(((2*y+1)*(v*pi))/(2*n))

def getBasisImage(u, v, n):
    # for a given (u,v), make a DCT basis image
    basisImg = n_.zeros((n,n))
    for y in range(0, n):
        for x in range(0, n):
            basisImg[y,x] = dct(x, y, u, v, n)
    return basisImg


def isOutOfBounds(row,col,height,width):
    return row<0 or row>height or col<0 or col>width

if __name__ == '__main__':
    print("Running DCT")

    # n (int): assume square image, so we don't have different xres and yres
    try:
        n = int(sys.argv[1])
    except:
        n = 8
    print("n: %d" % n)

    # We can get different frequencies by setting u and v
    print("Generating DCT basis images")
    imageSet = []
    for u in range(0, n):
        for v in range(0, n):
            basisImg = getBasisImage(u, v, n)
            imageSet.append(basisImg)

    print("Saving figure...")
    p_.figure("DCT")
    for i in range(0, len(imageSet)):
        p_.subplot(n, n, i+1)
        p_.axis('off')
        p_.imshow(imageSet[i],cmap = cm.Greys_r)
    p_.savefig('_dct_'+str(n)+'x'+str(n)+'_'+str(n)+'x'+str(n)+'.png')
    p_.show()

    print("Complete" )

    helperList=[[None for i in range(8)] for j in range(8)]
    c = 0
    for i in range(8):
      for j in range(8):
        helperList[i][j] = imageSet[c]
        c+=1

    # Now creating a zigzag DCT 

    height =  len(helperList)-1
    width = len(helperList[0])-1
    result = []
    row = 0
    col = 0
    goingDown = True
    while not isOutOfBounds(row,col,height,width):
        #print(A[row][col])
        result.append(helperList[row][col])
        if goingDown:
            if col==0 or row==height:
                goingDown = False
                if row==height:
                    col+=1
                else:
                    row+=1
            else:
                row+=1
                col-=1
        else:
            if row==0 or col==width:
                goingDown = True
                if col==width:
                    row+=1
                else:
                    col+=1
            else:
                row-=1
                col+=1

    p_.figure("DCT")
    for i in range(0, len(result)):
      p_.subplot(n, n, i+1)
      p_.axis('off')
      p_.imshow(result[i],cmap = cm.Greys_r)
    p_.savefig('_dct_zigzag'+str(n)+'x'+str(n)+'_'+str(n)+'x'+str(n)+'.png')
    p_.show()