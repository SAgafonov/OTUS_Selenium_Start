### Run 
##### All tests
```bash
pytest tests/ --url=http://localhost/ --browser={browser} # browser: chrome, ie, firefox.
```
<div>Default value for 'url' is "http://localhost/"</div>
<div>Default value for 'browser' is "chrome" </div>

#### Tests from a particular package
```bash
pytest tests/{package_name} 
```

#### Run tests using grid
```bash
pytest tests/{package_name} --remote_type={type} --executor-url={url} 
```
<div>'remote_type' accepts "local", "local_grid", "cloud". For "local_grid", "cloud" options 'executor-url' must be provided</div>
"local" means no grid.
<div>In 'executor-url' the URL where tests will be executed should be provided</div>