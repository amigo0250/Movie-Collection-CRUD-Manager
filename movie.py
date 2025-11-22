movies = []
def add_movie():
    print("\n=== Add Movie ===")
    name = input("Enter movie name: ")
    year = input("Enter release year: ")
    rating = input("Enter rating (out of 10): ")

    movie = {"name": name, "year": year, "rating": rating}
    movies.append(movie)

    print("Movie added successfully!\n")


def view_movies():
    print("\n=== Movie Collection ===")
    if not movies:
        print("No movies found.\n")
        return

    for idx, movie in enumerate(movies):
        print(f"{idx + 1}. {movie['name']} ({movie['year']}) - Rating: {movie['rating']}/10")
    print()


def update_movie():
    print("\n=== Update Movie ===")
    view_movies()

    if not movies:
        return

    try:
        index = int(input("Enter movie number to update: ")) - 1
        if index < 0 or index >= len(movies):
            print("Invalid selection!\n")
            return
    except:
        print("Invalid input!\n")
        return

    name = input("Enter new name (leave blank to keep same): ")
    year = input("Enter new year (leave blank to keep same): ")
    rating = input("Enter new rating (leave blank to keep same): ")

    if name:
        movies[index]["name"] = name
    if year:
        movies[index]["year"] = year
    if rating:
        movies[index]["rating"] = rating

    print("Movie updated successfully!\n")


def delete_movie():
    print("\n=== Delete Movie ===")
    view_movies()

    if not movies:
        return

    try:
        index = int(input("Enter movie number to delete: ")) - 1
        if index < 0 or index >= len(movies):
            print("Invalid selection!\n")
            return
    except:
        print("Invalid input!\n")
        return

    movies.pop(index)
    print("Movie deleted successfully!\n")


def menu():
    while True:
        print("===== Movie Collection CRUD =====")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            update_movie()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


menu()
