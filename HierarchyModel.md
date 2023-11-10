# Hierarchy Models

## Zarr Object Model 

The Zarr Object Model (ZOM) is defined in [Zarr Enhancement Proposal (ZEP) 46](https://github.com/zarr-developers/zeps/pull/46).

### python

A ZOM can be created from a zarr store with [`pydantic-zarr`](https://github.com/janelia-cellmap/pydantic-zarr)

### jq

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
