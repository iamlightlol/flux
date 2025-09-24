# File IO test
write_file("test.txt", "Flux says hi!")
let data = read_file("test.txt")
print("file contents:", data)
