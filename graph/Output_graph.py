# モジュールインポート------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import sys
import Identification as Iden
import  Function as fuct


# メイン-------------------------------------------------------------------

# 関数入力--------------------------------------------
print('関数の値を入力してください。(三次関数まで対応)')
print('y = ax^3 +bx^2 +cx +d')

# 入力値が数値の場合
try :
    a = float(input('a ='))
    b = float(input('b ='))
    c = float(input('c ='))
    d = float(input('d ='))

# 入力値が非数値の場合(強制終了させる)
except ValueError as error :
    print('適切な数値が入力されませんでした。')
    print('プログラムを終了します。')
    sys.exit()


# 定義域入力（要改善）--------------------------------
print('\n定義域を入力してください。')
print('low <= y <= high')

# 入力値が数値の場合
try :
   x_low = float(input('low ='))
   x_high = float(input('high ='))

# 入力値が非数値の場合(強制終了させる)
except ValueError as error :
    print('適切な数値が入力されませんでした。')
    print('プログラムを終了します。')
    sys.exit()

# 定義域の正当性確認
if x_low >= x_high :
    print('定義域が正しく入力されませんでした。')
    print('プログラムを終了します。')
    sys.exit()

#  関数識別結果出力-----------------------------------
print('\n識別結果です。')
Iden.iden(a,b,c,d)

if a==0 and b==0 and c==0 :
    sysexit()

print('定義域:', x_low, '<= x <=', x_high)

# 各次元毎にプログラムを動かす
if a==0 and b==0 and c!=0 :
    fuct.Linear_fun(c,d,x_low,x_high)

elif a==0 and b!=0 and c!=0 :
    fuct.Quadratic_fun(b,c,d,x_low,x_high)

elif a!=0 and b!=0 and c!=0 :
    fuct.Cubic_fun(a,b,c,d,x_low,x_high)
