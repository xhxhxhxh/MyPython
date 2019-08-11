# python学习笔记
## python基础
  + 常见错误
    1. 缩进、同行、拼写错误、首字空格。
  + 注释
    1. 单行注释`# `。
    2. 多行注释`"""  """`。
    3. TODO注释`# TODO(作者) 内容`。
  + 运算符
    1. `//`取商的整数部分。
    2. `**`幂。
    3. `'-' * 100`字符串连续拼接。
  + 变量类型
    1. 数字型包括：`int`整数型，`float`浮点型，`bool`布尔型，`complex`复数型。
    2. 非数字型包括： 字符串、列表、字典、元组。
    3. 使用`type()`判断变量类型。
    4. 数字型与字符型只可进行`*`运算，`+`等运算均不行。
    5. 使用`int(x) float(x)`将字符串转化为整数类型，不改变原来变量。
    6. `input()`函数返回的是一个字符串。
    7. 格式化输出
       + `%s`字符串格式。
       + `%06d`整数格式，不足6位前面自动补0。
       + `%.2f`float格式，保留两位小数。
       + `%%`百分号。
    8. 变量名只能由字母、下划线、数字三种形式组成，不能以数字开头，不能出现特殊字符。
    9. 变量名的单词用_连接。
  + 条件语句
    1. 语法：
       ```
       if 条件：
           代码
       elif 条件：
           代码
       else:
           代码
       ```
    2. 逻辑运算符：与`and`、或`or`、非`not`。
  + 循环语句
    + while循环语法：
      ```
      while i <= 100:
          sum += i
          i += 1
      ```
  + 函数
    + 函数定义:
      ```
      def 函数名():
          """注释"""
          代码
      ```
    + 参数默认值的设置与js ES6中类似，且设置了默认值的参数应放在元组尾部。
    + 多值参数：`def measure(num, *args, **kwargs):`。
  + 列表
    + 列表定义: 类似与其他语言的数组。
    + 列表常用方法：
      1. 获取列表索引: `name_list.index('王五')`。
      2. 在末尾追加数据: `name_list.append('赵六')`。
      3. 在指定索引处追加数据: `name_list.insert(2, '钱二')`。
      4. 合并数组: `name_list.extend(['孙悟空', '猪八戒'])`。
      5. 删除元素：`name_list.remove('张三')`，`name_list.pop(1)`删除对应索引的元素，并返回，默认删除最后一个元素，`name_list.clear() `清空数组，`del name_list[0]`将一个变量从内存中删除。
      6. 统计元素：`len(name_list)`获取列表长度，`name_list.count('张三')`统计元素重复次数。
      7. 排序数组：`num_list.sort()`升序，`num_list.sort(reverse=True)`降序，`num_list.reverse()`翻转数组。
      8. for循环遍历语法：
         ```
         for name in name_list:
             print(name)
         else: # 在没有被break时，循环结束后执行
             print('执行结束')
         ```
  + 元组
    1. 定义：使用`()`包裹，里面的元素不能修改，与列表相似。
    2. 里面只包含一个元素时：`info_tuple = ('张三',)`这样定义。
    3. 列表转元组：`tuple()`方法, 元组转元列表：`list()`。
    4. 作为函数返回值时，括号可省略，接收方式`gl_temp, gl_wet = measure()`。
    5. 交换数值：`a, b = b, a`。
  + 字典
    1. 定义： 类似其他语言中的对象。
    2. 方法： `person['name']`取值，`person['weight'] = 100`修改值，`person.pop('name')`删除值。
    3. `len(person)`统计字典长度，`person.update(person2)`合并字典，并对重复属性更新，`person.clear()`清空字典。
  + 字符串方法
    1. 判断是否含有空格：`space_str.isspace()`。
    2. 判断数字：`num_str.isdecimal()`。
    3. 判断以指定字符串开头：`hello_str.startswith('el')`和`hello_str.endswith('rld')`。
    4. 查找字符串，无内容时不会报错，会返回-1：`hello_str.find('el')`。
    5. 字符串替换，返回新的字符串：`hello_str.replace('world', 'python')`。
    6. 字符串对齐：`poem_str.center(10, '　')`。
    7. 去除首尾空白符：`space_str.strip()`。
    8. 字符串拆分：`str.split()`，字符串拼接：`''.join(split_str)`。
    9. 字符串截取：`str[起始索引:结束索引:步长]`，末尾索引从-1开始计数，逆序可将步长设为-1，列表和元组也支持该种方式。
  + 数的处理
    + 随机数：`import random random.randint(1, 3)`，返回[1,3]中的数。
  + 公共方法
    1. 统计长度：`len()`，删除数据：`del()`，最大值：`max()`，最小值：`min()`。
    2. 列表和元组可使用`*`和`+`运算符进行重复和拼接。
    3. 使用关键字`in`和`not in`判断成员是否存在。
  + 其他
    + `print('', end = '')`表示不换号打印。
    + 制表符：`\t`保持文本垂直方向对齐, `\n`换行。
    + 常量：约定使用大写字母，单词之间用下划线连接。
## 面向对象
  + 基础语法
    1. 采用大骆驼峰命名法。
    2. 语法：
       ```
       class Cat:
 
           def eat(self):
               print('猫在吃鱼')
       
           def drink(self):
               print('猫在喝水')
 
       tom = Cat()
       tom.eat()
       tom.drink()
       ```
    3. 初始化对象：使用` __init__(self, name)`方法，该方法会在对象初始化时自动调用。
    4. __del__方法：`__del__(self)`方法会在对象被销毁前调用。
    5. 身份运算符：`is  is not`，与`==`的区别在于前者判断是不是同一对象，后者判断是否相等，`None`关键字建议使用`is`判断。
    6. 私有属性和方法：在属性和方法前加`__`，私有属性可被对象内的方法访问到(要想访问可在前加`_类名`)，外部和子类均不能访问。
    7. 继承：`class Dog(Anmial):`，继承会获得父类以及父类的父类中所有的属性和方法。
    8. 重写：在子类中定义相同的方法可重写父类，可使用`super()`调用父类方法。
    9. 多继承：`class C(A, B)`, 同名属性和方法会使用第一个继承的父类。
    10. 类属性和方法：
        ```
        class Person():
            count = 0
 
            @classmethod
            def show_count(cls):
                print(cls.count)
            
            @staticmethod # 静态方法
            def say_hello():
                print('你好')
        
            def __init__(self, name):
                self.name = name
                Person.count += 1
        ```
  + 异常
    1. 捕捉异常：
       ```
       try:
          num = int(input('请输入一个整数'))
          print(8 / num)
          except ValueError:
              print('输入错误')
          except ZeroDivisionError:
              print('0错误')
          except Exception as result:
              print('未知错误%s' % result)
          else:
              print('无异常时执行')
          finally:
              print('无论是否异常都会执行')
       ```
  + 模块
    1. 模块重命名: `import 模块 as 名称`。
    2. 按需导入： `from 模块 import 工具`。
    3. package导入：需在文件夹中建立`__init__.py`文件，并在其中引入需要的模块。
    4. 模块构建发布：
      1. 创建`setup.py`文件，并填写相应信息。
      2. 构建模块：`python setup.py build`。
      3. 生成压缩包：`python setup.py sdist`。
      4. 安装模块：`tar -zxvf 模块压缩包`，`python setup.py install`。
      5. 安装第三方模块：`pip install 模块`。
    5. 使用pip命令安装：`pip install pygame -i https://pypi.tuna.tsinghua.edu.cn/simple --user` 更换镜像源。
  + 文件读写
    1. 语法：
       ```
       # 打开文件
       file = open("README", 'a')
       
       # 读取文件
       # file.write('hello')
       text = file.read()
       print(text)
       
       # 关闭文件
       file.close()
       ```
    2. 读一行：`readline()`
## pygame
  + 基础方法
    1. 初始化：`pygame.init()`。
    2. 终止游戏：`pygame.quit()`。
    3. Rect绘制矩形：`pygame.Rect(x, y, width, height)`，可从返回值中读取相应的值，如：`rect.size`表示`(width, height)`。
    4. 创建主窗口：`pygame.display.set_mode((480, 700))`，第一个参数便是窗口宽高。
    5. 加载图片：`background = pygame.image.load('./images/background.png')`。
    6. 绘制图像：`scree.blit(background, (0, 0))`。
    7. 更新画面：`pygame.display.update()`。
    8. 游戏时钟(控制帧率)：`clock = pygame.time.Clock()clock = pygame.time.Clock()  clock.tick(60)`。
    9. 事件监听：`pygame.event.get()`会返回一个事件列表。
    10. 定时器：`pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)`，第一个参数为定时器事件，第二个为间隔时间。
    11. 键盘监听：`pygame.key.get_pressed()`，返回一个列表，触发的事件值为1。

  
