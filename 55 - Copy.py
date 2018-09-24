
animals = {
    'kind': "kind",
    'breeds': "breeds",
    'price':"price"
    }
    
while True:
    print("Welcome To Animals Zoo")
    question_1 = input("do you wanna buy an animals? (y)es (p)ick up (n)o? ")
    if question_1 == 'y':
        animals_1 = input("which animals do you wanna buy? ")
        animals_2 = input("which breed do you prefer? ")
        animals_3 = input("what is the price for dog? ")
        animals['kind:'] = animals_1
        animals['breeds:'] = animals_2
        animals['price:'] = animals_3
    elif question_1 == 'p':
        for k,v in animals.items():
            print(k,v)
    else:
        break

