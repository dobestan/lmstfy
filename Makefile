# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python lmstfy/manage.py makemigrations multisites search
	python lmstfy/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls lmstfy/ | grep -v -e 'manage.py' | xargs -I{} rm -rf lmstfy/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 lmstfy/
	lmstfy/manage.py test lmstfy/ -v 2
