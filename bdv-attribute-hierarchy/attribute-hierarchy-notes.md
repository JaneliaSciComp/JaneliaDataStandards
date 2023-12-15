Notes and ideas from meeting on 15 Dec 2023 with Stephan Preibisch, Konrad Rokicki, and John Bogovic.

## Array Data

Array data MUST be stored as OME-Zarr and MAY contain channels and time axes. 

* If channels are stored in zarr arrays, then every array MUST:
    * contain the same number of channels
    * contain channels in the same order

* If time are stored in zarr arrays, then every array MUST:
    * contain the same number of time points
    * contain times in the same order

## Metadata

The top level zarr group contains metadata that describes

* What attributes are present in the zarr store
* Whether attributes are stored in the directory hierarchy as a group or
  as part of a zarr array

### Axes

Axes metadata (inherited from OME-Zarr) enumerate all the attributes in
the hierarchy and image axes, and describes whether they are stored as
part of the hierarchy of groups or as part of an array, and orders those
attributes in the hierarchy.

We add a `storage` field to objects in the `axes` array that may take
one of two values `"group"` or `"array"` which indicate that the axis or
attribute is stored as part of the group hierarchy or as part of an
array, respectively.

Axes with `type: space` MUST also have `storage: array`.

For example:

```json
"axes: [
    { "name": "i", "type": "tile", "storage": "group" },
    { "name": "a", "type": "angle", "storage": "group" },
    { "name": "c", "type": "channel", "storage": "array" },
    { "name": "t", "type": "time", "storage": "array" },
    { "name": "z", "type": "space", "storage": "array" },
    { "name": "y", "type": "space", "storage": "array" },
    { "name": "x", "type": "space", "storage": "array" }
]
```

The `tile` and `angle` attributes are stored as part of the zarr
hierarchy, while channel and time dimensions are stored 


### Attribute hierarchy

The `hierarchy` metadata describes the child groups that are present /
missing. 

The `attributes` metadata stores a an array of objects. 

Each object MUST:

* contain the field `name` that MUST correspond to the `name` of one of the `axes`. 
* contain the field `objects` whose value MUST be an array. The array
  MAY be empty

Each entry in the `objects` array MUST be an object and MUST:

* contain the field `id` whose value MUST be a string 
* contain the field `metadata` whose value MUST be an object 

The `missing` metadata stores an array of objects that encode elements
of the hierarchy that may not exist.


```json
"hierarchy" : {
    "attributes": [
        {
            "name": "i",
            "type: "tile",
            "objects": [
                {
                    "id": "0",
                    "metadata": { <custom metadata> }
                },
                {
                    "id": "1",
                    "metadata": { <custom metadata> }
                }
            ]
        },
        {
            "name": "a",
            "type: "angle",
            "objects": [
                {
                    "id": "00",
                    "metadata": { <custom metadata> }
                },
                {
                    "id": "01",
                    "metadata": { <custom metadata> }
                }
            ]
        }
    ],
    "missing" : [
        { "tile": "1", "angle": "00" }
    ]
}
```

Every combination of attribute name MUST be present in the hierarchy
except those attribute-ids listed in the `missing` array. 

In this example, the hierarchy could look like this:

```
root.zarr
  │
  ├── i0
  │   ├── a00
  │   └── a01
  │
  └── i1
      └── a01

```

