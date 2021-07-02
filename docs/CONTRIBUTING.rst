***********************
Contribution Guidelines
***********************

.. contents:: **Table of Contents**
    :depth: 2

Code Pipeline
=============

Feature branch -> develop <-> Release branch

Code Gateways
=============

Feature branch -> develop
-------------------------

- Must pass PR code review.
   - Suggestions to self check AND code reviewer(s):
      1. Check out locally, export of test cases works
      2. Check out locally, tests pass and results are published into TestRail
- Notes:
   1. YOU MUST SQUASH YOUR CODE ON MERGE TO DEVELOP
   2. The PR MUST contain updates to the CHANGELOG.rst
       - `Added` / `Changed` / `Removed`: Summarize what changed and what kind of semver update it needs (patch, minor, major)
          - patch: fixes a bug without introducing any new functionality, documentation updates, non-code updates
          - minor: introduces a new feature WITHOUT breaking existing functionality
             - e.g.:
                - Creating a new component
                - Adding new css vars, props, and/or slots (that doesn't break existing functionality)
       - major: introduces a new feature or modifies an existing feature that BREAKS existing functionality
          - e.g.:
             - Changing css vars (variable name and/or default values)
             - Changing component props (variable name and/or default values)
             - Changing how slots are handled (if it doesn't default to the existing way)
             - Changing component names
       - MIGRATION STEPS - if there was a breaking change, summarize what an implementing project needs to do

develop -> Release Branch
-------------------------

- Must pass PR code review.
   - Suggestions to self check AND code reviewer(s):
      1. CHANGELOG.rst file is updated
      2. Check out locally, new functionality works

Semantic Versioning
===================

When doing a component release, figuring out what version number you should update can be tricky. Use this guide to help
you decide what version number to update. If you're in doubt, please feel free to ask the channel,
refer to https://semver.org/ for more context, and visit `this helpful guide`_ from the Morningstar design system.

Patch Version (0.0.1)
---------------------

    PATCH version when you make backwards compatible bug fixes.

Update the patch version when you've made a backwards compatible bugfix or security update to the library.
Patch versions should *not* include any visual changes (size/shape/font/color/etc).

**Examples**

-  The ``installation`` is failing on certain Python versions

-  A Dependent package had a security issue, and you've updated this package. Doing so has not broken any functionality.

Minor version (0.1.0)
---------------------

    MINOR version when you add functionality in a backwards compatible
    manner

Update the Minor version when some functionality has been added, but it is backwards-compatible.

**Examples**

-  You've added a new predefined test step to the library.

-  You have removed a property from a function, but that property was
   never used for anything.

Major Version (1.0.0)
---------------------

    MAJOR version when you make incompatible API changes

This is basically when the first two cases do not apply, and you'll break consumers if you push this update.
We're potentially going to make a fair number of breaking changes, so we need to be judicious.

**Examples**

-  You've removed a deprecated function

-  You've added/ removed properties from a function and it has impact on functionality.




.. _Jira: https://jira.pfizer.com/projects/DTG/issues
.. _this helpful guide: https://designsystem.morningstar.com/getting-started/versioning-and-breaking-changes/
