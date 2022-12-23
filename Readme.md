#### Test get token through "client credentials" grant type
```python
source /django-env/bin/activate

python manage.py runserver

python test_token.py

```

- What`s going wrong with resulting `{"error": "invalid_client"}`? The client secret is saved before auto hashed.