class Circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius**2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


message = 'hello satya '
print(len(message))

print(message[0:4])
print(message[0:])

message1 = 'computer' + 'science'
print(message1)


helloSpaced = ''
for ch in 'hello':
    helloSpaced = helloSpaced + ch + ' '

print(helloSpaced)


#function count

def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input('enter string: ')
vowel_count = count_vowels(input_string)
print('number of vowels:' , vowel_count)


message = 'mohit is a god boy '
new_string = message.replace('mohit','sumit')
print(new_string)
























































