/api/users/{repositories.owner.username}/links/repositories/{repositories.name}/
is aliased to
/api/repositories/{repositories.id}

List
====
Repositories can be listed for either users or organizations.

```json
{
    "links": {
        "repositories.owner": {
            "href": "/api/users/{repositories.owner}",
            "type": "users"
        }
    },
    "repositories": [
        {
            "id": "example",
            "href": "/api/users/example/repositories/example",
            "type": "repositories",
            "private": false,
            "homepage": "http://example.org",
            "links": {
                "owner": "example"
            }
        },
        {
            "id": "test",
            "href": "/api/users/example/repositories/test",
            "type": "repositories",
            "private": true,
            "homepage": null,
            "links": {
                "owner": "example"
            }
        }
    ]
}
```

Create
======
```http
POST /api/users/example/repositories/

{
    "repositories": {
        "id": "new",
        "private": false,
        "homepage": "http://new.example"
    }
}
```

```json
{
    "links": {
        "repositories.owner": {
            "href": "/api/users/{repositories.owner}",
            "type": "users"
        }
    },
    "repositories": {
        "id": "new",
        "href": "/api/users/example/repositories/new",
        "type": "repositories",
        "private": false,
        "homepage": "http://new.example",
        "links": {
            "owner": "example"
        }
    }
}
```

Retrieve
========

Update
======

Delete
======
```http
DELETE /users/example/repositories/example
```
