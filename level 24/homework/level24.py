def manual_count(string, count_char):
    # ვქმნით ცვლადს count რომელიც შეინახავს დასათვლელი სიმბოლოების რაოდენობას
    count = 0
    
    # ვიწყებთ ციკლს რომელიც გადის string-ის თითოეულ სიმბოლოზე
    for char in string:
        # თუ სიმბოლო char ემთხვევა count_char-ს count-ს ვზრდით 1-ით
        if char == count_char:
            count += 1
    
    # ვაბრუნებთ საბოლოო დათვლილ მნიშვნელობას
    return count

# მაგალითი გამოყენება: ვითვლით რამდენჯერ გვხვდება "რ" სტრინგში
result = manual_count("გამარჯობა, როგორ ხარ?", "რ")
print(result)  # დაბეჭდავს 2-ს, რადგან "რ" ორჯერ გვხვდება