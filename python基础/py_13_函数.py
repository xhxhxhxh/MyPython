def multiplication_table():
    """乘法表"""

    num = 1

    while num <=9:

        i = 1

        while i <= num:

            result = i * num

            print('%d * %d = %d' % (i, num, result), end = '\t') # 制表符\t保持文本垂直方向对齐

            i += 1

        print('')
        
        num += 1