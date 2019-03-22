# cm-redactor-cli

### Install:
 * Install requirements using `pip install -r requirements.txt`
 * Clone git repo in the right folder: `git clone https://github.com/hassant4/cm-redactor-cli.git`

### Run:
To run in the command line:
```
python redact.py "My email is contact@chattermill.io"
=> My email is [redacted]
```
To use as a module:
```
from redact import Redactor
...
redactor = Redactor()
redacted = redactor.apply_rules('My email is contact@chattermill.io')
```

### Credits
Forked from Chattermill
