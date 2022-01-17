# Запуск проекта
```
docker-compose -f ./v_c/local.yml up --build
```
В файле ./compose/Dockerfile мы устанавливаем несколько версий библиотеки (в качестве примера выбран flask):
```
RUN pip install --target=/custom_folder/flask/1.1.4 flask==1.1.4
RUN pip install --target=/custom_folder/flask/2.0.2 flask==2.0.2
```
В файле main.py указываем значение переменной ```LIB_VERSION="2.0.2"```
## После запуска  логах должно быть выведено:

```
python_1  | Run main
python_1  | Pillow version 3.5.3
python_1  | flask version 2.0.2
v_c_python_1 exited with code 0
```
## Изменяем начение переменной ```LIB_VERSION="1.1.4"``` и билдим контейнер:

```
docker-compose -f ./v_c/local.yml up --build
```

При этом в логах:

```
python_1  | Run main
python_1  | Pillow version 3.5.3
python_1  | flask version 1.1.4
v_c_python_1 exited with code 0
```

