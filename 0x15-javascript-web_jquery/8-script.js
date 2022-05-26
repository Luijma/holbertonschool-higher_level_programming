$.get('https://swapi-api.hbtn.io/api/films/?format=json', (movies) => {
  for (const movie of movies.results) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  }
});
