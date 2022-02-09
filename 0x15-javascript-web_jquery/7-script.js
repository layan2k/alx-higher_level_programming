$.ajax({
    url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
    dataType: 'json'
  }).done(function(data) {
    $(#character).text(data.name)
  });
