# programming_formalisms_project_autumn_2025

<!-- markdownlint-disable MD013 --><!-- Badges cannot be split up over lines, hence will break 80 characters per line -->

[![Check code style](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_code_style.yaml/badge.svg?branch=main)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_code_style.yaml)
[![Check links](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_links.yaml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_links.yaml)
[![Check Markdown](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_markdown.yaml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_markdown.yaml)
[![Check package](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_package.yaml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_package.yaml)
[![Check spelling](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_spelling.yaml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/check_spelling.yaml)
[![Measure Codecov](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/measure_code_coverage.yml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/actions/workflows/measure_code_coverage.yml)
[![codecov](https://codecov.io/github/programming-formalisms/programming_formalisms_project_autumn_2025/graph/badge.svg?token=KbSwhVmhn6)](https://codecov.io/github/programming-formalisms/programming_formalisms_project_autumn_2025)

<!-- markdownlint-enable MD013 -->

Learners' project of the Programming Formalisms course of autumn 2024.

## Goal

Do some analysis on data from an Uppsala weather station.

## Internal links

- [`docs/requirements/`](docs/requirements.md): design documents
- [`src/learners/`](src/learners/README.md): place to put code
- [`learners/`](learners/README.md): place to put non-code

## Continuous integration scripts

<!-- markdownlint-disable MD013 --><!-- Tables cannot be split up over lines, hence will break 80 characters per line -->

Filename                                    |Descriptions
--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------
[`mlc_config.json`](mlc_config.json)        |Configuration of the link checker, use `markdown-link-check --config mlc_config.json --quiet docs/**/*.md` to do link checking locally
[`.spellcheck.yml`](.spellcheck.yml)        |Configuration of the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally
[`.wordlist.txt`](.wordlist.txt)            |Whitelisted words for the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally
[`.markdownlint.jsonc`](.markdownlint.jsonc)|Configuration of the Markdown linter, use `markdownlint "**/*.md"` to do markdown linting locally. The name of this file is a default name.
[`.markdownlintignore`](.markdownlintignore)|Files ignored by the Markdown linter, use `markdownlint "**/*.md"` to do markdown linting locally. The name of this file is a default name.

<!-- markdownlint-enable MD013 -->

## External links

- [Programming Formalisms course website](https://uppmax.github.io/programming_formalisms/)

## References

- `[Bergström & Moberg, 2002]` Bergström, Hans, and Anders Moberg.
  "Daily air temperature and pressure series for Uppsala (1722–1998)."
  Climatic change 53.1 (2002): 213-252
  [PDF](https://www.smhi.se/download/18.6ae791dc18fc9e7539e1121c/1717658901728/Bergstr%C3%B6m_Moberg_Uppsala.pdf)
  [Data](https://www.smhi.se/download/18.53cdce23194f389da053a4e/1740398333056/uppsala_tm_1722-2022.zip)
