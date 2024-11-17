# thanks-giving-recipe-api
simple api :)

# use trough web: (view only)
go to:
`https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes`

# how to use with curl
## get:
`curl https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes`
## add:
```
curl -X POST https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes \
  -H "Content-Type: application/json" \
  -d '{
    "name": "YOUR-RECIPE-NAME",
    "ingredients": ["YOUR INGREDIENTS"],
    "steps": ["STEPS FOR YOUR RECIPE"]
  }'
```
## delete:
`curl -X DELETE https://your-flask-api.vercel.app/thanksgivingrecipes/best-turkey-gravy`

# how to use with postman:
## get:
in the request bar change it to GET if not already on GET and then enter this:
`https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes`
## add:
### in the request bar change GET to POST and enter: 
`https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes`
### for the rest its the same:
```
"name": "YOUR-RECIPE-NAME",
"ingredients": ["YOUR INGREDIENTS"],
"steps": ["STEPS FOR YOUR RECIPE"]
```
## delete:
### in the request bar change GET to DELETE
### then enter this:
`https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes/RECIPE-NAME`

## static website for instructions:
### [here](https://webbrowser11.github.io/thanks-giving-recipe-api/)

## website for usage:
### [endpoint here](https://thanks-giving-recipe-api.vercel.app)
### [usage link here](https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes)
