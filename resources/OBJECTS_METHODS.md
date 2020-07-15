# Useful {Model}.objects attributes

{model} ==> Any class extends `django.db.models.Model`.

| Attribute | Description |
|---------- |------------ |
| {model}.objects.all() | Retrieve a list of **all rows** for this model from the database |
| {model}.objects.count() | Returns **number of rows** for this model from the database |
| {model}.objects.get(pk=[primaryKey]) | Return an object of the **row with a specific primary key** for this model from the database |
