# Запуск проекта
```
docker-compose -f local.yml up --build
```
В файле ./compose/Dockerfile мы запускаем скрипт, устанавливающий несколько версий библиотеки(в качестве примера выбран flask):
```
COPY ./compose/install_lib /install_lib
RUN sed -i 's/\r$//g' /install_lib
RUN chmod +x /install_lib
RUN /install_lib
```
Сам скрипт перебирает все указанные версии библиотеки, тянет их с github

```
LIB_PATH=/custom_folder/flask/

LIB_VERSIONS=1.1.2 2.0.2

for VERSION in 1.1.2 2.0.2
do
  echo LIB VERSION $VERSION
  pip install --target=$LIB_PATH/$VERSION  git+https://github.com/pallets/flask.git@$VERSION
done
```

В файле main.py указываем значение переменной ```LIB_VERSION="2.0.2"```
## После запуска логах должно быть выведено:

```
python_1  | Run main
python_1  | Redis version 3.5.3
python_1  | flask version 2.0.2
v_c_python_1 exited with code 0
```
## Изменяем значение переменной ```LIB_VERSION="1.1.4"``` и билдим контейнер:

```
docker-compose -f local.yml up --build
```

При этом в логах:

```
python_1  | Run main
python_1  | Redis version 3.5.3
python_1  | flask version 1.1.4
v_c_python_1 exited with code 0
```
