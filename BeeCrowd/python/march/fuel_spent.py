def getDistance(hours, speed):
    return speed * hours

def getLitersSpent(kilometers):
    return kilometers/12
    
hours = int(input())
speed = int(input())
print('{:.3f}'.format(getLitersSpent(getDistance(hours, speed))))