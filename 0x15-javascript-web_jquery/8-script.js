let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function(data) {
  data.results.forEach(function(movie) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
