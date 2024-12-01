# 6 შექმენით რაიმე string ტიპის ცვლადი და დათვალეთ რამდენი ხმოვანია ამ string'ში.												
text = "Hello World"
vowels = "aeiouAEIOU"


vowel_count = sum(1 for char in text if char in vowels)




print(f"Number of vowels in text: {vowel_count}")