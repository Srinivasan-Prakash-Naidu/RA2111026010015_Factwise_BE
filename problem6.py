def number_to_words(n):
    to_19 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
             'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    def words(num):
        if num == 0:
            return []
        elif num < 20:
            return [to_19[num-1]]
        elif num < 100:
            return [tens[num // 10 - 2]] + words(num % 10)
        elif num < 1000:
            return [to_19[num // 100 - 1]] + ['hundred'] + (['and'] + words(num % 100) if num % 100 != 0 else [])
        else:
            return ['one', 'thousand']
    
    return words(n)

def count_letters(n):
    return sum(len(word) for word in number_to_words(n))

total_letters = sum(count_letters(i) for i in range(1, 1001))
print(total_letters)

