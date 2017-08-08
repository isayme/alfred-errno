.PHONY: dist install clean

VERSION := 0.1.0

dist:
	make clean
	zip errno-${VERSION}.alfredworkflow README.md LICENSE errno.py icon.png info.plist warn.png

install:
	open errno-${VERSION}.alfredworkflow

clean:
	rm -rf *.alfredworkflow
