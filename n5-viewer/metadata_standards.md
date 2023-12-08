# n5 metadata definitions

- [dataType](#dataType)
- [compression](#compression)
- [blockSize](#blockSize)
- [dimensions](#dimensions)
- [pixelResolution](#pixelResolution)
- [resolution](#resolution)
- [downsamplingFactors](#downsamplingFactors)
- [offset](#offset)

### dataType
A string specifying the data type of the data in the array, which in turn specifies all the possible values for a given datum. This field is required, and must be one of the following: 
"uint8"
"uint16"
"uint32"
"uint64"
"int8"
"int16"
"int32"
"int64"
"float32"
"float64"
"string"
"object"

### compression
A JSON object identifying the primary compression method and providing configuration parameters. This property is required, and cannot be empty. The “compression” object must contain the “type” property. Multiple compressors are not allowed. “type” must be one of the following:

1. “blosc”: If the type is “blosc”, then the “compression” object must also contain the properties “clevel”, “blocksize”, “cname”, “nthreads”, and “shuffle”. Note that the “s” in blocksize is lower case.
2. “bzip2”: If the type is “bzip2”, then the “compression” object must also contain the property “blockSize”. 
3. “gzip”: If the type is gzip, the compression object must also contain the properties “useZlib” and “level”.
    1. “useZlib” indicates whether or not Zlib was used. 
    2. “level” indicates the level of compression on a scale of 1 to 9, including -1, where 1 is the least compressed, 9 is the most compressed, and -1 indicates the default compression level.
4. “lz4”: If the type is “lz4”, then the “compression” object must also contain the property “blockSize”.
5. “raw”: If the type is “raw”, this indicates no compression was used. Any additional properties in the “compression” object will be ignored.
6. “xz”: If the type is “bzip2”, then the “compression” object must also contain the property “preset”.

### blockSize
A list of integers defining the length of each dimension of a chunk of the array. (n5 assumes the chunks are on a regular grid.) This array must be the same length as “dimensions”. This field is required.

### dimensions
An array of integers indicating the total length of each dimension of the array. Length must be from 1 to 4, inclusive. This field is required. The order of dimensions must be xyzt (or xyz, xyt, or xy). Dimension order is assumed by the software and not expressed in the metadata, so a metadata document with incorrect dimension order will pass schema validation. Channel is expressed in the hierarchy structure, not the dimensions, with folders for each channel e.g. c0/, c1/.

### pixelResolution
A JSON object with exactly two properties:
1. "unit": The spatial units of the sampling interval. This field is required but can be any string.
2. "dimensions": The spatial sampling intervals for each dimension of the image. 

### resolution
A JSON array of the spatial sampling intervals for each dimension of the image. Used in the bigcat format. Neither allows nor assumes units.

### downsamplingFactors
A JSON array indicating the integer factor by which spatial resolution for each dimension was uniformly decreased, relative to the original image. Presumably, this happened in one of two ways: 

1. Naive downsampling, in which data are uniformly discarded. For example, downsamplingFactors of 4 means every fourth sample was discarded along a particular dimension. 
2. Average downsampling, in which subsets of samples are averaged to produce a new, smaller array. For example, downsamplingFactors of 4 means every four samples were averaged to produce a new sample. If dimensions are downsampled evenly, total number of samples is reduced by a factor of N^4, where N is the number of dimensions.   

s0/ should have downsamplingFactors of 1 (e.g. [1,1] for a 2-dimensional image), but this is not enforced by the schema. This array must be the same length as blockSize, dimensions, and resolution/pixelResolution. This field is NOT required. If it is present at some levels of the hierarchy, it should be present in all, but this is not currently enforced by the schema.

### offset
A JSON array indicating, loosely speaking, the extent of translation relative to the original image. More precisely, it indicates the new location of the origin. (Note that here 'origin' refers to the sample that was at (0,0) in the original image). In general, this can be arbitrary or physical units, but in bigcat it is always physical and in n5 it is typically physical. This field is NOT required. If it is present at some levels of the hierarchy, it should be present in all, but this is not currently enforced by the schema.