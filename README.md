<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- Centered title section with descriptive lines -->
<div align="center">
  <!-- Badges -->
  <p>
    <a href="www.linkedin.com/in/lubrano-alexander">
      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin" alt="linkedin link" />
    </a>
    <a href="https://lubranoa.github.io">
      <img src="https://img.shields.io/badge/Personal_Site-47b51b?style=for-the-badge" alt="personal website link" />
    </a>
    <a href="https://github.com/lubranoa">
      <img src="https://img.shields.io/badge/GitHub-8A2BE2?style=for-the-badge&logo=github" alt="github profile link" />
    </a>
  </p>
  <br />
  <!-- Titles and Subtitles -->
  <h1 align="center">CI/CD Group Project</h1>
  <p align="center">
    <b>Subtitle that's a short description</b>
  </p>
  <p align="center">
    Winter 2023 · <a href="https://ecampus.oregonstate.edu/soc/ecatalog/ecoursedetail.htm?subject=CS&coursenumber=362&termcode=ALL">CS 362 Software Engineering II</a> · Oregon State University
  </p>
  <br />
</div>

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
    
  - [Project Description](#project-description)
  - [Technologies Used](#technologies-and-frameworks-used)
  - [Features](#features)
  - [Usage](#usage)
  - [Skills Applied](#skills-applied)
  - [Acknowledgments](#acknowledgements)

</details>

<!-- Project Description -->
## Project Description

This project focused on the setting up of a Continuous Integration (CI) workflow for the team to develop and test several functions within a shared codespace. The first goal was to set up a shared private GitHub repository following specific guidelines and configuring a CI pipeline for the repository using GitHub Actions. The second goal was to implement three functions in a Python file using the CI workflow, code reviews, and a variety of testing techniques, like Unit Testing and Test Driven Development (TDD), to verify implementation of the software.

Each teammate picked one of three functions to work on. The one I chose to implement was an endian conversion function that converts an integer to its hexadecimal representation in little or big endian. This function was implemented using a test suite of Test Driven Development cases, our CI workflow, and peer code reviews. Again, the focus of this project is not on the functions themselves, but on the CI and testing done to produce the functions.

**Note**: This is a fork of our group's repo, which can be found [here][main-repo-url].

<!-- Technologies Used -->
## Technologies and Frameworks Used

   - [![python][python]][python-url]
   - [![github-wf][github-wf]][github-wf-url]
   - [![unittest][unittest]][unittest-url]
   - [![tdd][tdd]][tdd-url]

<!-- Features -->
## Features
   
  Because this program is an exercise in Continuous Integration and testing, it does not have the features of a program that can be run to solve a problem or do something for you. Here are some "*features*" of this project.

  - Implements a GitHub Workflow for CI in a shared repository
  - CI workflow triggers on pushes and pull requests to the repo
  - CI workflow runs tests and protects the main branch from errant code
  - Contains three functions that accomplish different tasks
  - Contains a test suite for testing these three functions
  - Development of the test suite involved varied testing techniques
  - My function, `conv_endian`, was developed using TDD

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->
## Usage

Seeing as this is not a program used to accomplish something, this section will focus more on the usage of the CI workflow in `python-app.yml` and the development of my testing section of `test.py` and my function in `task.py`.

#### GitHub CI Workflow

This [workflow](/.github/workflows/python-app.yml) does a few major things:
  1) Runs when pushes or pull requests trigger it.
  2) Sets up Python on an Ubuntu virtual machine.
  3) Installs any dependencies in the `.yml` file and in a `requirements.txt` file if present (if not, it's skipped).
  4) Lints any Python files for issues.
  5) Runs the test suite named `tests.py`.

The main goal of this CI workflow is to protect the main branch of the repository from errant or broken code. It accomplishes this in multiple ways:
  - Checks the code for syntax issues and errors. Any issues with the code must be fixed before creating a pull request.
  - Requires a pull request before merging a branch to the main branch.
  - Requires at least one approval from a repo collaborator.
  - Does not allow bypassing of the above settings.

If curious, the main repo's workflow history can be found in its [Actions tab][repo-actions-url].

#### Function Development

The project specifications stated that the function `conv_endian` must convert integers to a hexadecimal number split into two-character bytes in either little or big endian byte orders, depending on what was specified when calling the function. My approach to solving this problem was to develop it using Test Driven Development (TDD). 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Skills Applied -->
## Skills Applied

  - skill 1
  - skill 2

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

Alexander Lubrano - [lubrano.alexander@gmail.com][email] - [LinkedIn][linkedin-url]

Project Link: [https://github.com/lubranoa/CS362-Portfolio-Project][repo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Acknowledgements -->
## Acknowledgments

  - [Shields.io][shields-url]
  - [Simple Icons][icons-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Markdown links -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffd343
[python-url]: https://www.python.org/

[github-wf]: https://img.shields.io/badge/GitHub_Workflows-2088FF?style=for-the-badge&logo=githubactions&logoColor=white
[github-wf-url]: https://docs.github.com/en/actions/using-workflows

[unittest]: https://img.shields.io/badge/Python_unittest-3776AB?style=for-the-badge&logo=python&logoColor=ffd343
[unittest-url]: https://docs.python.org/3/library/unittest.html

[tdd]: https://img.shields.io/badge/Test_Driven_Development-grey?style=for-the-badge
[tdd-url]: https://www.guru99.com/test-driven-development.html

[main-repo-url]: https://github.com/Spatch7/CS362Portfolio
[repo-actions-url]: https://github.com/Spatch7/CS362Portfolio/actions
[shields-url]: https://shields.io/
[icons-url]: https://simpleicons.org/

[email]: mailto:lubrano.alexander@gmail.com
[linkedin-url]: www.linkedin.com/in/lubrano-alexander
[repo-url]: https://github.com/lubranoa/CS362-Portfolio-Project