# Definitions

- ["array"](#array)                                                                                                                                                                                                
- ["downsampling"](#downsampling)
- ["field of view"](#field-of-view)
- ["filtering"](#filtering)
- ["group"](#group)
- ["hierarchy"](#hierarchy)
- ["image"](#image)
- ["interpolation"](#interpolation)
- ["origin"](#origin)
- ["physical"](#physical)
- ["pixel"](#pixel)
- ["resampling"](#resampling)
- ["resolution"](#resolution)
- ["sample"](#sample)
- ["voxel"](#voxel)


### "array" 
1. An n-dimensional collection of discrete samples whose domain is a regular discrete (integer) grid.
2. A node in a hierarchy that contains a data structure of the type described in (1). Array nodes cannot have child nodes.

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
A set of numbers intended to be displayed on a screen. An image is usually represented as an array or array-like data structure, but can also be represented as the set of solutions for a discrete function over a finite domain. Ancillary data structures may be required to display an image or to interpret an image, but these are not part of the image itself. 

### "interpolation"
A process that, given an image, produces new samples at points in the domain not on the discrete image grid.

The most common methods for interpolation are "nearest-neighbor", "bi-/tri-/n-linear", "cubic", "windowed sinc".

### "origin"
1. Of an array: the point in the discrete domain with the minimum index (usually zero) for all dimensions.
2. Of an image: the point in the physical domain corresponding to the array origin.

The term "offset" is sometimes used to refer to the "origin".

### "physical"
Relating to quantities or measurements of the physical world.

Examples:
* sample intensities measured by a physical sensor
    * photon count
    * [Hounsfield unit](https://en.wikipedia.org/wiki/Hounsfield_scale)
* distances / areas / volumes / times measured in images in physical units (um, mm, seconds)
    * "the area of segment A is 12 mm^2"
    * "mitosis begins at time = 3.2s"

Non-examples:
* sample intensities not derived from sensors
    * segmentation id
    * the output of a deep neural network model
* distances / areas / volumes / times described by sample / array indexes
    * "the area of segment B is 85 pixels"
    * "mitosis begins at frame 51"

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
1. The level of detail in an image. A high resolution image will have more samples than a low resolution image for the same field of view.
2. The physical (usually spatial) sampling interval for an image. In other words, the distance between samples. Usually expressed separately for each dimension, e.g. millimeters per pixel in x. (Note: The sampling *interval* is the reciprocal of the sampling *rate*.) 
3. The total number of samples in each dimension of an image. For example, a 2-dimensional image with 1500 pixels along the x dimension and 1000 pixels along the y dimension could be said to have a resolution of 1500 x 1000 (the colloquial convention is to express the dimensions in x, y, z order). 

"Resolution" should be considered synonymous with "spatial resolution" unless otherwise specified (e.g. gray-level resolution, temporal resolution, etc.). 

The terms "spacing", "pixel spacing", and "pixel resolution" are commonly used to refer to "resolution".

### "sample" 
A single element of an array or image, located at a particular point in the domain, and
have a single value (intensity).

### "voxel" 
A single sample of a three-dimensional image.

