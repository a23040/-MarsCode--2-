# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:18:23 2025

@author: a5261
"""

from collections import deque

def solution(n: int, k: int, data: list) -> int:
    assert n == len(data)  # 确保输入的天数n与数据列表data的长度一致
    assert k < n  

    mins = deque()  # 创建一个双端队列,len=0,为空
    result = 0  # 初始化总花费为0

    for j in range(n):  
        while len(mins) > 0 and mins[-1][1] > data[j]:
            # 如果队列不为空且队列末尾的价格大于当前天的价格，则弹出队列末尾元素
            mins.pop()   # # mins中移除了尾部元素
        mins.append([j, data[j]])  # 将当前天的价格和天数加入队列
        #print(mins,len(mins),mins[-1][0],mins[-1][1])
        while mins[0][0] <= j - k:  # 第j天的食物不可以在第mins[0][0]天买，则移除对应的元素
            mins.popleft()   
            # mins中移除了头部元素
            #print("<= j - k",mins)
        result += mins[0][1]  # 将队列头部元素的价格加到总花费中
    return result  # 返回总花费

if __name__ == '__main__':
    print(solution(n = 5 ,k = 2 ,data = [1, 2, 3, 3, 2]) == 9)
    print(solution(n = 6 ,k = 3 ,data = [4, 1, 5, 2, 1, 3]) == 9)
    print(solution(n = 4 ,k = 1 ,data = [3, 2, 4, 1]) == 10)