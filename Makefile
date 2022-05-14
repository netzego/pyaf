POETRY		:= $(shell which poetry)
SYS_PYTHON	:= $(shell which python)
VENV		:= $(shell $(POETRY) env list --full-path | cut -d " " -f 1)
PYTHON		:= $(VENV)/bin/python
PYTEST		:= $(VENV)/bin/pytest

$(VENV)/pyvenv.cfg:
	$(POETRY) env use $(SYS_PYTHON)

venv: $(VENV)/pyvenv.cfg

install:
	$(POETRY) install

clean:
	fd --no-ignore --hidden --type d .pytest_cache -x rm -fr {}

distclean: clean
	rm -fr $(VENV)

testfiles:
	make -C testfiles

test:
	$(PYTEST) -v tests/

init: venv install

.PHONY: \
	venv \
	install \
	distclean \
	test \
	init \
	clean \
	testfiles
