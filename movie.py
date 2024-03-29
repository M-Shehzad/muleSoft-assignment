from msilib.schema import Error
import sqlite3


# CREATION OF DATABASE
conn = sqlite3.connect('MOVIES.db')

# CREATION OF TABLE
# c = conn.cursor()
# c.execute("""
# CREATE TABLE MOVIES(
# movie_name text PRIMARY KEY,
# lead_actor text,
# lead_actress text,
# director text,
# movie_year integer
# )
#  """)
# conn.commit()
# conn.close()


# insertion of movie
def insertMovie():
    try:
        conn = sqlite3.connect("MOVIES.db")
        c = conn.cursor()
        movie_name = input("Enter the movie name: ")
        actor_name = input("Enter the lead actor name: ")
        actress_name = input("Enter the lead actress name: ")
        director = input("Enter the director name: ")
        movie_year = int(input("Enter the year of release: "))
        c.execute("INSERT INTO MOVIES (movie_name,lead_actor,lead_actress,director,movie_year) VALUES (?,?,?,?,?)",
                  (movie_name.lower(), actor_name.lower(), actress_name.lower(), director.lower(), movie_year))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


def allMovies():
    try:
        conn = sqlite3.connect("MOVIES.db")
        c = conn.cursor()
        c.execute("SELECT * FROM MOVIES")
        allMovies = c.fetchall()
        for movie in allMovies:
            print("------------------------------")
            print("Movie name:"+movie[0])
            print("Lead Actor:"+movie[1])
            print("Lead Actress:"+movie[2])
            print("Director: " + movie[3])
            print("Movie year:"+str(movie[4]))
            print("------------------------------")
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


def selectMovie(movieName):
    try:
        conn = sqlite3.connect("MOVIES.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM MOVIES WHERE movie_name LIKE ?", ('%'+movieName.lower()+'%',))
        movie_details = c.fetchall()
        print("Results for "+movieName+":")
        for movie in movie_details:
            print("------------------------------")
            print("Movie name:"+movie[0])
            print("Lead Actor:"+movie[1])
            print("Lead Actress:"+movie[2])
            print("Director: " + movie[3])
            print("Movie year:"+str(movie[4]))
            print("------------------------------")
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


def actorDetails(actorName):
    try:
        conn = sqlite3.connect("MOVIES.db")
        c = conn.cursor()
        c.execute("""
        SELECT *
        FROM MOVIES
        WHERE lead_actor LIKE ? OR lead_actress LIKE ?
        """, ('%'+actorName+'%', '%'+actorName+'%'))
        actorMovies = c.fetchall()
        print(f"All the movies {actorName} has acted in:")
        for movie in actorMovies:
            print("------------------------------")
            print("Movie name:"+movie[0])
            print("Lead Actor:"+movie[1])
            print("Lead Actress:"+movie[2])
            print("Director: " + movie[3])
            print("Movie year:"+str(movie[4]))
            print("------------------------------")
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


def directorDetails(directorName):
    try:
        conn = sqlite3.connect("MOVIES.db")
        c = conn.cursor()
        c.execute("""
        SELECT *
        FROM MOVIES
        WHERE director LIKE ?
        """, ('%'+directorName.lower()+'%',))
        directorMovies = c.fetchall()
        for movie in directorMovies:
            print("------------------------------")
            print("Movie name:"+movie[0])
            print("Lead Actor:"+movie[1])
            print("Lead Actress:"+movie[2])
            print("Director: " + movie[3])
            print("Movie year:"+str(movie[4]))
            print("------------------------------")
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


while True:
    print("~~Movie Database~~")
    print("1. Insert a new movie")
    print("2. Display all Movies")
    print("3. Select a movie")
    print("4. Display all the movies an actor/actress has starred in: ")
    print("5. Display all the movies directed ")
    print("6. Exit")
    op = int(input("Enter your choice: "))

    if op == 1:
        insertMovie()
    elif op == 2:
        allMovies()
    elif op == 3:
        movieName = input("Enter the movie name: ")
        selectMovie(movieName)
    elif op == 4:
        actorName = input("Enter the actor Name: ")
        actorDetails(actorName)
    elif op == 5:
        directorName = input("Enter the Director Name:")
        directorDetails(directorName)
    elif op == 6:
        break
