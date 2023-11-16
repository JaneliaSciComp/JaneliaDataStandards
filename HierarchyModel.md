# Hierarchy Models

This is a space for brainstorming ideas about how to schematize hierarchical data structures for bioimaging. So far, two modeling frameworks have been proposed. 

## Zarr Object Model 

The Zarr Object Model (ZOM) is defined in [Zarr Enhancement Proposal (ZEP) 46](https://github.com/zarr-developers/zeps/pull/46).

According to this proposal, nodes in a hierarchy can be represented as JSON objects that contain the metadata of the actual nodes we're trying to model. 

### Modeling hierarchies in python

A ZOM can be created from a zarr store with [`pydantic-zarr`](https://github.com/janelia-cellmap/pydantic-zarr)

### Modeling hierarchies in jq

A ZOM can be created from a zarr store using jq with the following:

```bash
#!/bin/bash

root="$1"

zarrMetadataFiles=$(find  $root -type f -name '.zarray' -o -name '.zgroup' -o -name '.zattrs')
jq -n --arg root $root 'include "zarr"; zomAddFiles($root)' $zarrMetadataFiles
```

where the zarr module is defined [here](https://github.com/saalfeldlab/n5-imglib2/blob/master/src/main/resources/zarr.jq).

## N5 Container Tree

N5 Container trees are defined [here](https://github.com/saalfeldlab/n5-ij/wiki/N5-Container-Tree).

## Toy Example (Work in progress!)

Let's say we have an imaginary chunked file format, based on Zarr or n5, specifically formatted for a particular application.

Here is a text description of our rudimentary, imaginary file format:
* The top level of the hierarchy (right after the root) can only be groups, and the groups must be named c0, c1, etc. 
* The second level of the hierarchy can only be 2-dimensional arrays, and the arrays must be named s0, s1, etc.
* Arrays have the following metadata: dataType, dimensions, blockSize, and compression.
	* dataType is a string specifying the data type of the data in the array, which in turn specifies all the possible values for a given datum. This field is required. While it can be anything, some reasonable data types are listed here: https://zarr-specs.readthedocs.io/en/latest/v3/core/v3.0.html#data-types
	* dimensions is a JSON array of integers defining the length of each dimension of the array. This property is required.
	* blockSize is a JSON array of integers defining the length of each dimension of a chunk of the array. This property is required.
	* compression is a JSON object identifying the compression scheme and relevant parameters, or an empty object if no compression was used. The object must contain a `type` key identifying the compression scheme. Common compression types are gzip AND…?. If the type is gzip, the parameters should be “useZlib” and “level”. (UseZlib indicates whether or not Zlib was used. The level indicates the level of compression on a scale of 1 to 9, including -1, where 1 is the least compressed, 9 is the most compressed, and -1 indicates the default compression level. The compression level was specified at the time of compression.) This object is required. Multiple compressors are not allowed.

TODO: Create a JSON Schema for the toy format!
