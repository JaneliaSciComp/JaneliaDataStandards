## Arrays, coordinates, and indexes

Zarr stores multi-dimensional arrays into regularly sized chunks.
Chunks are themselves multi-dimensional arrays of a smaller size than
the complete multidimensional array and are stored as a 1D array of
values, called a "flattened" array.

Indexing into a multi-dimensional array is done with an ordered tuple,
each element of which indexes into one of the arrays dimensions.
Elements of this tuple are called "coordinates." For example, the tuple
`(i,j,k)` indexes a three-dimensional array, and `i`, `j`, and `k` are
its coordinates. We will call `i` the left-most index, and `k` the
right-most index (avoiding "first" and "last").

The only valid cordinates for arrays are the non-negative integers.

The following will describe conventions for mapping multi-dimensional
indexes (tuples of integers) to the scalar integer index of the
flattened 1D array.

### Reshaping and stride

One can think of reshaping a 1D are a recursive process of 
grouping a number of adjacent elements

A 1D array is reshaped to an n-dimensional array by grouping a number
adjacent elements belonging to the same dimension. 

* **Define:** the "size" of a dimension is the number of grouped elements.

The stride of the next dimension is the size of the previous dimension. 

* **Define:** the stride of a dimension is the (positive) step in the
  flat array that corresponds to the adjacent element (step of one)
  along that dimension.

* **Define:** the "first" dimension is the dimension with a stride of 1.
* **Define:** the "last" dimension is the dimension with the largest stride.

#### example

Suppose we have this flat array:

`0, 1, 2, 3, 4, 5`

and two dimensions having strides 1 and 3.


`(0, 1, 2), (3, 4, 5)`
`[(0, 1, 2), (3, 4, 5)]`


### row- / column- major

The terms row- and column-major derive for the storage of matrices -
often represented as a 2D array of numbers.  Horizontal groupings of
these numbers are called "rows" and vertical groupings are called
"columns." In mathematics, the entries of a matrix $A$ are denoted
$a_{ij}$. Where rows of the matrix are indexed by $i$ the "first", or
"left" index, and columns of the matrix are indexed by $j$, the
"second", or "right" index.

Discussion of row- and column- major depends on first agreeing which
index (left or right) refers to rows vs columns, and for matrices in
mathematics, the left indexs **always** (in this author's experience)
refers to rows.

### C- and F-order

* **Define:** C-order reshapes flat arrays into multiple dimensions such
  that the **rightmost** index has stride 1.
* **Define:** F-order reshapes flat arrays into multiple dimensions such
  that the **leftmost** index has stride 1.

These terms come from conventions for storing arrays in the C and
Fortran programming languages.
