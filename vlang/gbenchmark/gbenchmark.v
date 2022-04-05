// wrapping module for google benchmark
module gbenchmark

import bm_datatype

fn bm_empty_bst() {
	_ := bm_datatype.create_bst<int>()
}

// FIXME: add inside the wrapper the method to stop and start the timer
fn bm_insert_into_bst() {
	mut vect := []int{}
	for i in 0 .. 1000 {
		vect << i
	}

	_ := bm_datatype.insert_into_bst<int>(vect)
}
