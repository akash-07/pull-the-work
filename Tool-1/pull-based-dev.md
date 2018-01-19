# Some Conclusions

*One can skip directly to research questions summarized below*

- Two main things that integrators are concerned about are as: (1) Quality and (2) Prioritization

- Criteria for judging the contribution: Developers previous actions

- No empirical evidence on whether the developer's previous actions play a significant role in the contribution assessment in the context of pull based development.
(Suggested just opposite)

- Other *Social* signal: Developer's coding activity and social actions (following other developers) to decide the impression of incoming contribution.

- Pull request for two things: (1) Bug fixes and (2) Refactoring. They said that larger projects receive PR's almost daily for bug fixes and almost weekly for Refactoring so prioritizing PR's is an important tasks integrators need to perform.

- Use of inline code comments for code review =  75%
- Use of commit comments for code review = 8% (by integrators)
- Delegating code review using @ tags when the integrator is unaware of the content of PR, delegation also done by video conferencing in some cases
- Atleast 2 core developers should review the code on all PR's
- Code review done by code review tools in some cases
- PR can only be merged by a core team member
- Mostly web interface is used for merging PR

**How do integrators use PR based development mechanism in their projects?**

*Ans.* They use pull based model to:
1. accommodate code reviews
2. discuss new features
3. solicit external contributions

(solicit - ask for)

**How do integrators decide whether to accept a contribution?**

- Source code quality and quality of incoming code, documentation and granularity
(At higher level they also examine quality of commit set and whether it adheres to the project conventions)

- Project fit: Being inline with goals and targets of the project
- Technical fit: Being inline with Technical design of the project
- Importance of fix feature w.r.t to priorities of the project (*"If it fixes a serious bug with minimal changes, it's more likely to be accepted"*)
- Existence of testing code in the PR is preferred (Also manual testing is done if automatic testing doesn't build confidence)
- Track record of contributor is considered last (No such thing as more preference to team member or developer involved in the project)

**Reasons for rejection?**

- Main three -
  - Lack of technical Quality
  - Failed testing
  - Not inline with project conventions

- Less important but new -
  - Unresponsiveness of the submitter

Some discussion on time to make a decision is not summarized here.   

**What factors do the integrators use to examine the quality of contributions?**

- Conformance against project's current style and architecture. Many integrators also examine conformance against programming language idioms. (contributor's code should cause minor friction with existing code)
- Understandable and elegant source code, good documentation and provides clear added value to the project with minimal impact
- Characteristics of the PR: how the PR has been phrased shows how much time and thought has the submitter put in
- Commit organization of the PR (one commit message for each problem)
- Test cases along with PR are preferred (also required is proof of the fact that performance is not affected by proposed change)
- Lastly, social signals for building mental trust. Track record of the contributor.
- Tools for quality evaluation: Continuous integration tools are used in vast majority (75%). Less use of advanced and purpose specific tools like static analysis tools.

**How do the integrators prioritize the application of the contributions?**

- Urgency of the contribution. Criticality of fix is assessed using whether:
  - the contribution fixes a security issue
  - the contribution fixes a serious bug
  - the contribution fixes a bug that the project depends upon
  - number of issued blocked by the unsolved bug

- When the contribution is for addition of new feature, following things are assessed:
  - whether it implements a customer requested feature?
  - whether that feature is required for development of other features?

- Bug fixing contributions preferred over feature addition
- First in first out policy used
- Less complex PR's preferred (Small patches)
- Contributor's track record considered important (somewhat also considered is contributor's origin i.e whether he belongs to core team)   

**Key challenged faced by integrators working with pull based development.**

Technical -
- Asking contributors to keep volume of PR low (one PR for each feature added would be better: *Feature isolation*)
- Experience of the contributor (sends PR but doesn't know git)
- Adherence to project architecture. Integrators might expect the contributor to make some additional changes such that the code adheres to the project architecture and generalize things but asking them to do so is not straightforward.

Social -
- Rejecting PR and telling people what is wrong without hurting them
- Motivating contributors to keep working on the project

**Possible tools stated in the paper**

- An open question is how to efficiently automate the quality
evaluation for pull requests. While tools that automate the
evaluation of many tasks that the developers do to determine
quality (e.g. code style analyzers, test coverage, metrics for software quality, impact analysis etc) do exist, we have seen that developers go little beyond testing and continuous integration. To solve this issue, one could envisage a pluggable platform that, given a pull request update, runs a suite of tools and automatically updates the pull request with a configurable quality score. For the platform to be useful, it will have to automatically learn from and adapt to project-specific behaviors.

- In large projects, integrators cannot keep up with the volume of incoming contributions. A potential solution could be a recommendation system that provides hints on which contributions need the integrator’s immediate attention. Existing work on assisted bug triaging is not directly applicable to the pull-based model, as a pull request is not necessarily as static as a bug report. Researchers might need to come up with different methods of work prioritization that take into account the liveness and asynchrony of the pull-request model. Our analysis of how developers prioritize contribution is a first step in this direction.

**What data do I need from github?**

- Some way to figure out the code quality, documentation of code written by submitter and check to check whether it adheres to project's architecture
- check whether the code is inline with goals of the project
- check whether the code is inline with technical design of the project

(looks) Feasible:
- Importance of fix feature w.r.t other features, prioritizing bug fixes over new feature addition
- checking for existence of testing code within PR
- track record of contributor
- how the issue message has been phrased and commit set has been phrased
- Size of impact
