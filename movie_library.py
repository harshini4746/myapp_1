import xml.etree.ElementTree as ET
import os

XML_FILE = "movies.xml"

def initialize_xml():
    if not os.path.exists(XML_FILE):
        root = ET.Element("movies")
        tree = ET.ElementTree(root)
        tree.write(XML_FILE)

def add_movie(movie_id, title, director, genre, rating):
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    
    movie = ET.Element("movie")
    ET.SubElement(movie, "id").text = movie_id
    ET.SubElement(movie, "title").text = title
    ET.SubElement(movie, "director").text = director
    ET.SubElement(movie, "genre").text = genre
    ET.SubElement(movie, "rating").text = str(rating)
    
    root.append(movie)
    tree.write(XML_FILE)
    print("Movie added!")

def view_movies():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    print("Movie List:")
    for movie in root.findall("movie"):
        print(f"ID: {movie.find('id').text}, Title: {movie.find('title').text}, Director: {movie.find('director').text}, Genre: {movie.find('genre').text}, Rating: {movie.find('rating').text}")

def search_movie(movie_id):
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    for movie in root.findall("movie"):
        if movie.find('id').text == movie_id:
            print("Movie Found:")
            print(f"ID: {movie.find('id').text}, Title: {movie.find('title').text}, Director: {movie.find('director').text}, Genre: {movie.find('genre').text}, Rating: {movie.find('rating').text}")
            return
    print("Movie not found!")

if __name__ == "__main__":
    initialize_xml()
    while True:
        print("\n1. Add Movie\n2. View Movies\n3. Search Movie\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            movie_id = input("Enter ID: ")
            title = input("Enter Title: ")
            director = input("Enter Director: ")
            genre = input("Enter Genre: ")
            rating = input("Enter Rating: ")
            add_movie(movie_id, title, director, genre, rating)
        elif choice == "2":
            view_movies()
        elif choice == "3":
            movie_id = input("Enter ID to search: ")
            search_movie(movie_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")