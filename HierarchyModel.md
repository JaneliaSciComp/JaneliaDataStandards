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

Let's say we have an imaginary chunked file format specifically intended for a particular application.
Restrictions:
* The top level of the hierarchy (right after the root) can only be groups, and the groups must either be named c0, c1, etc., or s0, s1, etc.
* Within the s0, s1, etc. groups, arrays must be 1D to 4D.
* Within the s0, s1, etc. groups, the number of files must be equal to the number of chunks specified in the array metadata.
* The application accepts both Zarr and n5 files.

TODO: Decide on modeling approach and start creating schemas.
Separate validation of the zarr/n5 part from validation of the more specific application requirements?