#! /usr/bin/env python
# coding=utf8

import sys

NONE = 0
WHITE = 1
BLACK = 2


# 定义一个人
class Person(object):
    def __init__(self, no):
        self.no = no
        """:type: int"""
        self.color = 0
        """:type: int"""
        self.friends = set()
        """:type: set[Person]"""
        self.done = False

    def __hash__(self):
        return hash(self.no)

    def __eq__(self, other):
        if self.no == other.no:
            return True
        return False

    def __ne__(self, other):
        if self.no != other.no:
            return True
        return False

    def set_done(self):
        self.done = True

    def add_friends(self, person):
        """:type person: Person"""
        self.friends.add(person)

    def set_color(self, color):
        """
        :type color: int
        :rtype: bool
        """
        if self.color != 0 and self.color != color:
            print 'no[%s] has already color[%s] != color[%s]' % (self.no, self.color, color)
            return False
        self.color = color
        # print 'no[%s] set color[%s]' % (self.no, self.color)
        return True


# 设置彼此之间的关系
def set_friends(p_map, i, j):
    """
    :type p_map: dict[int, Person]
    :type i: int
    :type j: int
    :return: None
    """
    p_map[i].add_friends(p_map[j])
    p_map[j].add_friends(p_map[i])


# 遍历其朋友节点
def iterate_friends(person):
    """
    :type person: Person
    :rtype: None
    """
    # 计算朋友颜色
    friend_color = NONE
    if person.color == WHITE:
        friend_color = BLACK
    elif person.color == BLACK:
        friend_color = WHITE

    # 先广度
    for friend in person.friends:
        if not friend.set_color(friend_color):
            sys.exit()
    person.set_done()

    # 再深度
    for friend in person.friends:
        if not friend.done:
            iterate_friends(friend)


# 二分组
def bin_device(persons):
    """
    :type persons: list[Person]
    :return: None
    """
    # 定义子集
    white = set()
    """:type: set[Person]"""
    black = set()
    """:type: set[Person]"""

    # 遍历所有人
    persons[0].set_color(WHITE)
    for person in persons:
        # print 'iterate no[%s] has color[%s]' % (person.no, person.color)
        iterate_friends(person)

    # 分组
    for person in persons:
        if person.color == BLACK:
            black.add(person)
        elif person.color == WHITE:
            white.add(person)
    white = sorted(white, cmp=lambda x, y: cmp(x.no, y.no))
    black = sorted(black, cmp=lambda x, y: cmp(x.no, y.no))

    # 输出
    print 'white: '
    for person in white:
        print person.no
    print 'black: '
    for person in black:
        print person.no


def __main__():
    # 所有人
    p_map = dict()
    for i in xrange(1, 9):
        p_map[i] = Person(i)

    # 人与人之间的关系
    set_friends(p_map, 1, 5)
    set_friends(p_map, 1, 7)
    set_friends(p_map, 2, 5)
    set_friends(p_map, 3, 5)
    set_friends(p_map, 3, 6)
    set_friends(p_map, 4, 7)
    set_friends(p_map, 4, 8)

    # 二分组
    bin_device(p_map.values())


if __name__ == '__main__':
    __main__()

