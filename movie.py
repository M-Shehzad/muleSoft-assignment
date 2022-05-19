import sqlite3


# CREATION OF DATABASE
# conn = sqlite3.connect('MOVIES.db')

# # CREATION OF TABLE
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
    conn = sqlite3.connect("MOVIES.db")
    c = conn.cursor()
    movie_name = input("Enter the movie name: ")
    actor_name = input("Enter the lead actor name: ")
    actress_name = input("Enter the lead actress name: ")
    director = input("Enter the director name: ")
    movie_year = int(input("Enter the year of release: "))
    c.execute("INSERT INTO MOVIES (movie_name,lead_actor,lead_actress,director,movie_year) VALUES (?,?,?,?,?)",
              (movie_name, actor_name, actress_name, director, movie_year))
    conn.commit()
    conn.close()


def selectMovie(movieName):
    conn = sqlite3.connect("MOVIES.db")
    c = conn.cursor()
    c.execute("SELECT * FROM MOVIES WHERE movie_name = ?", (movieName,))
    movie_details = c.fetchone()
    print(movieName+" details: ")
    print(movie_details)
    conn.commit()
    conn.close()


def actorDetails(actorName):
    conn = sqlite3.connect("MOVIES.db")
    c = conn.cursor()
    c.execute("""
    SELECT *
    FROM MOVIES
    WHERE lead_actor = ? OR lead_actress = ?
    """, (actorName, actorName))
    actorMovies = c.fetchall()
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


def directorDetails(directorName):
    conn = sqlite3.connect("MOVIES.db")
    c = conn.cursor()
    c.execute("""
    SELECT *
    FROM MOVIES
    WHERE director = ?
    """, (directorName,))
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


print("~~Movie Database~~")
while True:
    print("1. Insert a new movie")
    print("2. Select a movie")
    print("3. Display all the movies an actor/actress has starred in: ")
    print("4. Display all the movies directed: ")
    print("5. Exit")
    op = int(input("Enter your choice: "))

    if op == 1:
        insertMovie()
    elif op == 2:
        movieName = input("Enter the movie name: ")
        selectMovie(movieName)
    elif op == 3:
        actorName = input("Enter the actor Name: ")
        actorDetails(actorName)
    elif op == 4:
        directorName = input("Enter the Director Name:")
        directorDetails()
    elif op == 5:
        break
