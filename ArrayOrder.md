## Multi-dimensional array indexing

Zarr stores multi-dimensional arrays into regularly sized chunks.
Chunks are themselves multi-dimensional arrays of a (usually) smaller
size than the complete multi-dimensional array and are stored as a 1D
array of values, called a "flattened" array.

Indexing into a multi-dimensional array is done with an ordered tuple,
each element of which indexes into one of the array's dimensions.
Elements of this tuple are called "coordinates." For example, the tuple
`(i,j,k)` indexes a three-dimensional array, and `i`, `j`, and `k` are
its coordinates. We will call `i` the "left" or "first" index, and `k` the
"right" or "last" index.

In this document, we will consider the non-negative integers as the only
valid coordinates for arrays (though this can be different in other
contexts).

The following will describe conventions for mapping multi-dimensional
indexes (ordered tuples of integers) to the scalar integer index of the
flattened 1D array.

### Reshaping and stride

One can think of reshaping a 1D array as a recursive process of grouping a
number of adjacent elements.

An (n-1)-dimensional array is reshaped to an n-dimensional array by
grouping a number adjacent elements belonging to the same dimension. 

* **Define:** the "size" of a dimension is the number of grouped elements.

* **Define:** the stride of a dimension is the (positive) step in the
  flat array that corresponds to the adjacent element along that dimension.

The stride of a dimension is the product of sizes of all previous dimensions. 

* **Define:** the "inner" dimension is the dimension with a stride of 1.
* **Define:** the "outer" dimension is the dimension with the largest stride.

#### examples

Suppose we have this flat array:

`[0, 1, 2, 3, 4, 5]`

and two dimensions having sizes 3 and 2. The first stride is always 1.
The second stride is the previous dimensions' size: 3 in this example. So
our strides are 1 and 3. There is no grouping to be done for a
dimensions of stride one, so the first and only step is to group
elements into groups of 3 (the larger stride):

`[(0, 1, 2), (3, 4, 5)]`

<details>

<summary>a larger example</summary>

Suppose we have this flat array:

`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]`


and three dimensions having sizes 2, 3, and 4. Their strides are 1, 2, and 6
where `2*3 = 6`. There is no grouping to be done for a dimensions of stride 1,
so the first step is to join elements into groups of 2 (the
second stride):

`[(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 23)]`

Next, group elements of the new list (which are themselves groups) into
groups of 3 (the largest stride).

`[((0, 1), (2, 3), (4, 5)), ((6, 7), (8, 9), (10, 11)), ((12, 13), (14, 15), (16, 17)), ((18, 19), (20, 21), (22, 23))]`

Notice:
* The element adjacent to `0` in the inner group is `1`, hence stride `1`.
* The element adjacent to `0` in the intermediate grouping is `2`, hence stride `2`.
* The element adjacent to `0` in the outer grouping is `6`, hence stride `6`.

</details>


### C- and F-order

* **Define:** C-order indexes multi-dimensional arrays such that the **last** index has stride 1.
* **Define:** F-order indexes multi-dimensional arrays such that the **first** index has stride 1.

These terms come from conventions for storing arrays in the C and Fortran programming languages.

C-order is equivalent to "lexicographical order". F-order is equivalent to "co-lexicographical
order".

### array size

The size of a multi-dimensional array is described by a list of sizes per
dimension. For example: `[3, 5, 7].` In this example, the *first*
dimension has size `3`, the *last* dimension has size `7`.

If this array is indexed using C-order, then the last index has stride
`1`. As a result, the middle index will have stride `7`, and the *first*
dimension will have stride `7*5 = 35`. 

Consider again an array of size `[3, 5, 7]`, but using F-order
indexing. Again, the *first* dimension has size `3`, the *last*
dimension has size `7`. Now, however, using F-order, the 
*first* dimension will have stride `1`, the *second* dimension will have
stride `3`, and the *third* dimension will have stride `3*5=15`.

## Interpretation of multi-dimensional arrays

The following sections require adding an interpretation or semantics to
the dimensions of a multi-dimensional array. We'll discuss interpreting
arrays as matrices and images.

### row- and column-major

Matrices are usually represented as a 2D array of numbers. Horizontal
groupings of these numbers are called "rows" and vertical groupings are
called "columns." In mathematics, the entries of a matrix $A$ are
denoted $a_{ij}$. Rows of the matrix are indexed by $i$, the
"first" or "left" index, and columns of the matrix are indexed by $j$,
the "second" or "right" index.

* **Universal Matrix Convention**: Left indexes refer to rows,
  right indexes refer to columns.

The terms row- and column-major derive for the storage of matrices.
Defining these terms first depends on first agreeing which index (left
or right) refers to rows vs columns for matrices in mathematics.

* **Define:** Arrays storing matrices in "row-major" give columns stride 1. 
* **Define:** Arrays storing matrices in "column-major" give rows stride 1. 

The names come from the fact that varying the column index changes the
position along a single row.

* **Consequence:** Given matrix storage conventions, C-order storage is
  equivalent to "row-major".
* **Consequence:** Given matrix storage conventions, F-order storage is
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
coordinates label the horizontal and vertical dimensions `x` and `y`,
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
3) [multi-dimensional arrays in vigra](http://ukoethe.github.io/vigra/doc-release/vigranumpy/index.html#more-on-the-motivation-and-use-of-axistags)
