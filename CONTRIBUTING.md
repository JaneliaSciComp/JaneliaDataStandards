# How to contribute

Thanks for considering contributing to Janelia's data standards!

In order to keep things simple, please refrain from forking this repository.
Instead, create a new branch with your changes in this repository and create a pull request against the main branch (or any other suitable branch).
Alternatively, if your changes are small and reasonable, you may commit them to the main branch yourself.
If you don't have edit rights in this repository but would like them, please contact Virginia Scarlett. 

Posts in a format suitable for [quarto](https://quarto.org), such as quarto markdown (.qmd) or a notebook (.ipynb) can be added to /posts/. 
Use the existing posts as a template, at least for the header block. 

The workflow for submitting a PR (should you wish to do so) is as follows: \
Clone the repo > create your feature branch > do some work > do `quarto render` to convert your markdown pages to html > Optionally do `quarto preview` to host the site locally and see it in your browser > `git commit` and `git push` as usual.

Whether or not you are submitting a PR, and whether or not you wish to preview the updates in your browser, please render the site before your final push using `quarto render`. You will need quarto installed. This workflow is described in the [quarto docs for GitHub Pages](https://quarto.org/docs/publishing/github-pages.html) (option #1 of 3).

The rendered site pages are automatically stored in, and deployed from, /docs/ on the main branch, so please do not manually modify that folder.
