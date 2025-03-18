#recursive factorial number
def factorial(n : int):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a Factorial num: "))
print(f"Factorial from {num} is {factorial(num)}")
print()

#-----------------------------------------------------------------------------------------------------------------------

#recursive fibonaci number
def fibonaci(n : int):
    if n <=1:
        return n
    return fibonaci(n -1) + fibonaci(n - 2)

num = int(input("Enter a Fibonacci num: "))
print(f"Fibonacci from {num} is {fibonaci(num)}")
print()

#-----------------------------------------------------------------------------------------------------------------------

#recursive reverse list
my_lst = [1, 2, 3, 4, 5, 6]
def reverse(n):
    if len(n) == 0:
        return n
    return reverse(n[1:]) + [n[0]]

print(f"Your reversed list is: {reverse(my_lst)}")
print()

#-----------------------------------------------------------------------------------------------------------------------

#recursive sum numbers
def sum_nums(numbers:list[int]):
    if numbers == 0:
        return 0

    return numbers[0] + sum(numbers[1:])
print(sum_nums([1,2,3]))
print(sum_nums([10,20,30]))
print()