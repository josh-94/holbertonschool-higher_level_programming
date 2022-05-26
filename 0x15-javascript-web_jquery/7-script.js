$.ajax('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .done((data) => $('#character').append(data.name));
