### Run 
##### All tests
```bash
pytest tests/ --url=http://localhost/ --browser={browser} # browser: chrome, ie, firefox 
```

##### Tests from a particular package
```bash
pytest tests/{package_name} --url=http://localhost/ --browser={browser} # browser: chrome, ie, firefox 
```