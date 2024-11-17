# thanks-giving-recipe-api
simple api :)

# use trough web: (view only)
go to:
`https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes`

# how to use with curl
get list:
`curl https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes`
add:
```
curl -X POST https://thanks-giving-recipe-api.vercel.app/thanksgivingrecipes \
  -H "Content-Type: application/json" \
  -d '{
    "name": "YOUR RECIPE NAME",
    "ingredients": ["YOUR INGREDIENTS"],
    "steps": ["STEPS FOR YOUR RECIPE"]
  }'
```
delete:
`curl -X DELETE https://your-flask-api.vercel.app/thanksgivingrecipes/best-turkey-gravy`
