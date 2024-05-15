ledDictionary = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 
       6: 6, 7: 3, 8: 7, 9: 6, 0: 6
}

ledsAmount = int(input())

for i in range(ledsAmount):
    counter = 0
    numbers = map(int,input())
    for j in numbers:
        counter += ledDictionary[j]
    print(counter, 'leds')