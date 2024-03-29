WARLUG_WEBSERVER := root@warszawa.linux.org.pl
WARLUG_WEBSERVER_DEST_DIR := /srv/website

.PHONY: install-deps
install-deps:
	bundle install --path=vendor

.PHONY: build
build: install-deps
	bundle exec jekyll build --future

.PHONY: preview
preview: install-deps
	bundle exec jekyll serve

.PHONY: deploy
deploy: build
	rsync -av _site/ $(WARLUG_WEBSERVER):$(WARLUG_WEBSERVER_DEST_DIR)
