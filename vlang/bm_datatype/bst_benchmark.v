// Binary Search Tree benchmark
//
// The benchmark include a general overview of the
// data structrure.
//
// author: https://github.com/vincenzopalazzo
module bm_datatype

import datatypes

pub fn create_bst<T>() &datatypes.BSTree<T> {
	return &datatypes.BSTree<T>{}
}

pub fn insert_into_bst<T>(vect []T) &datatypes.BSTree<T> {
	mut bst := datatypes.BSTree<T>{}
	for elem in vect {
		bst.insert(elem)
	}
	return &bst
}
