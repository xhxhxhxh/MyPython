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
