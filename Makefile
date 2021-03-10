all: random-sqs random-sqs.service
.PHONY: all random-sqs install uninstall
lib_dir=/usr/local/lib/random-sqs
conf_dir=/usr/local/etc/random-sqs
service_dir=/etc/systemd/system
venv=$(lib_dir)/venv

install: $(service_dir) random-sqs.service
	@echo Installing the service files...
	cp random-sqs.service $(service_dir)
	chown root:root $(service_dir)/random-sqs.service
	chmod 644 $(service_dir)/random-sqs.service

	@echo Installing library files...
	mkdir -p $(lib_dir)
	cp random-sqs.py $(lib_dir)
	chown root:root $(lib_dir)/*
	chmod 644 $(lib_dir)/*

	@echo Installing configuration files...
	mkdir -p $(conf_dir)
	cp random-sqs.env $(conf_dir)
	chown root:root $(conf_dir)/*
	chmod 644 $(conf_dir)/*

	@echo Creating python virtual environment and isntalling packages...
	python3 -m venv $(venv)
	$(venv)/bin/pip3 install -r requirements.txt

	@echo Installation complete...
	@echo run 'systemctl start random-sqs' to start service
	@echo run 'systemctl status random-sqs' to view status

uninstall:
	-systemctl stop random-sqs
	-systemctl disable random-sqs
	-rm -r $(lib_dir)
	-rm -r $(conf_dir)
	-rm -r $(service_dir)/random-sqs.service