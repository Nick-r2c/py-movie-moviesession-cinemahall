from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )


def get_movies_sessions(session_date: str | None = None) -> QuerySet:

    if session_date:
        date_obj = datetime.strptime(session_date, "%Y-%m-%d")
        return MovieSession.objects.filter(show_time__date=date_obj)

    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
