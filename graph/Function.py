# モジュールインポート-------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


# 一次関数算出---------------------------------------------------------------
def Linear_fun (c,d,x_low,x_high):

    # 関数出力------------------------------------
    # 定義域内のy算出
    sec_x = np.arange(x_low, x_high, 0.01)
    y = c*sec_x + d 

    # 定義域内の最大、最小値
    print('値域:',min(y),' <= y <= ',max(y))
    print('最大値:', max(y))
    print('最小値:', min(y))

    # グラフ出力---------------------------------
    print('グラフを出力しました。')
    print('グラフを×で閉じるとプログラムが終了します。')
    plt.plot(sec_x, y)
    plt.scatter(0,d)
    plt.title('Linear-function-graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['function','Intercept'])
    plt.xlim(x_low -1, x_high +1)
    plt.ylim(min(y)-1,max(y)+1)
    plt.grid()
    plt.show()


# 二次関数算出---------------------------------------------------------------
def Quadratic_fun (b,c,d,x_low,x_high):

    # 関数出力------------------------------------
    # 定義域内のy算出
    sec_x = np.arange(x_low, x_high, 0.01)
    y = b*sec_x**2 + c*sec_x + d 

    # 定義域内の最大、最小値
    print('値域:',min(y),' <= y <= ',max(y))
    print('最大値:', max(y))
    print('最小値:', min(y))

    # 頂点、傾き算出-----------------------------
    x_ver = -c/(2*b)
    if b > 0 :
        y_ver = -1*x_ver**2 + d
    else :
        y_ver = x_ver**2 + d

    print('頂点: (',x_ver,',',y_ver,')')
    if b > 0 :
        print('下に凸のグラフです。')
    else :
        print('上に凸のグラフです。')

    # グラフ出力---------------------------------
    print('グラフを出力しました。')
    print('グラフを×で閉じるとプログラムが終了します。')
    plt.plot(sec_x, y)
    plt.scatter(x_ver,y_ver)
    plt.title('Quadratic-function-graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['function','Vertex'])
    plt.xlim(x_low -1, x_high +1)
    plt.ylim(min(y)-5,max(y)+5)
    plt.grid()
    plt.show()


# 三次関数算出----------------------------------------------------------------
def Cubic_fun (a,b,c,d,x_low,x_high):

    # 関数出力----------------------------------
    # 定義域内のy算出
    sec_x = np.arange(x_low, x_high, 0.01)
    y = a*sec_x**3 + b*sec_x**2 + c*sec_x + d

    # 定義域内の最大、最小値
    print('値域:',min(y),' <= y <= ',max(y))
    print('最大値:', max(y))
    print('最小値:', min(y))

    # 極値出力----------------------------------
    # 判別式D
    D = 4*b**2 -12*a*c
    
    if D > 0 :
        D = np.sqrt(D)

        # 微分後の解の公式にてx座標を算出
        dx1 = ( -2*b + D)  / ( 6 * a )
        dx2 = ( -2*b - D)  / ( 6 * a )

        # x座標から極値を算出
        ev1 = a*dx1**3 + b*dx1**2 + c*dx1 + d
        ev2 = a*dx2**3 + b*dx2**2 + c*dx2 + d
        
        
        # 極大、極小の選出
        if ev1 > ev2 :
            print('x =',dx1,'の時、極大値:',ev1)
            print('x =',dx2,'の時、極小値:',ev2)
        else :
            print('x =',dx2,'の時、極大値:',ev2)
            print('x =',dx1,'の時、極小値:',ev1)

    else :
        print('極値なし')
    
    # 変曲点出力--------------------------------
    ddx = -b/(3*a)
    ddy = a*ddx**3 + b*ddx**2 + c*ddx + d
    print('変曲点:(',ddx,',',ddy,')')

    # グラフ出力--------------------------------
    print('グラフを出力しました。')
    print('グラフを×で閉じるプログラムが終了します。')
    plt.plot(sec_x, y)

    if D > 0 :
        if ev1 > ev2 :
            plt.scatter(dx1, ev1)
            plt.scatter(dx2, ev2) 
        else :
            plt.scatter(dx2, ev2)
            plt.scatter(dx1, ev1) 
            
    plt.scatter(ddx,ddy) 
    
    if D > 0 :
        plt.legend(['function','Maxima','Minima','Inflection point'])
    else :
        plt.legend(['function','Inflection point'])
        
    plt.title('Cubic-function-graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(x_low -1, x_high +1)
    plt.ylim(min(y),max(y))
    plt.grid()
    plt.show()
