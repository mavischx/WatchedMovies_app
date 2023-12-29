#movie suggestion button
#Add movie, DISPLAY => ranking:Title(year),rating
#Search, enter name show ranking
#First/Last, show movie index 0/length-1
#Clear, all ""
#error when same movie entered again
#show all movies buttton
#show by rating

from tkinter import *
import random
from movie import Movie

window = Tk()
window.geometry("300x750")
window.title("WatchList")

#============================================================
# Event Handling Methods
class NoTitleEntered (Exception) : pass
class InvalidRankingError(Exception): pass
class DuplicateTitleError(Exception): pass

#display the movie in the entry boxes
def display(index):
    global current
    global movie
    movie = movieList[index]
    current=index
    title_entry.delete(0, END)
    title_entry.insert(END, movie.get_title())
    year_entry.delete(0, END)
    year_entry.insert(END, movie.get_release_year())
    genre_entry.delete(0, END)
    genre_entry.insert(END, movie.get_genre())
    ranking_entry.delete(0, END)
    ranking_entry.insert(END, movie.get_ranking())
    step_up_var.set(movie.get_rating())


def addMovieclick():
    try:
        addMovie()
    except NoTitleEntered:
        error_entry.delete(0, END)
        error_entry.insert(END, "No title entered")
    except DuplicateTitleError:
        error_entry.delete(0, END)
        error_entry.insert(END, "Same title already exists")

#let user add movie into the list
def addMovie():
    title = title_entry.get()
    genre = genre_entry.get()
    year = int(year_entry.get())
    rating = step_up_var.get()
    ranking = int(ranking_entry.get())

    # Check if the title is blank
    if not title.strip():
        raise NoTitleEntered("Title cannot be blank")

    if any (movie.get_title().lower() == title.lower() for movie in movieList):
        raise DuplicateTitleError("Movie with the same title already exists")

    new_movie = Movie(title, genre, year, rating,ranking)
    movieList.append(new_movie)

    numOfMovies()

def searchRankingClick():
    try:
        search_by_ranking()
    except InvalidRankingError:
        error_entry.delete(0, END)
        error_entry.insert(END, "Ranking out of range")


# allow users to know search up the movie by ranking
def search_by_ranking():
    global current
    search_ranking = search_entry_by_ranking.get()
    if not (1 <= int(search_ranking) <= len(movieList)):
        raise InvalidRankingError("Ranking out of range")
    else:
        for index, movie in enumerate(movieList):
            if movie.get_ranking() == int(search_ranking):
                current = index
                error_entry.delete(0, END)
                error_entry.insert(END, "")
                display(current)
                return
        error_entry.delete(0, END)
        error_entry.insert(END, "Movie not found")

#allow users to know search up the movie by title
def search_by_title():
    global current
    search_title = search_entry_by_title.get()
    for index,movie in enumerate(movieList):
        if movie.get_title().strip().lower()==(search_title.strip().lower()):
            current = index
            error_entry.delete(0, END)
            error_entry.insert(END, "")
            display(current)
            return

    error_entry.delete(0, END)
    error_entry.insert(END, "Movie not found")

#display all the movies in the list with the same rating
def showByrating():
    global current
    search_rating = showByrating_entry.get()
    ratelist = []
    for index, movie in enumerate(movieList):
        if movie.get_rating() == int(search_rating):
            current = index
            ratelist.append(index)
            error_entry.delete(0, END)
            error_entry.insert(END, "")

    movie_listbox.delete(0, END)  # Clear the current items in the listbox
    for index in ratelist:
        movie_info = f"{movieList[index].get_ranking()}: {movieList[index].get_title()} ({movieList[index].get_release_year()}), Rating: {movieList[index].get_rating()}"
        movie_listbox.insert(END, movie_info)

def nextCmd():
    global current
    if (current < (len(movieList) - 1)):
        current += 1
        display(current)
def prevCmd():
    global current
    if (current>0):
        current -= 1
        display(current)
def firstCmd():
    global current
    current = 0
    display(current)
    return movieList[current]

def lastCmd():
    global current
    current = len(movieList) - 1
    display(current)
    return movieList[current]

#show total of movies
def numOfMovies():
    num_movies = len(movieList)
    display_label.config(text=f"You have watched {num_movies} movie(s)")
def clear():
    title_entry.delete(0, END)
    year_entry.delete(0, END)
    genre_entry.delete(0, END)
    ranking_entry.delete(0, END)

#suggest a random movie from the list
def suggest():
    global current
    r = random.randint(0, len(movieList) - 1)
    current = r
    display(current)

#show all the movie in the list
def showAll():
    movie_listbox.delete(0, END)  # Clear the current items in the listbox
    for movie in movieList:
        # Display movie information in the listbox
        movie_info = f"{movie.get_ranking()}: {movie.get_title()} ({movie.get_release_year()}), Rating: {movie.get_rating()}"
        movie_listbox.insert(END, movie_info)



movie1 = Movie("Interstellar", "Sci-Fi", rating=5,release_year=2014, ranking=1)
movie2 = Movie("LaLaLand", "Music", rating=5,release_year=2016, ranking=2)
movie3 = Movie("Before Sunrise", "Romance",  rating=5,release_year=1995, ranking=3)
movie4 = Movie("Shutter Island", "Mystery", rating=4,release_year=2010, ranking=4)
movie5 = Movie("The Shawshank Redemption", "Drama", rating=4,release_year=1994, ranking=5)
movie6 = Movie("BoyHood", "Drama", rating=3,release_year=2014, ranking=6)
movie7 = Movie("The Dark Knight", "Action", rating=3,release_year=2008, ranking=7)
movie8 = Movie("Don't Look Up", "Sci-Fi",  rating=3,release_year=2021, ranking=8)
movie9 = Movie("Forrest Gump", "Drama", rating=4,release_year=1994, ranking=9)
movie10 = Movie("Jumanji", "Action", rating=2,release_year=1994, ranking=10)

# Create a list of Movie objects
movieList = [movie1, movie2, movie3, movie4, movie5,movie6, movie7, movie8, movie9, movie10]

# Set current and movie
global current
global movie
movie = movieList[0]
current = 0


# End of Method Declarations
#========================================================================
frame = Frame(window, width=200, height=1000)
frame.place(x=10,y=100)


movie_label = Label(window, text="WatchList", fg="black", font=("arial", 25, "bold"))
movie_label.place(x=70, y=30)

# Title Label and Entry
title_label = Label(frame, text="Title", fg="white", bg="black", width=15, font=("arial", 10, "bold"))
title_label.grid(row=0, column=0, sticky=W+E)
title_entry = Entry(frame)
title_entry.insert(END, 'Titanic')
title_entry.grid(row=0, column=1, sticky=W+E)

# Genre Label and Entry
genre_label = Label(frame, text="Genre", fg="white", bg="black", width=15, font=("arial", 10, "bold"))
genre_label.grid(row=1, column=0, sticky=W+E)
genre_entry = Entry(frame)
genre_entry.insert(END, 'Romance')
genre_entry.grid(row=1, column=1, sticky=W+E)

# Release Year Label and Entry
year_label = Label(frame, text="Release Year", fg="white", bg="black", width=15, font=("arial", 10, "bold"))
year_label.grid(row=2, column=0, sticky=W+E)
year_entry = Entry(frame)
year_entry.insert(END, '1997')
year_entry.grid(row=2, column=1, sticky=W+E)

# Ranking Label and Entry
ranking_label = Label(frame, text="Ranking", fg="white", bg="black", width=15, font=("arial", 10, "bold"))
ranking_label.grid(row=3, column=0, sticky=W+E)
ranking_entry = Entry(frame)
ranking_entry.insert(END, '11')
ranking_entry.grid(row=3, column=1, sticky=W+E)

# Rating Label and OptionMenu
rating_label = Label(frame, text="Rating", fg="white", bg="black", width=15, font=("arial", 10, "bold"))
rating_label.grid(row=4, column=0, sticky=W+E)
rating_list = ['1', '2', '3', '4', '5']
step_up_var = StringVar()
combo1 = OptionMenu(frame, step_up_var, *rating_list)
step_up_var.set("5")
combo1.grid(row=4, column=1, sticky=W+E)

# Add Movie Button
add_button = Button(frame, text="Add Movie", fg="black", bg="azure2", font=("arial", 10, "bold"), command=addMovieclick)
add_button.grid(row=5, columnspan=2, sticky=W+E)

# Navigation Buttons (Next, Prev, First, Last)
next_button = Button(frame, text="Next", fg="black", bg="azure3", font=("arial", 10, "bold"), command=nextCmd)
next_button.grid(row=6, column=0, sticky=W+E)
prev_button = Button(frame, text="Prev", fg="black", bg="azure3", font=("arial", 10, "bold"), command=prevCmd)
prev_button.grid(row=6, column=1, sticky=W+E)
first_button = Button(frame, text="First", fg="black", bg="azure3", font=("arial", 10, "bold"), command=firstCmd)
first_button.grid(row=7, column=0, sticky=W+E)
last_button = Button(frame, text="Last", fg="black", bg="azure3", font=("arial", 10, "bold"), command=lastCmd)
last_button.grid(row=7, column=1, sticky=W+E)

# Clear All Button
clear_button = Button(frame, text="Clear all", fg="black", bg="azure2", font=("arial", 10, "bold"), command=clear)
clear_button.grid(row=8, columnspan=2, sticky=W+E)

# Error Label and Entry
error_label = Label(frame, text="Error", fg="red", width=15, font=("arial", 10, "bold"))
error_label.grid(row=9, column=0, sticky=W+E)
error_entry = Entry(frame, fg="red")  # Adjust the width as needed
error_entry.grid(row=9, column=1, padx=5, pady=5, sticky=W+E)

# Display Label
display_label = Label(frame, text="No. of movies", fg="black", bg="azure2", width=15, font=("arial", 10, "bold"))
display_label.grid(row=10, columnspan=2, sticky=W+E)

# Suggest Button
suggest_button = Button(frame, text="Movie Suggestion!", fg="deeppink3",bg="mistyrose1", font=("arial", 10, "bold"), command=suggest)
suggest_button.grid(row=11, columnspan=2, sticky=W+E)

# Search by Ranking
search_button_by_ranking = Button(frame, text="Search by Ranking", fg="black", bg="azure3",font=("arial", 10, "bold"), command=searchRankingClick)
search_button_by_ranking.grid(row=12, column=0, sticky=W+E)
search_entry_by_ranking = Entry(frame)
search_entry_by_ranking.insert(END, " ")
search_entry_by_ranking.grid(row=12, column=1, sticky=W+E)

# Search by Title
search_button_by_title = Button(frame, text="Search by Title", fg="black",bg="azure3", font=("arial", 10, "bold"), command=search_by_title)
search_button_by_title.grid(row=13, column=0, sticky=W+E)
search_entry_by_title = Entry(frame)
search_entry_by_title.insert(END, " ")
search_entry_by_title.grid(row=13, column=1, sticky=W+E)

# Show by Rating
showByrating_button = Button(frame, text="Show by Rating", fg="black",bg="azure3", font=("arial", 10, "bold"), command=showByrating)
showByrating_button.grid(row=14, column=0, sticky=W+E)
showByrating_entry = Entry(frame)  # Adjust the width as needed
showByrating_entry.grid(row=14, column=1, padx=5, pady=5, sticky=W+E)

# Show All Movies
showAll_button = Button(frame, text="Show all movies", fg="black",bg="azure3", font=("arial", 10, "bold"), command=showAll)
showAll_button.grid(row=15, columnspan=2, sticky=W+E)

# Movie Listbox
movie_listbox = Listbox(window, height=15, width=45)
movie_listbox.place(x=10, y=550)

# Definitions
#=====================================================================

numOfMovies()
mainloop()