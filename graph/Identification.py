# 関数識別------------------------------------------------------------------------
def iden(a,b,c,d) :

    # 関数なし---------------------------------------------------
    if a==0 and b==0 and c==0 :
        print('値は',d,'です。関数ではありません。')
        sysexit()

    # 一次関数---------------------------------------------------
    if a==0 and b==0 and c!=0 :
        print('一次関数')
        if d > 0 :
            print('y =',c,'x +',d)
        elif d == 0 :
            print('y =',c,'x')
        else :
            print('y =',c,'x',d)
            
    # 二次関数---------------------------------------------------
    if a==0 and b!=0 and c!=0 :
        print('二次関数')  
        if c > 0 :
            if d > 0 :
                print('y =',b,'x^2 +',c,'x +',d)
            elif d == 0 :
                print('y =',b,'x^2 +',c,'x')
            else :
                print('y =',b,'x^2 +',c,'x',d)
        elif c == 0 :
            if d > 0 :
                print('y =',b,'x^2 +',d)
            elif d == 0 :
                print('y =',b,'x^2')
            else :
                print('y =',b,'x^2',d)
        else :
            if d > 0 :
                print('y =',b,'x^2',c,'x +',d)
            elif d == 0 :
                print('y =',b,'x^2',c,'x')
            else :
                print('y =',b,'x^2',c,'x',d)

    
    # 三次関数--------------------------------------------------
    if a!=0 and b!=0 and c!=0 :
        print('三次関数') 
        if b > 0 :
            if c > 0 :
                if d > 0 :
                    print('y =',a,'x^3 +',b,'x^2 +',c,'x +',d)
                elif d == 0 :
                    print('y =',a,'x^3 +',b,'x^2 +',c,'x')
                else :
                    print('y =',a,'x^3 +',b,'x^2 +',c,'x',d)
            elif c == 0 :
                if d > 0 :
                    print('y =',a,'x^3 +',b,'x^2 +',d)
                elif d == 0 :
                    print('y =',a,'x^3 +',b,'x^2')
                else :
                    print('y =',a,'x^3 +',b,'x^2',d)
            else :
                if d > 0 :
                    print('y =',a,'x^3 +',b,'x^2',c,'x +',d)
                elif d == 0 :
                    print('y =',a,'x^3 +',b,'x^2',c,'x')
                else :
                    print('y =',a,'x^3 +',b,'x^2',c,'x',d)
        
        elif b == 0 :
            if c > 0 :
                if d > 0 :
                    print('y =',a,'x^3 +',c,'x +',d)
                elif d == 0 :
                    print('y =',a,'x^3 +',c,'x')
                else :
                    print('y =',a,'x^3 +',c,'x',d)
            elif c == 0 :
                if d > 0 :
                    print('y =',a,'x^3 +',d)
                elif d == 0 :
                    print('y =',a,'x^3')
                else :
                    print('y =',a,'x^3',d)
            else :
                if d > 0 :
                    print('y =',a,'x^3',b,'x^2',c,'x +',d)
                elif d == 0 :
                    print('y =',a,'x^3',b,'x^2',c,'x')
                else :
                    print('y =',a,'x^3',b,'x^2',c,'x',d)
        
        else :
            if c > 0 :
                if d > 0 :
                    print('y =',a,'x^3',b,'x^2 +',c,'x +',d)
                elif d == 0 :
                    print('y =',a,'x^3',b,'x^2 +',c,'x')
                else :
                    print('y =',a,'x^3',b,'x^2 +',c,'x',d)
            elif c == 0 :
                if d > 0 :
                    print('y =',a,'x^3',b,'x^2 +',d)
                elif d == 0 :
                    print('y =',a,'x^3',b,'x^2')
                else :
                    print('y =',a,'x^3',b,'x^2',d)
            else :
                if d > 0 :
                    print('y =',a,'x^3',b,'x^2',c,'x +',d)
                elif d == 0 :
                    print('y =',a,'x^3',b,'x^2',c,'x')
                else :
                    print('y =',a,'x^3',b,'x^2',c,'x',d)