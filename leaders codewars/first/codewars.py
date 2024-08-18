#8kyu

# class Cat(Animal):
#     def speak(self):
#         return f'{self.name} meows.'
# class Cat extends Animal {
#   speak() {
#     return `${this.name} meows.`;
#   }
# }

#7kyu

def multiply_all(nums):
    def mult(multer):
        multed = []
        for i in nums:
            answer = i * multer
            multed.append(answer)
        return multed
    return mult

#7kyu

def is_divisible(*numbers):
    first = numbers[0]
    rest = numbers[1:]
    
    for i in rest:
        if first % i != 0:
            return False
    return True

print(is_divisible((12,6,7)))

#8kyu

# class Human {}

# class Man extends Human {}

# class Woman extends Human {}

# class God {
#   static create() {
#     return [new Man(), new Woman()];
#   }
# }
