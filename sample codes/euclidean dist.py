def euclidean_distance(x1,y1,x2,y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distance

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    distance = euclidean_distance(x1, y1, x2, y2)
    print('Distance: %.2f'%distance)