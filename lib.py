books = ["Python Basics", "Data Science", "AI Guide", "Math for CS"]
copies = [3, 0, 2, 1]

available = list(filter(lambda x: x[1] > 0, zip(books, copies)))
print("Available books:")
for b, c in available:
    print(f"{b} - {c} copies")

fees = [10, 20, 15, 25]
updated_fees = list(map(lambda f: f + 5, fees))
print("\nUpdated late fees:")
for b, f in zip(books, updated_fees):
    print(f"{b}: {f}")

chosen = "Data Science"
print("\nChecking chosen book:", chosen)
for b, c in zip(books, copies):
    if b == chosen:
        if c == 0:
            print("Book not available, stopping program.")
            break
        else:
            print("Book is available.")
