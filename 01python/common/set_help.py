
UNION = 'union'
INTERSECTION = 'intersection'
DIFFERENCE = 'diffenrence'


class SetHelper:

    @staticmethod
    def sets_relation(setA, setB, relation):
        """
         通用的用来获取两个集合的关系的方法
        :param setA,setB: 两个集合
        :param relation: 'union'-表示求并集 'intersection'-表示求交集 'difference'-表示求差
        :return: set
        """
        if not (isinstance(setA, set) and isinstance(setB, set)):
            raise TypeError
        else:
            if relation == UNION:
                return setA|setB
            if relation == INTERSECTION:
                return setA&setB
            if relation == DIFFERENCE:
                return setA-setB