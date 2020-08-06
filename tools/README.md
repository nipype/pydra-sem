### Contents

* `xmls`: a directory containing all the xmls from which pydra tasks should be generated.
* `generate_tasks.py`: the script which automatically generates pydra tasks.

### How to use

`tools/generate_tasks.py` takes 2 optional arguments: the `output directory` and the `xml directory`.

```bash
python tools/generate_tasks.py [output directory] [xml directory]
```

* `output directory`: the directory that the generated tasks should be rooted at.
If omitted the current working directory is used.
* `xml directory`: a directory which contains xmls. The names of the xmls must match the names in module_list.
If omitted binary files are used which must be found on the default path.

### Command to use

```bash
python tools/generate_tasks.py pydra/tasks/sem/ tools/xmls/
```
