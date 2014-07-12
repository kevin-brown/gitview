/api/users/{users.username}/
is aliased to
/api/users/{users.id}/

List
====
A list of users is not accessible through the API.

Create
======
User creation is not supported through the API.

Retrieve
========
```json
{
    "links": {
        "users.repositories": {
            "href": "/api/users/{users.id}/links/repositories",
            "type": "repositories"
        }
    },
    "users": {
        "id": "uuid",
        "href": "/api/users/example",
        "type": "users",
        "name": "example",
        "email": "example@example.org",
        "created_at": "2014-07-06T20:00:00Z",
        "updated_at": "2014-07-06T20:00:00Z"
    }
}
```

Update
======
```http
PUT /users/example
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json

{
    "users": {
        "attribute": "value"
    }
}
```

Delete
======
```http
DELETE /users/example
```
