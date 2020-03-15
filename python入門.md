Python
===

[PYHTON初學](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-71f55bccb693)

[PYTHON 教程](http://www.runoob.com/python/python-tutorial.html)
資料型態:
===
```
Python 的內建型態主要分為以下三種：

數值型態：int, float, bool
字串型態：str, chr
容器型態：list, dict, tuple

## 1. 整數 integer( int )
x = 1
print(x)
print(type(x))

##2. 浮點數 floating-point (float)
x = 1.5
print(x)
print(type(x))


##3. 布林值 boolean (bool)
a = True
print(a)
print(type(a))
b = Flase


a = 1
b = 2
print(a==b)

1. 字串 string (str)
song = "Hello, Goodbye"
print(song)
print(type(song))

print('"Bohemian Rhapsody" is a song by the British rock band Queen.')


str1 = "Lucy in the sky"
str2 = " with diamonds"
print(str1 + str2)

str = "ccClub"
print(str*3)


str = "Python"
print(str)
print(len(str))


str = "Python" ## char  字元  P0  Y1 T2  H3 O4 N5 

str[4]


2. 字元 character (chr)：
c = 66
cAsChr = chr(c)
print(cAsChr)

##對應 ASCII 編號


Casting 型別轉換

1. float 轉成 int 
floatNum = 55.0
intNum = int(floatNum)
print(floatNum)
print(intNum)
print(type(floatNum))
print(type(intNum))

2 STR to int

stringNum = "55"
intNum = int(stringNum)
print(stringNum)
print(intNum)
print(type(stringNum))
print(type(intNum))

3.int to str

inta = 55
stra = str(inta)
print(inta)
print(stra)
print(type(inta))
print(type(stra))


```
print 輸出:
===
```

print(1)     //輸出數字
print("we are going")
print('we are going')//輸出字串
print(" i's am")  
// i's am

print(' i\'m m)
// i'm m 
// \' 系統內建單引號

print('apple' + '4')
// apple4

print('apple'+ str(4))
// apple4

print(1+2)
//3

print('1+2')
// 1+2

print(int('1') + 2)
// 3

print(float('1.2') + 2)
// 3.2

print('thus' , a)
// thus + a變數


```

---

數學運算
===

```
1+1
//2

2*2
//4

2**3
//8  次方

2^2
//0   無效


8%2
//0

8%3
// 2  MOD運算

9//4
// 2  可以有多少個4

9//3
// 3

9//2
// 4
10//3
//3

---

變量 variable
===

apple = 10
print(apple)
//10

apple_fruit = 10
ApPPLE_EGG = 11
appleEgg = 12 + 3
print(appleEgg)
// 15

a = 1
b = 2
c = 3 
print(a,b,c)
// 1 2 3

a,b,c = 1,2,3
print(a,b,c)
//123
a = 1
b = a*2
print(a,b)
// 1 2


```

---

 循環
===

```
while當什麼時候做什麼事情

while condidtion < 10:
    print(condition)
    condition = condition + 1


while True:
    print("I'm True")

//無限循環


emample_list =[1,2,3,4,5,6,7,12,542,876]
for i in example_list:
    print(i)
    print('inner')    //在for迴圈裡面
print('stop')        //在FOR結束之後 才會執行

//疊帶器 從第一個輸出到最後最後
// 空格4個 = tab 都算在for迴圈裡面
// Window :  control + [  選擇所想要改變的語句 可以增加或減少 TAB]

for i in range(1,10):
    print(i)
//電腦自動生成的疊帶器 1 ~ 9 少一要注意
//range(stat,stop不包含,[step])

for i in range(1,10,2)
    print(i)
//1 3 5 7 9 


continu & break
a = True
while a:
 b=input('value:')
    if b == '1':
        a = False
    else:
        pase //直接跳過
        
while True:
    b=input('value:')
        if b == '1':
           break //跳出迴圈
    else:
        pase //直接跳過
        
while True:
    b=input('value:')
        if b == '1':
         conttinue(結束後面的語句 重新循環)
    else:
        pase //直接跳過
        

num_list = []
for i in range(1, 11):   # range()的第三個參數沒有設定，表示用預設值1
    num_list += [i]   # 也可以寫成num_list.extend([i])
    
ret = [items for sub_list in L for items in sub_list]

# 其含义是：
ret = []
for sub_list in L:
    for items in sub_list:
        ret.append(items)




    
```
---

條件
===


```
x,y,z = 1,2,3

if x < y :
    print('x is less than y')
//x is less than y


if x < y < z :
    print('x is greater than y and y is less than z')
//x is greater than y and y is less than z


if x < y > z :
    print('x is greater than y and y is less than z')
//empty


x,y,z = 1,2,0
if x < y > z :
    print('x is greater than y and y is less than z')
//x is greater than y and y is less than z


x,y,z = 2,2,0
if x<= y :
    print('x is less  or equal to y')
//'x is less  or equal to y'
   
   
if x == y:
print('x is equal to y')
//'x is equal to y'


x,y,z = 1,2,0
if x != y:
print('x is equal to y')
//'x is not equal to y'

x,y,z = 1,2,3
if x > y:
    print('x is greater than y')
else:
    print('x is less than y')
    

x,y,z, = 4,2,3

if x>y:
    pirnt('x is greater than y')
elif x > z: 
    print('...')
else:
    print('x is less or equal to y')

```
函數
===

```
定義函數

a = 1
b = 2
c = a+b
print(c)
//3 

//def開頭 define  定義一個函數 + name

def function(a,b):
    print('this is a function')
    a = 2 + 1
    print(a)
//在四個空格以後的區間才是屬於 這個函數的程式碼範圍

function()
// this is a function 
// 3

加入參數

---

def fun(a,b):
    c = a*b
    print('the c is' ,c)

fun(2,3)
// 6


fun(a = 2, b = 5)
// the c is 10


def sale_car(price , colour , brand ,is_second_hand ):
    print('price:',prince,
    'colour:',coulour,
    'brand',brand,
    'is_second_hand',is_sceond_hand
    )
    
    
sale_car(1000,'red','carmy',True)
// price .... coliur ...

//默認函數
def sale_car(price , colour = 'red' , brand = 'carmy' ,is_second_hand = True ):
    print('price:',prince,
    'colour:',coulour,
    'brand',brand,
    'is_second_hand',is_sceond_hand
    )
sale_car(1000)
// price 1000  .colour........

sale_car(2000)
// price 2000  .colour........

sale_car(3000 , coulour= 'blue')
// price 2000  .colour: blue

def sale_car(price , colour = 'red' , brand  ,is_second_hand = True ):

//error
//沒定義好的值 不能放在 已經定義好的後面

def sale_car(price , brand  ,colour = 'red'   ,is_second_hand = True ):

//true
//print.............


```
全域變量 global locak
===


```
APPLE = 100 // 不在方法內的變數 叫全域變數
在任何地方都可以使用

a = None //即使 在方法內仍然也要描述

def fun():
    global a  // global 定義全域變數
    a = 20 
    c = 20    // local 只能在方法內運行
    return a + 100

print(APPLE)
print('a past = ', a)
print(fun())
print('a now = ', a)
//100
// a past = None
//120
// a now = 20


```
讀寫文件
===

```
\n  下一行
text = 'This is my first text.\n This is next Line
// This is my first text.
// This is next Line

my_file = open('my file.txt','w')  //第一次會創建文件 第二次會讀或寫

// w = write r =read

my_file.write(text)    //建立一個檔案  把text 存入
my_file.close         // 必須關上 不然會當機


append_text='\n this is appenden file.'
my_file = open('my file.txt','a')

// a= append
my_file.write(apppend_text)
my_file.close


```

讀文件

```
file = open('my file.text' , 'r')
content = file.read()
print(content)

content = file.readline() // 讀一行 第一行
second = file.readline()  // 讀一行 第2行
content = file.readlines() // 讀全部 放進 list裡面
print(content)

```
---

class 類別
===

```
class Calcutor:
    name = 'Good calcutor'
    cash = 18
    def add(self,x,y)
        print(self.name) // = java this 繼承 
        result = x + y
        print(result)
    def minus(self,x,y)
        result = x - y
        print(result)
    def times(self,x,y)
        print(x*y)
    def divide(self,x,y)
        print(x/y)

 calcul = Calcutor()
 calcul.name
 //'good calculator'
 calcul.price
 //18
 calcul.add(10 ,11)
 // 'Good calcutor'
 // 11
 
```
 類 init(初始)
 ===
 
 
```
 _init_//建構子函數
 
class Calcutor:
    name = 'Good calcutor'
    price = 18
    def _init_(self,name,price,hight,width,weight) // 建構子 必須輸入的參數
        slef.name = neme
        self.price= price
        self.h  =  higj
        self.w = width
        self.we = weight
    def add(self,x,y)
        result = x + y
        print(result)
    def minus(self,x,y)
        result = x - y
        print(result)
    def times(self,x,y)
        print(x*y)
    def divide(self,x,y)
        print(x/y)

c = calculator('BAD' ,12,30,1,2)
        
c.name
//BAD

def _init_(self,name,price = 19,hight,width,weight)  //可以在定義的時候設定默認值
     self.add(1,2)        //可以在初始設置函數運算  或是其他運算

```     
 input(輸入)
 ===
 

``` 
 a_input = input('please give anumber:') // return a sting
 print('This input number is:',a_input)
 // a_input = 需要輸入一個數字 
 // This input number is:...
 
 如果要進行判斷要轉呈字串 或是輸入轉成int
 if input == '1'  //or str(2):
 
 or   a_input = int(input('please give anumber:'))
 

```
 
 元組 tuple  列表 list
 ===
 
```
 <List>

可以儲存數值： list1=[1, 2, 3] 

可以儲存字串：list2=['a', 'p', 'p', 'l', 'e']

可以進行操作 list1+list2 與包含方法 list.append()等

 

<Tuple>

可以儲存數值： tuple1=(1, 2, 3)

可以儲存字串：tuple2=('a', 'p', 'p', 'l', 'e')

可以進行操作 tuple1+tuple2

tuple的元素值不可以修改！不可以刪除！
也因此沒有像list有一些改變元素值的方法（例如：list.pop()、list.reverse()......等）


 a_tuple = (12,3,5,15,6)
 anothor_tuple = 2,4,6,7,8
 
 a_list = [12,3,67,7,82]
 
 
 可以用來被疊帶
 
 for content in a_list: // 疊帶輸出
     print(conten)

 for conten in a_tuple: // 疊帶輸出
     print(content)

 for intdex int range(len(a_list)) // 從0到 a_list 長度 -1
 
 
 a = [1,2,3,4,5,6,7]
 
 a.append(數值) //列表後面追加一個值
 a.insert(數值,index) //在index 位添加一個數值
 a.remove(列表中的值) // 刪除列表第一個指定的值
 print(a[index])
 print(a[-1])   // a[-1]列表最後一位 從後面往前數
 print(a[0:3])    // : 從什麼到什麼 0:3  = 0 ,1,2
                     // :3  0,1,2
                     // 不包含最後的參數
                     // 5:  五到最後
                     // -3:0 最後三位
 a.index(2)          // 第一次出現2的index是多少
 a.count(2)            //陣列中出現2的次數
 a.sort()            //從小到大排序 而且會覆蓋原本的list
 a.sort(reverse = True) //從大到小排序 覆蓋遠本的list
 
```
 ---
 
 多維列表
 ===
 
```
 函數庫 簡介 主要用到 numpy  跟  panda 處理多維資料
Numpy: Numpy 處理多維度資料比起 Python 中的 List 有速度快且方便的優勢。
Pandas: 它是一個存取、處理表格資料非常方便的套件，它將協助我們讀取和處理檔案資料。
random: 打亂資料的工具。
TensorFlow: 深度學習的框架。
Matplotlib: 資料視覺化的套件。

  a = [1,2,3,4,5,]
  multi_a=[ [1,2,3],  //三行三列
           [2,3,4],
           [3,4,5]]
  print(a[1])  
  //1
  print(multi_a[0][1])
  //1

```  
  ---
  
  dictionary 
  ===
  
```
  a =[1,2,3,4,5] //陣列
  
  b={key:'value' ,
      'key':value2}//字典  key對應到值
      
 print(b['key'])
 //value2
 
 del ['key'] // 刪除key  跟對應的資料
 
 b['new key'] = new value // 在字典中加入資料  可是字典沒有順序 可能加在最前或最後 或中間
 
 c = {'apple':[1,2,3],
       b:{1:2,2:3}}
 print(c[b][2])
 //3
 
 //可以加入很多東西 函數 陣列 字典 funtion
 
```
 ---
 
 import 
 ===
 
```
 載入 函式子庫
 import time   
 print(time.localtime())
 
 
 import time as t
 print(t.localtime())
 
 from time import localtime //簡化 只載入想要的  而且可以直接呼叫
 //print(localtime())
 
 from time import * //載入全部的功能
 pirnt(get.time())
 
 ---
 
 創建自己的函式庫
 ===
 
 m1.py
 
 def printdata(data):
     print(data)
     

 再跟函式庫同個檔案目錄 就可以import
 
 import m1
 print(m1(printdata('python')))


放在 python 檔案夾的 site pakacge裡面 
就可以直接調用
一般下載的檔案 也放在裡面


```
---

例外處理 try
===

try:
    嘗試執行的程式
except 例外名稱 as 變數名稱:
    例外發生時執行的程式
else:
    若try沒產生例外則會執行這裡
finally:
    不管有沒有發生例外都會跑到的程式
    
```
try:
    file = open('eee'.'r') //錯誤產生
except Exception as e  // 錯誤訊息 存在變數. e
    print e
    print('no file')
    reponse = input('do you want to create a new file')
    if(response == 'y')
        file = open('eeee','w')//創新文件
    else:
        pass
else: // 如果沒有錯誤 就用  else 語句
    file.write('sss')
    file.close


```

EXCEL
===
[](https://www.cnblogs.com/sun-haiyu/p/7096423.html)




進階技巧
===

動態變量實現連續宣告
https://biosomedayfrog.blogspot.com/2017/07/python_20.html
```
for i in range(1,11):
____j=9
____locals()["biosomeday%s%s" %( i , j )+"abc"]=3
____print(locals()["biosomeday%s%s" % ( i , j )+"abc"])
```


可變參數 
===

```
##list
def print_param_0(*param):
      print param
>>> print_param_0('test','t1',3)

## dic
def print_param(**params):
    print params
>>> print_param(x=1,y=2,zz='tan')

https://www.zhihu.com/question/27581780
```