# hello-flask

## Endpoints
Hello:
```
curl http://localhost:5000/hello?name=<Your name>
```

Set current name:
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Bengt"}' http://localhost:5000/hello
```

Square:
```
curl http://localhost:5000/square/<number>
```