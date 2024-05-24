import random##匯入random模組
x1 = 1##設定範圍
x2 = 100##設定範圍
a = random.randint(x1, x2)##取隨機數
b = int(input("請輸入數字:"))##歸零
n = 0##歸零
while(a != b) and (n < 10):##判斷是否猜對或者猜太多次了
    if b < a:##判斷b是否小於a
        b = int(input('數字太小囉！再試一次吧：'))   # 如果 b<a，提示數字太小，請他再輸入一次
    elif b > a:##判斷b是否大於於a
        b = int(input('數字太大囉！再試一次吧：'))   # 如果 b>a，提示數字太大，請他再輸入一次
    n += 1##猜的次數+1
if n == 10:##猜得太多次了
    print("猜錯太多次囉!")##輸出
else:##猜對了
    print('答對囉！')##輸出