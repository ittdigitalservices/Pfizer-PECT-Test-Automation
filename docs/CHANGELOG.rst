*********
Changelog
*********


Description
===========

This Changelog contains changes for each version of this project and adheres to `Semantic Versioning`_ and uses a format is based on `Keep a Changelog`_.

Types of changes include:

-	**Added** for new features.

-	**Changed** for changes in existing functionality.

-	**Deprecated** for soon-to-be removed features.

-	**Removed** for now removed features.

-	**Fixed** for any bug fixes.

2.2 - 2021-04-23 SUPPORTED
--------------------------------

**Added**

- tests-ui Step Definitions and samples.features file with examples.
- Logging Functionality
- Cross Browser functionality
- pytest-logger and  pytest-xdist

**Changed**

- Libraries updated to latest versions
- Small changes in tests-ui overall structure

**Deprecated**

- None

**Removed**

- Due to update on pytest-bdd library there are some breaking changes over the 2.0 code that may need to be addressed
  - "strict_gherkin" is no longer needed. Tests will break if the property is still present on scenarios call
  - For more details please see: https://pytest-bdd.readthedocs.io/en/stable/#migration-from-3-x-x

**Fixed** 

-	All existing issues have been fixed except for: https://github.com/pfizer/python-test-automation-boilerplate/issues

**Known Issues** 

-	Pytest latest version does not support TestRail plugin. The temporary workaround is to downgrade pytest version to 5.4.2

2.1 - 2021-01-27 SUPPORTED
--------------------------------

**Added**

- Predefined steps

**Changed**

- Updated libraries to latest present date versions
- Changed 'tests' folder name to 'tests-ui' folder

**Deprecated**

- None

**Removed**

- Due to update on pytest-bdd library there are some breaking changes over the 2.0 code that may need to be addressed
  - "strict_gherkin" is no longer needed. Tests will break if the property is still present on scenarios call
  - For more details please see: https://pytest-bdd.readthedocs.io/en/stable/#migration-from-3-x-x

**Fixed** 

-	None
  - bugs were not related to the boilerplate but libraries used and got removed by using latest libraries versions

2.0 - 2020-04-21 - NO LONGER SUPPORTED
----------------------------------

**Added**

- Install.sh file added.
- New files in the 'scripts' folder to ensure the install.sh file runs successfully.

**Changed**

- Folder structure changed. 
- Changed version number of Python, which is a prerequisite.

**Deprecated**

- Unknown. 

**Removed**

- Removed drivers including Chromedriver, Firefox and Internet Explorer. 

**Fixed** 

- Unknown. 

2.1-MLR - 2020-11-27 - SUPPORTED
----------------------------------

**Added**

- Templates for the following scenarios
  - new_megamenu_and_cookies.feature
  - new_megamenu_and_no_cookies_no_selfvalidation.feature
  - new_megamenu_and_selfvalidation.feature
  - old_megamenu_and_cookies.feature
  - old_megamenu_and_no_cookies.feature
- Update test steps to support screenshot of entire new megamenu and old megamenu

**Changed**

- Updated libraries to latest present date versions

**Deprecated**

- None

**Removed**

- Due to update on pytest-bdd library there are some breaking changes over the 2.0 code that may need to be addressed
  - "strict_gherkin" is no longer needed. Tests will break if the property is still present on scenarios call
  - For more details please see: https://pytest-bdd.readthedocs.io/en/stable/#migration-from-3-x-x

**Fixed** 

-	None
  - bugs were not related to the boilerplate but libraries used and got removed by using latest libraries versions


.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html
.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0/ 
