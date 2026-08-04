print("向前走5个路口后，右转到达：")
for i in range(1, 6): 
    print(f"向前走，经过第{i}个路口")
print("已走完5个路口，右转")
print("到达目的地！")

import random

print("\n路线2：向前走，直到碰到丁字路口后向左转：")
i = 1      
while True:                     
    is_t_junction = random.choice([True, False])
    if is_t_junction:
        print(f"向前走，经过第{i}个路口，是丁字路口！")
        print("左转")
        print("到达目的地！")
        break
    else:
        print(f"向前走，经过第{i}个路口，不是丁字路口，继续向前")
        i += 1
