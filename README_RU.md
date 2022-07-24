# Шаблон приложения на базе DJANGO

### Установки в окружении
- python **v3.10.5** (_рекомендуемая версия_)
- django **v4.0.6** (_модуль python_)
- watchdog **v2.1.9** (_модуль python_)
- transliterate **v1.10.2** (_модуль python_)

### Копирование репозитория

```sh
git clone git@github.com:SeRj-ThuramS/template-django-application.git
```

### Создание виртуального окружения
_Помните, что для каждой ОС нужно создавать отдельное окружение_

```sh
python -m venv venv_{win64|win32|linux}
```

### Вход в окружение windows

```sh
.\venv_{win64|win32}\Scripts\activate
```

### Вход в окружение linux

```sh
source venv_linux/bin/activate
```

### Установка необходимых пакетов

```sh
pip install django==4.0.6 watchdog==2.1.9 transliterate==1.10.2
```

### Обновление PIP

```sh
python -m pip install --upgrade pip
```
### Выход из окружения

```sh
deactivate
```

### Запустить проект для разработки

```sh
python main.py --name name_project --migrate models --debug ...
```

### Ключи для запуска приложения
> --name <name_project> - задается название проекта. Это обязательный параметр
>
> --migrate <models> - запустить миграцию моделей DJANGO в БД. Указывается папка с моделями DJANGO. Пример --migrate models, --migrate src.models
>
> --debug - запустить в режиме разработки. Данный режим обеспечиванет перезапуск приложения после сохранения изменений в файлах проекта. Не рекомендуется использовать данный режим для release приложений
>
> ... - означает, что вы можете указать свои параметры по примеру "--src script --src1 script ...". (--src, --src1) - путь до пакета. (script, script1) - запускаемый модуль
