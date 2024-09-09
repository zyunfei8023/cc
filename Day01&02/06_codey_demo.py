import random

rooms =[
    [],
    [],
    []
]

teachers=['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']

for teacher in teachers:
    room_id = random.randint(0,2)
    rooms[room_id].append(teacher)
    
    
index=0
for room in rooms:
    count=len(room)
    print("房间{}人数{}:{}".format(index,count,room))
    index+=1