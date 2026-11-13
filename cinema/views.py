from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Genre, Movie, Comment


def home(request):
    return render(request, 'home.html')



def movie_list(request):
    q = request.GET.get('q')
    
    movies = Movie.objects.all()
    if q:
        movies = movies.filter(
            Q(title__icontains=q) | Q(genre__name__icontains=q)
        )


    return render(request, 'show_movies.html', {'movies': movies, 'q': q})





def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)

    comments = Comment.objects.filter(movie=movie)
    return render(request, 'show_movie.html', {'movie': movie, 'comments': comments})





def movie_create(request):

    if request.method == 'POST':
        data = request.POST

        Movie.objects.create(

            title=data['title'],
            description=data['description'],
            year=data['year'],
            genre_id=data['genre'],
            poster=request.FILES['poster']
        )

        return redirect('movie_list')
    
    genres = Genre.objects.all()
    return render(request, 'create_movie.html', {'genres': genres})





def movie_update(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':

        data = request.POST
        movie.title = data['title']
        movie.description = data['description']
        movie.year = data['year']
        movie.genre_id = data['genre']
        
        if 'poster' in request.FILES:
            movie.poster = request.FILES['poster']

        movie.save()

        return redirect('movie_detail', id=movie.id)
    
    genres = Genre.objects.all()
    return render(request, 'edit_movie.html', {'movie': movie, 'genres': genres})







def movie_delete(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()

        return redirect('movie_list')
    return render(request, 'delete_movie.html', {'movie': movie})



def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'show_genres.html', {'genres': genres})





def genre_create(request):

    if request.method == 'POST':
        data = request.POST
        name = data['name']
        if Genre.objects.filter(name=name).exists():
            return render(request, 'create_genre.html', {'error': True})

        
        Genre.objects.create(
            name=name
            
        )
        
        return redirect('genre_list')
    return render(request, 'create_genre.html')





def genre_update(request, id):
    genre = get_object_or_404(Genre, pk=id)

    if request.method == 'POST':
        data = request.POST
        name = data['name']

        if name != genre.name and Genre.objects.filter(name=name).exists():
            return render(request, 'edit_genre.html', {'genre': genre, 'error': True})
        
        genre.name = name
        genre.save()

        return redirect('genre_list')
    return render(request, 'edit_genre.html', {'genre': genre})




def genre_delete(request, id):
    genre = get_object_or_404(Genre, pk=id)


    if request.method == 'POST':
        genre.delete()


        return redirect('genre_list')
    
    return render(request, 'delete_genre.html', {'genre': genre})



def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'show_comments.html', {'comments': comments})






def comment_create(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
    
        data = request.POST
    
        Comment.objects.create(
            movie=movie,
            author_name=data['author_name'],
            text=data['text']
        )
        
        return redirect('movie_detail', id=movie.id)
    return render(request, 'create_comment.html', {'movie': movie})




def comment_update(request, id):
    comment = get_object_or_404(Comment, pk=id)

    if request.method == 'POST':
        data = request.POST

        comment.author_name = data['author_name']
        comment.text = data['text']
        comment.save()

        return redirect('comment_list')
    return render(request, 'edit_comment.html', {'comment': comment})




def comment_delete(request, id):
    comment = get_object_or_404(Comment, pk=id)

    if request.method == 'POST':
        comment.delete()
    
        return redirect('comment_list')
    return render(request, 'delete_comment.html', {'comment': comment})
