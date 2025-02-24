tailwind-whatch:
	python manage.py tailwind start

python-start:
	python manage.py runserver

start:
	make -j 2 tailwind-whatch python-start 