movies=["Star Wars\n","Bladerunner\n","Django\n","Inglorious Bastards\n","Indiana Jones"]
file = open('movies.txt','w')
for film_title in movies:
    file.write(film_title)
file.close()