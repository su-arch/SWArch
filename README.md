# SWArch

## Run
`~/SWArch/5200_flask_app: flask run`

## Docs
[address sheet](https://docs.google.com/spreadsheets/d/1xICn3orrbPI6uKnEBG2G12yB0st0GDQ7WzzVTKFiuEw/edit#gid=0)

[the 3rd paper](https://docs.google.com/document/d/1Y2ppWUZipnUZcrbwpIJknaRZC5otsBlZKqsKTe8RTR0/edit)

[mongoDB](https://cloud.mongodb.com/v2/5e489c3e79358e377c805caa#clusters)

## Database
1. start mongodb: `mongo --authenticationDatabase admin`
2. use mongodb terminal: `mongo --port 27017 --authenticationDatabase admin`
3. create a db called `arch` in the terminal: `use arch;` //it's not created actually until you insert some ducuments into it
4. create a collection: `db.createCollection("addresses");`
4. insert a document into the collection: `db.addresses.insert({"name":"test"});`

## Helpful links

[MongoDB tutorial](https://www.tutorialspoint.com/mongodb/)