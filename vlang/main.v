// Entry point to run the google benchmark over V datatypes
//
// author: https://github.com/vincenzopalazzo
module main

import vbenchmark
import gbenchmark
import vlangbm

fn int() {}

fn main() {
	// FIXME: take the parameter argument to catch
	// what benchmark library the user want use
	println('\n' + '-'.repeat(20) + ' vbenchmark (google benchmark) BM ' + '-'.repeat(20))
	mut exit_code := configure_and_run_google_benchmark()
	if exit_code > 0 {
		exit(exit_code)
	}
	println('\n' + '-'.repeat(20) + ' V BM ' + '-'.repeat(20) + '\n')
	exit_code = configure_and_run_v_benchmark()
	exit(exit_code)
}

fn configure_and_run_v_benchmark() int {
	vlangbm.bm_empty_bst()
	vlangbm.bm_insert_into_bst()
	return 0
}

fn configure_and_run_google_benchmark() int {
	vbenchmark.add_benchmark('init empty BST', gbenchmark.bm_empty_bst)
	vbenchmark.add_benchmark('insert into BST', gbenchmark.bm_insert_into_bst)
	if !vbenchmark.run_benchamars() {
		return 1
	}
	return 0
}
