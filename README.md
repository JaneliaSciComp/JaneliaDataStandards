# Janelia Data Standards

## Purpose

The Janelia Data Standards group was formed by bioimaging developers who have encountered specific, practical bioimaging data dilemmas that international community standards don’t yet cover. In particular, Janelia scientists use the [OME-NGFF](https://github.com/ome/ngff) standard as much as possible. Janelia is excited about OME-NGFF, is contributing to it, and is rooting for its success. However, many of Janelia’s developers have encountered situations in which this format is insufficient for their needs, forcing them to either create their own flavor of this format, or use a different format entirely. Ambiguities include working with image tiles that form parts of a whole, high dimensional image data, or large ancillary data sets such as point clouds or ROIs. In such situations, developers must make choices about how to read and write never-before-seen data and metadata structures.

**This website is Janelia’s bioimaging developers’ manifesto.** It is a collection of essays written by developers, for developers, on the advanced technical quandaries they’ve encountered. It records the choices Janelia’s developers have made when encountering exotic data dilemmas, so that other developers encountering similar dilemmas can make consistent choices. 

## Style

The articles in this collection must strike a balance between being too specialized and too generic. On the one hand, contributors are encouraged to remain pragmatic, to describe their use cases, and to share their example data. On the other hand, the articles will necessarily speak to the abstract design principles that drove the developers’ choices. It is not this group’s mission to write a comprehensive textbook on image data design. Nevertheless, **the articles will be vetted, and their conclusions authoritative,** for Janelia’s purposes. Where swift, unambiguous decisions are needed, such decisions will be made, and the rationale behind those decisions will be explained. 

## Contributing

This project aims to develop conventions that Janelians need to do their work, and to disseminate those conventions across Janelia. It is not this group’s goal to create an international standard. However, as this project matures, contributions from the community may be considered. Individuals outside of Janelia who are interested in contributing an article should create a GitHub issue to explore this possibility before investing additional time in it. It is this group’s hope that the rapidly evolving conventions developed here may ultimately, gradually, be considered for incorporation into the OME-NGFF standard as well. 

## Product

This effort is in its infancy. Ultimately, the product is expected to consist of four components:

- Written articles. 
- A cool website that hosts the articles.
- A glossary and/or thesaurus.
- A directory of example data that the public can view and browse.

We appreciate the community’s interest in this social experiment.

