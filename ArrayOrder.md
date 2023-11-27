## Multi-dimensional array indexing

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

The only valid coordinates for arrays are the non-negative integers.

The following will describe conventions for mapping multi-dimensional
indexes (ordered tuples of integers) to the scalar integer index of the
flattened 1D array.

### Reshaping and stride

One can think of reshaping a 1D as a recursive process of grouping a
number of adjacent elements.

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

and two dimensions having strides 1 and 3, equivalently having dimensions 3 and 2.

`(0, 1, 2), (3, 4, 5)`
`[(0, 1, 2), (3, 4, 5)]`


### C- and F-order

* **Define:** C-order reshapes flat arrays into multiple dimensions such
  that the **rightmost** index has stride 1.
* **Define:** F-order reshapes flat arrays into multiple dimensions such
  that the **leftmost** index has stride 1.

These terms come from conventions for storing arrays in the C and
Fortran programming languages.


### array size

When discussing an array that is stored in C-order, dimension size will
be described using a list if sizes per dimension. For example: `[ 3, 5, 7 ].`
In this example, the left-most dimension has size `3`, the right-most
dimension has size `7`.

As always the *first* dimension will have stride 1. Because we're using
C-order, is the right-most index. As a result, the *second* dimension
will have stride `7`, and the *third* dimension will have stride `7*5 =
35`. 

Consider again an array of size `[ 3, 5, 7 ]`, but using F-order.
Again, the left-most dimension has size `3`, the right-most dimension
has size `7`.

As always the *first* dimension will have stride 1.  However, now using
F-order, the *second* dimension will have stride `3`, and the *third*
dimension will have stride `3*5=15`.

### row- and column-major

Matrices are often represented as a 2D array of numbers.  Horizontal
groupings of these numbers are called "rows" and vertical groupings are
called "columns." In mathematics, the entries of a matrix $A$ are
denoted $a_{ij}$. Where rows of the matrix are indexed by $i$ the
"first", or "left" index, and columns of the matrix are indexed by $j$,
the "second", or "right" index.

* **Universal Matrix Convention**: Left indexes refer to rows,
  right indexes refer to columns.

The terms row- and column-major derive for the storage of matrices.
Defining these terms first depends on first agreeing which index (left
or right) refers to rows vs columns for matrices in mathematics.

* **Define:** Arrays storing matrices in "row-major" give columns stride 1. 
* **Define:** Arrays storing matrices in "column-major" give rows stride 1. 

The names come from the fact that varying the column index changes the
position along a single row

* **Consequence:** Given matrix storage conventions C-order storage is
  equivalent to "row-major".
* **Consequence:** Given matrix storage conventions F-order storage is
  equivalent to "column-major".

#### example

As a result of the *Universal Matrix Convention* the size of a matrix
with `2` rows and `3` columns is `[2, 3]` for both C- and F-orderings.
Consider:

```
          column 0   column 1   column 2
  row 0  [    0          1          2   ]
  row 1  [    3          4          5   ]
```

* The flat C-ordered array will be: `[0, 1, 2, 3, 4, 5]`
* The flat F-ordered array will be: `[0, 3, 1, 4, 2, 5]`

To reiterate, the multi-dimensional indexes for both C- and F-order are:

```
          column 0   column 1   column 2
  row 0  [  (0,0)     (0,1)       (0,2) ]
  row 1  [  (1,0)     (1,1)       (1,2) ]
```

because, the row index is *always* the left-most index.


### image analysis

Most formats for storing image files store data such that the
"horizontal axis" / rows have a smaller stride than the "vertical axis"
/ columns.  (Note: while rows have smaller stride than columns, it is
common for rows NOT to have stride 1, for example when using
"interleaved" color components, the "color" dimension often will have a
stride of 1.)

### cartesian coordinates

In contrast to the matrix row/column index convention, cartesian
coordinates label the horizontal and vertical dimensions `x` and `y`
respectively. Referencing positions in the 2D plane is done using
ordered two-tuples `(x,y)`, where `x` is conventionally the left-index
and `y` is the right-index. Using cartesian coordinates, varying
the left dimensions varies horizontal position, and varying the right
dimension varies the vertical position.

Applications and workflows that make use of image geometry most commonly
use cartesian coordinates.

## Conclusions

If a convention is such that the meaning / interpretation of the index
in a particular position (left / rightmost) is strong, then C- and F-
order will agree on the ordering of an array's dimensions, but will
store the arrays differently when flattened.

If a convention is such that the meaning / interpretation of a
particular stride (fastest / slowest) is strong, then C- and F- order
will dis-agree on the ordering of an array's dimensions, but will store the
arrays the same way when flattened.

### refs

1) [nrrd axis ordering](https://teem.sourceforge.net/nrrd/format.html#general.4)
2) [n5 ordering discussion](https://github.com/saalfeldlab/n5/issues/31)
