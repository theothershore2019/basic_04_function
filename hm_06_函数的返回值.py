def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2

    # 可以使用返回值，告诉调用函数一方返回的结果
    return result
    # 注意：return 表示返回，后续的代码都不会被执行
    # num = 1000


# 可以使用变量，来接收函数的返回结果
sum_result = sum_2_num(10, 20)

print(sum_result)
