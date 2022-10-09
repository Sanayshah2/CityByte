## Steps to Check Code Coverage

Install Requirements.
```
pip install -r requirements.txt
```

To run coverage for both the applications info and search.
```
python -m coverage run --source=info,search --omit=*/migrations/* ./manage.py test
```

To generate the report of coverage from above coverage run.
```
python -m coverage report
```

To generate index.html in htmlcov
```
python -m coverage html
```

![](https://github.com/therealppk/CityByte/blob/main/docs/assets/code_coverage.png)
