cricket = {1, 2, 3, 4}
football = {3, 4, 5, 6}
master = {1, 2, 3, 4, 5, 6, 7, 8}

both = cricket & football
only_one = cricket ^ football
neither = master - (cricket | football)

print("Both:", both)
print("Only One:", only_one)
print("Neither:", neither)
