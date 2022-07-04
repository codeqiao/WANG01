import math
class Point:
    """点"""
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

class Straight:
    """直线"""
    def __init__(self, a:float, b:float, c:float):
        
        self.a = a
        self.b = b
        self.c = c

class Circle:
    """圆"""
    def __init__(self, center:Point, r:float):
        self.center = center
        self.r = r

class Segment:
    """线段"""
    def __init__(self,point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2

class Rect:
    """矩形:用四个线段表示"""
    def __init__(self, segement1:Segment,segement2:Segment,segement3:Segment,segement4:Segment):
        self.segement1 = segement1
        self.segement2 = segement2
        self.segement3 = segement3
        self.segement4 = segement4


class GetIntersection:
    """
    求直线与直线的交点
    直线与矩形的交点
    直线与圆的交点
    """
    def get_straight_and_straight_intersection(self, straight1:Straight,straight2:Straight):
        """求直线与直线的交点"""
        if (straight1.a*straight2.b - straight2.a*straight1.b) == 0:
            return None
        else:
            x = round((straight1.b*straight2.c - straight2.b*straight1.c)/(straight1.a*straight2.b - straight2.a*straight1.b), 2)
            y = round((straight2.a*straight1.c - straight1.a*straight2.c)/(straight1.a*straight2.b - straight2.a*straight1.b), 2)
            return Point(x,y)

    def get_straight_and_circle_intersection(self, straight:Straight, circle:Circle):
        """求圆和直线的交点"""
        point_list = []
        distance = abs(self.__get_signed_distance(straight,circle.center))
        if(distance>circle.r):
            """此时没有交点"""
            return point_list
        if(distance==circle.r):
            """此时有一个交点"""
            if straight.b == 0:
                if -straight.c/straight.a > circle.center.x:
                    point_list.append(Point(circle.center.x+circle.r, circle.center.y))
                    return point_list
                if - straight.c/straight.a < circle.center.x:
                    point_list.append(Point(circle.center.x-circle.r, circle.center.y))

            elif straight.a == 0:
                if - straight.c/straight.b > circle.center.y:
                    point_list.append(Point(circle.center.x,circle.center.y+circle.r))
                    return point_list
                if - straight.c/straight.b < circle.center.y:
                    point_list.append(Point(circle.center.x,circle.center.y-circle.r))
                    return point_list
            
            else:
                straight_vertial = self.get_rectangle_vertial(straight, circle.center)
                return point_list.append(self.get_straight_and_straight_intersection(straight, straight_vertial))
        else:
            """此时有两个交点"""
            lengthen = round(math.sqrt(circle.r**2-distance**2),2)
            straight_vertial = self.get_vertical_straight(straight, circle.center)
            if straight.b == 0:
                point_list.append(Point(-straight.c/straight.b,circle.center.y+lengthen))
                point_list.append(Point(-straight.c/straight.b,circle.center.y-lengthen))
                return point_list
            elif straight.a == 0:
                 point_list.append(Point(circle.center.x+lengthen,-straight.c/straight.b))
                 point_list.append(Point(circle.center.x-lengthen,-straight.c/straight.b))
                 return point_list
            else:
                shadow_point = self.get_straight_and_straight_intersection(straight, straight_vertial)
                #投影到直线与y轴的焦点的距离
                dis_shadow_point_to_y_point = math.sqrt(shadow_point.x**2+(shadow_point.y+straight.c/straight.b)**2)
                #单位向量e
                point_e = Point(shadow_point.x/dis_shadow_point_to_y_point,shadow_point.y/dis_shadow_point_to_y_point)
                point_list.append(Point(shadow_point.x+point_e.x*lengthen,shadow_point.y+point_e.y*lengthen))
                point_list.append(Point(shadow_point.x-point_e.x*lengthen,shadow_point.y-point_e.y*lengthen))
                return point_list



    def get_vertical_straight(self, straight:Straight, point:Point):
        if straight.b == 0:
            return Straight(0, 1, -point.y)
        elif straight.a == 0:
            return Straight(1, 0, -point.x)
        else:
            return Straight(straight.b, -straight.a, straight.a*point.y-straight.b*point.x)

    def get_straight_and_rect_intersection(self, straight:Straight, rectangle:Rect):
        """将一个矩形转化为四个线段来求解"""
        segement_list = [rectangle.segement1,rectangle.segement2,rectangle.segement3,rectangle.segement4]
        point_list = []
        
        for segement in segement_list:
            point = self.__get_straight_and_segement_section(straight = straight,segement=segement)
            if point != None:
                point_list.append(point)
            else:
                continue

        return self.__delete_list_repeat(point_list)
        
      
    def __delete_list_repeat(self, point_list:list):
        """删除列表中重复的点"""
        list_new = []
        for item in point_list:
            for item1 in list_new:
                if item1.x == item.x and item1.y == item.y:
                    break
            else:
                list_new.append(item)
        
        return list_new
       
    def __get_signed_distance(self, straight:Straight, point:Point):
        distance = (straight.a*point.x+straight.b*point.y+straight.c)/(math.sqrt(straight.a*straight.a+straight.b*straight.b))
        d = math.sqrt(distance*distance) #获取distance的绝对值
        if straight.b == 0:
            '''此时k==0垂直于x轴'''
            if point.x <= -straight.c/straight.a:
                return -distance # 点位于直线的左边，符号取负
            else:
                return distance 
        
        else:
            if point.y >= ((- straight.a/straight.b)*point.x - straight.c/straight.b):
                return distance # 此时点位于直线的上方 
            else:
                return -distance

    def __get_straight_and_segement_section(self, straight:Straight, segement:Segment):
        distance1 = self.__get_signed_distance(straight, segement.point1)
        distance2 = self.__get_signed_distance(straight, segement.point2)
        if distance1 * distance2 <= 0:
            # 当两个距离的乘积小于或等于零时则表示有交点
            distance1 = math.sqrt(distance1*distance1)
            distance2 = math.sqrt(distance2*distance2)
            k = distance1/(distance1 + distance2) # 求distance1所占的线段的比例
            if distance1 + distance2 == 0:
                return segement
            if distance1 + distance2 !=0 :
                return Point(segement.point1.x+k*(segement.point2.x-segement.point1.x),segement.point1.y+k*(segement.point2.y-segement.point1.y))
        else:
            return None

class ShapeHelper:
    @staticmethod
    def build_straight_object(a:float,b:float,c:float):
        """
        创建一个直线的对象
        :param a,b,c: 对应ax+by+c=0的三个a,b,c
        return: 直线的对象
        """
        return Straight(a,b,c)
    
    @staticmethod
    def build_point_object(x:float,y:float):
        """
        创建一个点的对象
        :param x,y: 点的坐标
        return: 点的对象
        """
        return Point(x,y)
    
    @staticmethod
    def build_circle_object(center:Point,r:float):
        """
        创建一个圆的对象
        :param center 圆心
        :param r 圆的半径
        return: 圆的对象
        """
        return Circle(center,r)
    
    @staticmethod
    def build_segment_object(point1:Point,point2:Point):
        """
        创建一个线段的对象
        :param point1 线段的一个点
        :param point2 线段的另一个点
        return: 线段的对象
        """
        return Segment(point1, point2)

    @staticmethod
    def build_rect_object(segement1:Segment,segement2:Segment,segement3:Segment,segement4:Segment):
        """
        创建一个矩形对象
        :param segement1-4 矩形的四个边（四条线段）
        return: 矩形的对象
        """
        return Rect(segement1, segement2, segement3, segement4)



        
if __name__ == "__main__":
    get = GetIntersection()

    #直线和直线的交点的测试案例
    straight1 = Straight(2,3,5)
    straight2 = Straight(1,6,9)
    point = get.get_straight_and_straight_intersection(straight1,straight2)
    print(point.x, point.y)

    #直线和矩形的交点的测试案例
    rectangle = Rect(Segment(Point(0,1),Point(2,1)),Segment(Point(0, 1),Point(0,0)),Segment(Point(0,0),Point(2,0)),Segment(Point(2,1),Point(2,0)))
    straight3 = Straight(1,-2,0)
    point_list = get.get_straight_and_rect_intersection(straight3, rectangle)
    for point in point_list:
        print ('(',point.x, point.y,')')

    # 直线和园的测试案例

    circle = Circle(Point(2,2),2)
    straight4 = Straight(0,1,-3)
    point_list = get.get_straight_and_circle_intersection(straight4, circle)
    for point in point_list:
        print ('(',point.x, point.y,')')

