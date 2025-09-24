fn main():
    let nums = [1, 2, 3]
    print("Len of nums:", len(nums))
    append(nums, 4)
    print("After append:", nums)
    print("Square root of 9:", sqrt(9))
    print("Upper:", upper("flux"))
    print("Random number:", random())
    write_file("out.txt", "Hello from Flux!")
    print("File contents:", read_file("out.txt"))
