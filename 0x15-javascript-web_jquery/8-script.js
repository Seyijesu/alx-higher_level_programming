$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  $.each(data.results, function (index, value) {
    $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
  });
});
