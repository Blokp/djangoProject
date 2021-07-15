## General info
Simple app written in Django to check current BTC price, hash information about people and sort them by name and surname

## Setup
To run server locally, clone repo and run start_local.sh script. Installed Docker is required to run the app.

## Using app
 * Locally -
 curl -X POST -H "Content-Type: application/json" -d @test_file.json localhost:8000/zadanie1
 * On the server -
 curl -X POST -H "Content-Type: application/json" -d @test_file.json https://invulnerable-moliere-06811.herokuapp.com/zadanie1/
 * Valid json for zadanie1
 ```json
{
  "data_list": [
    {"first_name": "Stefan", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
  ]
}
```
* Valid json for zadanie2
 ```json
{
    "buy": "0.1234"
}

```
