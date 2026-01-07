#字符串转换整数 (atoi)   
class Solution:
    def myAtoi(self, s: str) -> int:
        # 步骤1：跳过所有前导空格（仅前导，不是strip()，但strip()效果等价）
        s = s.strip()
        if not s:  # 空字符串（如输入全是空格）
            return 0
        
        # 步骤2：处理符号
        sign = 1  # 默认正号
        first_char = s[0]
        if first_char == '-':
            sign = -1
            s = s[1:]  # 去掉负号
        elif first_char == '+':
            s = s[1:]  # 去掉正号（sign保持1）
        # 若第一个字符是数字：不处理符号，sign保持1
        
        # 步骤3：校验第一个有效字符是否为数字（非符号/非数字则返回0）
        if s and not s[0].isdigit():  # 去掉符号后为空（如"+"）或首字符非数字
            return 0
        
        # 步骤4：读取连续数字
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
                # 提前截断（可选优化：避免result过大）
                if result * sign < -2**31:
                    return -2**31
                if result * sign > 2**31 - 1:
                    return 2**31 - 1
            else:
                break  # 遇到非数字，停止读取
        
        # 步骤5：应用符号并截断到32位范围
        result *= sign
        min_int = -2**31
        max_int = 2**31 - 1
        if result < min_int:
            return min_int
        elif result > max_int:
            return max_int
        else:
            return result
        