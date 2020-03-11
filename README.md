# SWArch

## Run
`~/SWArch/5200_flask_app: flask run`

## Docs
[address sheet](https://docs.google.com/spreadsheets/d/1xICn3orrbPI6uKnEBG2G12yB0st0GDQ7WzzVTKFiuEw/edit#gid=0)

[the 3rd paper](https://docs.google.com/document/d/1Y2ppWUZipnUZcrbwpIJknaRZC5otsBlZKqsKTe8RTR0/edit)

[mongoDB](https://cloud.mongodb.com/v2/5e489c3e79358e377c805caa#clusters)

## UI
* The `UI` relies on the `Bootstrap` and `JavaScript`.
* Navigating to the `upload` page, you will be greeted with a drop down menu where you choose the country to upload.
* Selecting a country triggers an `Ajax` request to a `form factory` that returns correct version of the form based on country selected.
* Client side validation is responsible for ensuring that the `required fields` for that country are not empty.

### Form Factory
* It is instantiated through the factory pattern.
* It consults rules tables for the fields to be provided for countries.

## API
* The `Api` can be invoked by the application as well as the user.
* The `API` receives requests, either from the UI or from a service such as `curl`.
* When calling the `API` for upload or query, `Country Data` must always be provided in `JSON` format.
* `API` provides `four` endpoints.
* The `home(/api)` endpoint gives information about accessible endpoints and accepted data format.
* The `upload(/api/upload)` and `query(/api/query)` endpoints are invoked by the UI through `POST` requests to upload and query the address data. 
* The address can also be directly updated using `/api/update/{addressID}` endpont. This accepts the `PUT` requests and expects `JSON` payload with the addressID.  

## Database
1. start mongodb: `mongo --authenticationDatabase admin`
2. use mongodb terminal: `mongo --port 27017 --authenticationDatabase admin`
3. create a db called `arch` in the terminal: `use arch;` //it's not created actually until you insert some ducuments into it
4. create a collection: `db.createCollection("addresses");`
4. insert a document into the collection: `db.addresses.insert({"name":"test"});`

## Helpful links

[MongoDB tutorial](https://www.tutorialspoint.com/mongodb/)
