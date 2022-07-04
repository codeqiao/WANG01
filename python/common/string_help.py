import random

class StringHelper:

    @staticmethod
    def random_string_generator(str_size, allowed_chars):
        """
         通用的生成随机字符串的方法
        :param str_size: 目标字符串的长度 
        :param allowed_chars: 目标字符串允许存在的字符
        :return: str
        """
        return ''.join(random.choice(allowed_chars) for x in range(str_size))

    @staticmethod
    def census_char_number(string):
        """
         通用的统计字符串中字符出现次数的方法
        :param string: 源字符串
        :return: dict
        """
        char_dict = {}
        for a_char in string:
            if a_char in char_dict:
                char_dict[a_char] += 1
            else:
                char_dict[a_char] = 1
        return char_dict