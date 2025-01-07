def find_bolinuvchi(number):
    if number <= 0:
        return "Iltimos, musbat butun son kiriting."
    
    find_bolinuvchi = []
    for i in range(1, number + 1):
        if number % i == 0:
            find_bolinuvchi.append(i)
    return find_bolinuvchi
try:
    user_input = int(input("Bo'luvchilarni aniqlash uchun son kiriting: "))
    result = find_bolinuvchi(user_input)
    print(f"{user_input} sonining bo'luvchilari: {result}")
except ValueError:
    print("Iltimos, faqat butun son kiriting!")

    

    
