# Introduction

Articles posted to the Janelia Data Standards website should be vetted, authoritative, well-considered, and of high stylistic and technical quality. For this reason, each new article will undergo a review, using GitHub’s PR and review tooling. This process is intended to help the reviewer refine their ideas.

# Review process

Each new article must be approved by at least two reviewers. Reviewers must complete all *three* sections of the template below. Reviewers are selected by the author. The author may select more than two reviewers, if desired, but only the approval of two reviewers is needed. The review *may* consist of in-line comments, but it *must* include the template. 

Anybody who wishes to give feedback on the PR may do so, and the author is encouraged to consider all feedback thoughtfully, whether it comes from casual commenters or official reviewers. There is no deadline between initial submission of the PR and assignment of reviewers. If the author wishes, they may submit the PR, wait a while, see who comments on it, and then invite the commenters to become reviewers.

There is no rule of thumb on how long the review needs to be. There is also no rule of thumb on how many comments the author must respond to. All that matters is that two reviewers must ultimately approve the article. Reviewers are encouraged to be reasonable and understand that not all of their comments will be heeded. 

Reviewers have **three weeks** to complete their review. After three weeks, it is up to the authors’ discretion whether they wish to give the tardy reviewer more time, or select a new reviewer.

If an article fails to achieve the approval of two reviewers in a reasonable time frame, the PR will be closed. (Who decides this, and how, will be played by ear.) The author may wish to re-submit a modified version of the article. Authors are discouraged from simply re-submitting the same article with more agreeable reviewers. In the event of disagreement on a data standard, the disagreeing parties are encouraged to meet—preferably over food and drink—and have one or more in-person discussions to try and achieve consensus. If consensus is simply impossible, the disagreeing parties should each write an article arguing for their position. The two articles should link to each other on the website, and should respond to each other’s ideas.

---

# Review template

The questions below do not need to be answered line-by-line. Rather, they are meant to convey a general sense of the purpose of that section. It is up to the reviewers to decide how thoroughly they wish to address each section.

## 1. The Big Picture

Is this article appropriate for the Janelia Data Standards project? Is the general premise of the article sound? Is the proposed data standard generalizable beyond that author’s particular use case?

## 2. Technical Choices

Is the proposed standard elegant, straightforward, and focused? Does the author adequately explain the rationale behind the standard? Is the author making any flawed implicit assumptions, either about the problem or about their audience? Does the author provide an implementation and/or example data?

## 3. Writing Style

Is the post readable to bio-imaging developers who may come from a different sub-field, or code in a different language? Does it contain any typos or awkward sentences? Are the ideas organized in a logical flow?

---

Here is a diagram illustrating the review process.

![A sketch of the review process.](review_process_image.png)

---

# Modifying existing articles

Ideas and standards evolve over time, so some articles will need to be modified after publication. The modification history will be noted clearly on the post itself, so that no modification will be silent.

If the author is making a *minor* modification to their own article, they may skip the review process. A minor modification does not change the audience or the use case for the standard, and poses no danger of rendering existing implementations of the standard obsolete.

If the author is making a moderate or significant modification to their own published article, they must submit a new PR, and the PR will undergo the same review process described above.

The line between ‘minor’ and ‘moderate’ modifications will be fuzzy. For example, altering a standard to be more permissive may not pose a danger of rendering existing implementations obsolete, but the author may wish to submit it for review anyway. These judgment calls are up to the author.

Anyone may modify *any* article, even one they didn’t write, subject to the following condition: **any modification—even a minor one—requires the modifier to reach out to the original author.** Beyond that, the procedure then depends on the size of the modification:

- Minor modifications only require a quick assent from the original author. If person A wrote the original article, and person B wishes to make a minor modification, then person B should reach out to person A. If person A replies, ‘go ahead’, then no further review is necessary.
    - If the original author cannot be reached, then minor modifications can be made with no review.
- Moderate or significant modifications require formal review. In these cases, the modifier must make a good-faith effort to invite the original author to be a reviewer. If the original author wants to review, then the new author must select them as a reviewer. If the original author can’t be reached, then the article can be modified without their consent, with the usual review process.

---

# TODO: Implementation in GitHub
