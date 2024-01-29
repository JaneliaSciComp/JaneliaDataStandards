# n5 data/metadata notes

Code for the n5 viewer is here: https://github.com/saalfeldlab/n5-viewer
Some documentation on the n5 fiji plugin/API is here: https://github.com/saalfeldlab/n5-ij/wiki

# n5 metadata definitions
#### Required fields (n5 array)
- [dataType](#dataType)
- [compression](#compression)
- [blockSize](#blockSize)
- [dimensions](#dimensions)
#### Optional fields
- [offset](#offset)
#### Conditionally required fields
- [pixelResolution](#pixelResolution)
- [resolution](#resolution)
- [downsamplingFactors](#downsamplingFactors)

___

## Required fields (n5 array)

#### dataType
A string specifying the data type of the data in the array, which in turn specifies all the possible values for a given datum. Must be one of the following: `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `float32`, `float64`, `string`, or `object`. This property is required.

#### compression
A JSON object identifying the compression method and related parameters. The `compression` object must contain the `type` property. `type` must be one of the following six options:
1. `blosc`: If the type is `blosc`, then the `compression` object must also contain the properties `clevel`, `blocksize`, `cname`, `nthreads`, and `shuffle`. The additional `typesize` property is optional.
    * `clevel` is an integer indicating the level of compression on a scale of -1 to 9. 1 is the lowest level of compression, and 9 is the highest. -1 indicates the default compression level. Compression level of 0 (no compression) is not recommended, but is technically permitted by n5 viewer. The user should use `type`:`raw` instead.
    * `blocksize` is a positive integer indicating the size of the 'compression blocks' the memory buffer is divided into (in bytes). A value of 0 indicates that the default size will be used. Note that the 's' in blocksize is lower case.
    * `cname` indicates the internal compression algorithm to be used. Must be one of the following: `lz4`, `lz4hc`, `blosclz`, `zstd`, `snappy`, or `zlib`.
    * `nthreads` is a positive integer greater than or equal to 1, indicating the number of threads to use for compression.
    * `shuffle` is an integer between -1 and 2 (inclusive) indicating the type of shuffling to perform, if any, prior to compression. 0 indicates no shuffling; 1 indicates byte-wise shuffling; 2 indicates bit-wise shuffling. -1 indicates the default procedure.
    * `typesize` is a positive integer indicating the stride in bytes over which shuffling is performed. Required unless `shuffle` is 0, in which case the value is ignored.
2. `bzip2`: If the type is `bzip2`, then the `compression` object must also contain the property `blockSize`. 
    * See above definition of `blocksize`. Note that for `bzip2`, `blockSize` has a capital 'S'.
3. `gzip`: If the type is gzip, then the compression object must also contain the properties `useZlib` and `level`.
    * `useZlib` indicates whether or not Zlib was used. 
    * `level` is equivalent to `clevel`, above.
4. `lz4`: If the type is `lz4`, then the `compression` object must also contain the property `blockSize`.
    * See above definition of `blocksize`. Note that for `lz4`, `blockSize` has a capital 'S'.
5. `raw`: If the type is `raw`, this indicates no compression was or should be used.
6. `xz`: If the type is `bzip2`, then the `compression` object must also contain the property `preset`.
    * `preset` is an integer indicating the level of compression on a scale of -0 to -9. -0 is the lowest level of compression, and -9 is the highest. TODO: How to allow -0 in JSON Schema???

Multiple compressors are not allowed. This property is required. 

#### blockSize
A JSON array of positive integers indicating the length of each dimension of a chunk of the array. (Assumes the chunks are on a regular grid.) Must contain at least one item and cannot contain more than 4. This array must be the same length as `dimensions`, `pixelResolution`/`resolution`, `offset` (if present) and `downsamplingFactors` (if present), though this is not currently enforced by the schema. This property is required.

#### dimensions
A JSON array of positive integers indicating the length of each dimension of the whole array. Must contain at least one item and cannot contain more than 4. This property is required.

A couple of requirements are not currently enforced by the schema:
1. The order of dimensions must be xyzt (or xyz, xyt, or xy). Dimension order is assumed by the software and is not expressed anywhere in the metadata, so a metadata document with incorrect dimension order will pass schema validation. 
2. Channel is expressed in the hierarchy structure, not the metadata. Folders for each channel must be named e.g. c0/, c1/. 

## Optional fields

#### offset
A JSON array indicating, loosely speaking, the extent of translation relative to the original image. More precisely, it indicates the new location of the origin. (Note that here 'origin' refers to the sample that was at (0,0) in the original image.) In general, this can be in arbitrary or physical units, but in bigcat they are always presumed to be physical. The three above requirements for `downsamplingFactors` that are not currently enforced by the schema also apply to `offset`, except that in the first point above, s0/ should have `offset`s of 0. This property appears in the bigcat format but not the n5 format. This property is optional. 

## Conditionally required fields

#### pixelResolution
This property is only valid for the n5-viewer format. For the bigcat format, use `resolution`. 

`pixelResolution` is a JSON object with exactly two properties:
1. `unit`: The units of the spatial sampling interval. Can be any string. This property is required.
2. `dimensions`: A JSON array containing the spatial sampling intervals for each dimension of the image. Can be any positive integer or float, including 0. Must contain at least one item and cannot contain more than 4. This property is required.

This property is required, except in the following case: if a multiscale image has `pixelResolution` for s0, and the other levels have downsamplingFactors, then `pixelResolution` is not required for any of the other levels.

#### resolution
This property is only valid for the bigcat format. For the n5-viewer format, use `pixelResolution`. 

`resolution` is a JSON array containing the spatial sampling intervals for each dimension of the image. Can be any positive integer or float, or 0. Must contain at least one item and cannot contain more than 4. Neither allows nor assumes units. 

This property is required, except in the following case: if a multiscale image has resolution for s0, and the other levels have downsamplingFactors, then `resolution` is not required for any of the other levels.

#### downsamplingFactors
A JSON array indicating the integer factor by which spatial resolution for each dimension was uniformly decreased, relative to the original image. Presumably, this happened in one of two ways: 
1. Naive downsampling, in which data are uniformly discarded. For example, downsamplingFactors of 4 means every fourth sample was discarded along a particular dimension. 
2. Average downsampling, in which subsets of samples are averaged to produce a new, smaller array. For example, downsamplingFactors of 4 means every four samples were averaged to produce a new sample. If dimensions are downsampled evenly, the total number of samples is reduced by a factor of N^M, where N is the number of dimensions and M is the downsampling factor.   

Items in the JSON array can be any positive integer or float, including 0. Must contain at least one item and cannot contain more than 4. 

A few requirements are not (currently) enforced by the schema:
1. s0/ of a multiscale image should not contain `downsamplingFactors`. (This is not enforced by the software, but is recommended practice.)
2. This array must be the same length as blockSize, dimensions, and resolution/pixelResolution.
3. If `downsamplingFactors` is present at *some* scale levels of a multiscale image except s0/, it should be present in *all* scale levels of that image except s0/.