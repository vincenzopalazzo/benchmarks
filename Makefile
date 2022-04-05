default: vfmt v

v:
	cd vlang; v -prod -cc g++ main.v && ./main --benchmark_out=result_prod.json --benchmark_out_format=json
	cd vlang; v -cc g++ main.v && ./main --benchmark_out=result_deb.json --benchmark_out_format=json

vfmt: 
	v fmt -w .

vdep:
	v install --git https://github.com/vincenzopalazzo/vbenchmark.git