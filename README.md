# DJANGO Application Template

### Settings in the environment
- python **v3.10.5** (_recommended version_)
- django **v4.0.6** (_python module_)
- watchdog **v2.1.9** (_python module_)
- transliterate **v1.10.2** (_python module_)

### Copying a repository

```sh
git clone git@github.com:SeRj-ThuramS/template-django-application.git
```

### Creating a virtual environment
_Remember that for each OS you need to create a separate environment_

```sh
python -m venv venv_{win64|win32|linux}
```

### Login to windows environment

```sh
.\venv_{win64|win32}\Scripts\activate
```

### Login to linux environment

```sh
source venv_linux/bin/activate
```

### Installing required packages

```sh
pip install django==4.0.6 watchdog==2.1.9 transliterate==1.10.2
```

### PIP Update

```sh
python -m pip install --upgrade pip
```
### Leaving the environment

```sh
deactivate
```

### Launch project for development

```sh
python main.py --name name_project --migrate models --debug ...
```

### Keys to run the application
> --name <name_project> - the name of the project is given. This is a required parameter
>
> --migrate <models> - run the migration of DJANGO models to the database. The folder with DJANGO models is specified. Example --migrate models, --migrate src.models
>
> --debug - run in development mode. This mode ensures that the application is restarted after saving changes in the project files. It is not recommended to use this mode for release applications.
>
> ... - means that you can specify your options like "--src script --src1 script ...". (--src, --src1) - path to the package. (script, script1) - executable module
