VCC=c
PYCC=python3

default: dep fmt v py

dep: vdep pydep

fmt: vfmt pyfmt

v:
	cd vlang; v -prod -cc g++ main.v && ./main --benchmark_out=result_prod.json --benchmark_out_format=json
	cd vlang; v -cc g++ main.v && ./main --benchmark_out=result_deb.json --benchmark_out_format=json

vfmt: 
	v fmt -w .

vdep:
	v install --git https://github.com/vincenzopalazzo/vbenchmark.git

py:
	cd python && $(PYCC) bm.py

pyfmt:
	cd python && poetry run black .

pydep:
	cd python && poetry install

pycheck:
	cd python && poetry run pytest . --log-cli-level=INFO