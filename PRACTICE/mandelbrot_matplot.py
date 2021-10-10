import numpy as np

def mandelbrot_set(text,xmin,xmax,ymin,ymax,xn,yn,maxiter,number,horizon=2.0):

    X = np.linspace(xmin,xmax,xn,dtype=np.float32)
    Y = np.linspace(ymin,ymax,yn,dtype=np.float32)
    C = X + Y[:,None]*1j
    N = np.zeros(C.shape,dtype=int)
    Z = np.zeros(C.shape,np.complex64)
    for n in range(maxiter):
        I = np.less(abs(Z),horizon)
        N[I] = n
        Z[I] = eval("{}Z[I]{}**number +C[I]".format(text[0],text[1]))
    N[n==maxiter-1] = 0

    return Z,N
    
if __name__=="__main__":
    import time
    import matplotlib
    from matplotlib import colors
    import matplotlib.pyplot as plt
    
    xmin,xmax,xn=-2.75,+1.25,2500
    ymin,ymax,yn=-1.75,+1.75,1250
    maxiter = 200
    def looping_mandelbrot(text_change):
        fig = plt.figure(figsize=(30,30),dpi=72)
        for a in range(2,11):
            horizon = 1.23**40

            log_horizon = np.log(np.log(horizon))/np.log(a)

            Z,N = mandelbrot_set(text_change,xmin,
                                 xmax,ymin,ymax,xn,
                                 yn,maxiter,a,horizon)
            print(a,Z.shape,N.shape)    
            with np.errstate(invalid="ignore"):
                M = np.nan_to_num(N+1-np.log(np.log(abs(Z)))/np.log(a)+log_horizon)

            dpi = 72
            width = 10
            height = 10*yn/xn
        #fig = plt.figure(figsize=(width,height),dpi=dpi)
        #fig.add_subplot(2,2,a-1)
            ax = fig.add_subplot(3,3,a-1)#.add_axes([0.0,0.0,1.0,1.0],frameon=False,aspect=1)
            light = colors.LightSource(azdeg=315,altdeg=10) 

            M = light.shade(M,cmap=plt.cm.hot,vert_exag=1.5,
                    norm=colors.PowerNorm(0.3),blend_mode="hsv")
            plt.imshow(M,extent=[xmin,xmax,ymin,ymax],interpolation="bicubic")
            ax.set_xticks([])
            ax.set_yticks([])
        return fig
        #year = time.strftime("%Y")
        #major,minor,micro=matplotlib.__version__.split(".",2)
        #text = ("The Mandelbrot fractal \n"
        #        "Rendered with matplotlib %s.%s, %s user HERBERT VENTE" % (major,minor,year))
        #ax.text(xmin+.025,ymin+.025,text,color="white",fontsize=12,alpha=0.5) 

    cases = [
             #["",""],
             #["np.sin(",")"],
             ["np.tanh(",")"]]
    for i,a in enumerate(cases):
        fig = looping_mandelbrot(a)
        fig.savefig("/mnt/c/users/user/onedrive/escritorio/colage_mandelbrot_plot_2.png")#.format(i))    
    
    
