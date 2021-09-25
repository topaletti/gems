local-settings:
	cp settings/local.py gems/settings.py

local-migrate: local-settings
	python3 manage.py makemigrations
	python3 manage.py migrate

remote-settings:
	cp settings/remote.py gems/settings.py
