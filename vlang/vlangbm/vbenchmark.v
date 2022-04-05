/// prepare the v benchmark
module vlangbm

import benchmark
import bm_datatype

// benchmark related to the BST datatype

pub fn bm_empty_bst() {
	mut bmark := benchmark.new_benchmark()
	_ := bm_datatype.create_bst<int>()
	bmark.stop()
	print(bmark.total_message('int empty bst: '))
}

pub fn bm_insert_into_bst() {
	mut bmark := benchmark.new_benchmark()
	mut vect := []int{}
	for i in 0 .. 1000 {
		vect << i
	}
	_ := bm_datatype.insert_into_bst<int>(vect)
	bmark.stop()

	print(bmark.total_message('insert into bst: '))
}
