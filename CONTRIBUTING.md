# How to contribute

Thanks for considering contributing to Janelia's data standards!

In order to keep things simple, please refrain from forking this repository.
Instead, create a new branch with your changes in this repository and create a pull request against the main branch (or any other suitable branch).
Alternatively, if your changes are small and reasonable, you may commit them to the main branch yourself.
If you don't have edit rights in this repository but would like them, please contact Virginia Scarlett. 

Posts in a format suitable for [quarto](https://quarto.org), such as quarto markdown (.qmd) or a notebook (.ipynb) can be added to /posts/. 
Use the existing posts as a template, at least for the header block. Quarto will render these files to html, i.e., build the static site files.

The workflow for submitting a PR (should you wish to do so) is as follows: \
Clone the repo > create your feature branch > do some work > Optionally do `quarto preview` to host the site locally and see it in your browser > `git commit` and `git push` as usual.

To preview the site or build it locally, you will need quarto installed on your computer. Neither of these is strictly necessary, since a GitHub action should render the site files remotely for you. However, I've found that one `quarto publish` or `quarto render` might be necessary after merging a branch into main.

The rendered site pages are automatically stored in, and deployed from, the gh-pages branch, so please do not modify that branch.
