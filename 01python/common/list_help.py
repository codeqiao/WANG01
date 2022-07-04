
class ListHelper:
    """
    列表助手类
    """
    @staticmethod
    def find_all(list_target,func_condition):
        """
        通用的在列表中查找多个元素的方法
        :param list_target: 查找的列表 
        :param func_condition: 查找的条件：函数类型
            函数名(参数) -->bool
        :return generator object
        """
        for item in list_target:
            if func_condition(item):
                yield item
    
    @staticmethod
    def find_single(list_target,func_condition):
        """
        通用的在列表中查找单个元素的方法
        :param list_target: 查找的列表 
        :param func_condition: 查找的条件：函数类型
            函数名(参数) -->bool
        :return 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target,func_condition):
        """
        通用的获取列表中满足条件的个数的方法
        :param list_target: 目标列表 
        :param func_condition: 计数的条件：函数类型
            函数名(参数) -->bool
        :return 满足条件元素的个数
        """
        count_value = 0
        for item in list_target:
            if func_condition(item):
                count_value+=1
        return count_value

    @staticmethod
    def is_exists(list_target,func_condition):
        """
        通用的判断某个条件是否在列表中是否存在的方法
        :param list_target: 目标列表 
        :param func_condition: 判断的条件：函数类型
            函数名(参数) -->bool
        :return bool　True：存在  False：不存在
        """
        for item in list_target:
            if func_condition(item):
                return True
        else:
            return False

    @staticmethod
    def sum(list_target,func_condition):
        """
        通用的列表求和的方法
        :param list_target: 查找的列表 
        :param func_condition: 求和的方式：函数类型
            函数名(参数) -->bool
        :return 和
        """
        sum = 0
        for item in list_target:
            sum+=func_condition(item)
        return sum
        
    @staticmethod
    def get_power_set(list_target):
        """
        通用的列表求幂集的方法
        :param list_target: 求幂集的列表 
        :return 幂集的集合
        """
        length = len(list_target)
        mark_list = [1<<i for i in range(0,length)]
        power_set_list = []
        for k in range(0,2**length):
            temp = []
            for idx, mst in enumerate(mark_list):
                if k&mst:
                    temp.append(list_target[idx])
            power_set_list.append(temp) 
        return power_set_list
