## Run

```shell
bash bootstrap.sh
```

## Load Custom Modules

Check that modules from *./modules/* were loaded (using the python console)

```python
mm = slicer.app.moduleManager()
mm.modulesNames()
```