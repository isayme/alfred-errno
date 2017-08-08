.PHONY: dist install

dist:
	rm -rf *.alfredworkflow
	zip errno.alfredworkflow README.md LICENSE errno.py icon.png info.plist warn.png

install:
	open errno.alfredworkflow
