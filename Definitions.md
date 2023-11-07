# Definitions

### "array" 
1. An n-dimensional collection of discrete samples whose domain is a regular grid.
2. A node in a hierarchy that contains a data structure of the type described in (1). Array nodes cannot have child nodes.

### "aliasing"

### "downsampling"
The act of resampling an image to a lower resolution, often by an integer factor.

### "field of view"
The physical extent of the domain of an image.

### "filtering"
1. Usually referes to a convolution operation (a local, linear operation on the intensity values of an image).
2. Any operation that modifies the intensity values of an image.

### "group"
A node in a hierarchy that can have child nodes, and can contain metadata, but cannot contain array data.

### "hierarchy"
A collection of groups and arrays, connected in a tree-like structure.

### "image"
an array whose samples are interpreted as measurements over a physical space, with a particular sampling rate, or "resolution".

### "interpolation"
A process that, given an image, produces new samples at points in the domain not on the discrete image grid.

The most common methods for interpolation are "nearest-neighbor", "bi-/tri-/n-linear", "cubic", "windowed sinc".

### "origin"
1. Of an array: the point in the discrete domain with the minimum index (usually zero) for all dimensions.
2. Of an image: the point in the physical domain corresponding to the array origin.

The term "offset" is sometimes used to refer to the "origin".

### "pixel" 
A single sample of a two-dimensional image.

Often used interchangeably with "sample".

Related terms: "sample", "voxel"

### "resampling"
A process that generates a new array representing an image at a new resolution. 

The new resolution is often an integer multiple of the original image resolution, but need not be. Resampling methods often
consist of filtering and interpolation steps.

Related terms: "downsampling", "resolution"

### "resolution"
the physical (often spatial) sampling rate of an image. 

A high resolution image will comprise of more samples for the same field of view compared to a low resolution image.

The terms: "spacing", "pixel spacing", "pixel resolution" are commonly used to refer to "resolution".

### "sample" 
A single element of an array or image, located at a particular point in the domain, and
have a single value (intensity).

### "voxel" 
A single sample of a three-dimensional image.

