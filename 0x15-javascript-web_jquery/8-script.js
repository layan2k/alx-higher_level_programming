$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  dataType: 'json'
}).done(function (data) {
  const stuff = data.results;

  for (i = 0; i < stuff.length; i++) {
    const title = stuff[i].title;
    const intoelement = `<li>${title}</li>`;
    $('ul#list_movies').append(intoelement);
  }
});
