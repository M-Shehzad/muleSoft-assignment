import sqlite3


# #CREATION OF DATABASE
# conn = sqlite3.connect('MOVIES.db')

# # CREATION OF TABLE
# c = conn.cursor()
# c.execute("""
# CREATE TABLE MOVIES(
# movie_name text PRIMARY KEY,
# movie_year integer
# )
#  """)

# c.execute("""
# CREATE TABLE MOVIE_CAST(
#     movie_name text,
#     actor_role text,
#     actor_name text,
#     PRIMARY KEY(movie_name,actor_role),
#     FOREIGN KEY (movie_name) REFERENCES MOVIES(movie_name) ON DELETE CASCADE
# )
# """)

# conn.commit()
# conn.close()


# insert function
def insertMovie():
    conn = sqlite3.connect("MOVIES.db")
    c = conn.cursor()
    movie_name = input("Enter the movie name: ")
    movie_year = int(input("Enter the year of release: "))
    c.execute("INSERT INTO MOVIES (movie_name,movie_year) VALUES (?,?)",
              (movie_name, movie_year))
    n = int(input("Enter the number of cast members: "))
    for i in range(1, n+1):
        actor_role = input("Enter the role of actor "+str(i)+":")
        actor_name = input("Enter the name of actor "+str(i)+":")
        c.execute("INSERT INTO MOVIE_CAST (movie_name,actor_role,actor_name) VALUES (?,?,?)",
                  (movie_name, actor_role, actor_name))
    conn.commit()
    conn.close()
    return


def selectMovie(movieName):
    conn = sqlite3.connect("MOVIES.db")
    c = conn.cursor()
    c.execute("SELECT * FROM MOVIES WHERE movie_name = ?", (movieName,))
    movie_details = c.fetchall()
    print(movieName+" details: ")
    print(movie_details)
    c.execute("SELECT * FROM MOVIE_CAST WHERE movie_name = ?", (movieName,))
    cast_details = c.fetchall()
    print(movieName + " cast:")
    print(cast_details)
    conn.commit()
    conn.close()


def actorDetails(actorName):
    conn = sqlite3.connect("MOVIES.db")
    c = conn.cursor()
    c.execute("""
    SELECT MOVIES.movie_name,movie_year,actor_role
    FROM MOVIES
    INNER JOIN MOVIE_CAST ON
    MOVIES.movie_name = MOVIE_CAST.movie_name
    WHERE actor_name = ?
    """, (actorName,))
    actorMovies = c.fetchall()
    for movie in actorMovies:
        print("------------------------------")
        print("Movie name:"+movie[0])
        print("Movie year:"+str(movie[1]))
        print("Actor Role:"+movie[2])
        print("------------------------------")
    conn.commit()
    conn.close()


print("~~Movie Database~~")
while True:
    print("1. Insert a new movie")
    print("2. Select a movie")
    print("3. show all the movies an actor has acted in")
    print("4. Exit")
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
        break
