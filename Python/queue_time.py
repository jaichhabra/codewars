
import numpy as np

customers = [20, 17, 38, 48, 28, 11, 44, 32, 21, 1, 31, 47, 43, 14, 33, 25, 1, 14, 30, 19, 38, 34, 25, 49, 39, 49, 17, 2, 26, 4, 44, 25, 17, 38, 3, 25, 22, 6, 45, 27, 17, 16, 28, 37, 48, 16, 32, 26, 29, 4, 26, 6, 49, 21, 9, 26, 26, 21, 3, 50, 4, 5, 30, 19, 15, 28, 37, 3, 28, 2, 11, 23, 21, 21, 22, 43, 21, 17, 46, 35, 45, 44, 45, 45, 49, 26, 43, 46, 4, 22, 6, 46, 4, 48, 33, 46, 13, 2, 40, 18, 2, 21, 32, 19, 19, 24, 44, 45, 30, 1, 5, 38, 33, 14, 50, 45, 19, 25, 2, 45, 25, 21, 47, 43, 18, 33, 10, 2, 31, 48, 47, 36, 16, 39, 48, 42, 9, 18, 10, 41, 25, 29, 15, 19, 9, 41, 24, 35, 50, 45, 34, 20, 20, 8, 16, 45, 29, 13, 21, 34, 38, 49, 30, 18, 14, 48, 37, 15, 10, 7, 48, 44, 17, 15, 13, 43, 29, 29, 27, 48, 39, 32, 47, 17, 48, 23, 49, 24, 14, 1, 3]

n = 5

l=[0]*n
for i in customers:
    l[l.index(min(l))]+=i
print(l) 

# queue = customers[:n]
 
# estim_time = 0
# while sum(queue) != 0 :
#     print(f'queue before quitting the till : {queue}')
#     queue_non_zero = []
#     for i in range(len(queue)):
#         if queue[i] != 0:
#             queue_non_zero.append(queue[i])
#     min_ = np.min(queue_non_zero)
    
#     for i in range(len(queue)):
#         if queue[i] != 0:
#             queue[i] = queue[i] - min_
#     estim_time += min_
#     print(f'minium of queue is {min_}')
#     print(f'queue after quitting the till : {queue}')
#     print(f'number of zeroes : {np.count_nonzero(queue)}')
#     if len(customers) - 1 >= n:
#         indices = [i for i, x in enumerate(queue) if x == 0]
#         queue[queue.index(0)] = customers[n]
#         n += 1
#     elif len(queue)  - np.count_nonzero(queue) == len(queue) - 1 :
#         estim_time += max(queue)
#         queue[queue.index(max(queue))] = 0
#     print(f'estimated time {estim_time}')
# # # # # # if len(set(customers)) > tills :
# # # # # #     estim_time = sum(set(customers))
# # # # # # elif len(set(customers)) == 0:
# # # # # #     estim_time = 0
# # # # # # elif len(set(customers)) <= tills :
# # # # # #     estim_time = max(set(customers))

# print(estim_time)







