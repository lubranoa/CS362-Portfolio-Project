<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- Centered title section with descriptive lines -->
<div align="center">
  <!-- Badges -->
  <p>
    <a href="https://www.linkedin.com/in/lubrano-alexander">
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
  <h1 align="center">Continuous Integration in Collaborative Python Development</h1>
  <p align="center">
    <b>Co-development of Python functions using Test-Driven Development (TDD) and a Continuous Integration (CI) workflow with GitHub Actions in a shared repository.</b>
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
    - [GitHub CI Workflow](#github-ci-workflow)
    - [Function Development](#function-development)
  - [Skills Applied](#skills-applied)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

</details>

<!-- Project Description -->
## Project Description

This project involved establishing a Continuous Integration (CI) workflow to streamline team collaboration and ensure robust software testing. The primary objectives were to set up a shared private GitHub repository, configure a CI pipeline using GitHub Actions, and implement Python functions guided by Unit Testing and Test-Driven Development (TDD).

Each teammate was responsible for developing one of three functions. I implemented an endian conversion function that converts integers to their hexadecimal representation in either little or big endian formats. This function was developed using a comprehensive TDD process, validated through peer code reviews, and tested via the CI pipeline. The project emphasized the integration of CI and TDD methodologies to deliver high-quality, reliable code.
**Note**: This repository is a fork of our group's main repository, accessible [here][main-repo-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Technologies Used -->
## Technologies and Frameworks Used

   - [![python][python]][python-url]
   - [![github-wf][github-wf]][github-wf-url]
   - [![unittest][unittest]][unittest-url]
   - [![tdd][tdd]][tdd-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Features -->
## Features
   
  Because this program is an exercise in Continuous Integration and testing, it does not have the features of a program that can be run to solve a problem or do something for you. Here are some "*features*" of this project.

  - Configured a GitHub Actions workflow to automate testing and integration in a shared repository.

  - Developed unit tests and designed test suites using Python's unittest framework.

  - Implemented Test-Driven Development (TDD) methodologies to guide function implementation.

  - Conducted peer code reviews to maintain code quality and facilitate knowledge sharing.

  - Established a Continuous Integration (CI) pipeline to streamline team collaboration and ensure robust software testing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->
## Usage

Seeing as this is not a program used to accomplish something, this section will focus more on the usage of the CI workflow in `python-app.yml` and the development of my testing section of `test.py` and my function in `task.py`.

### GitHub CI Workflow

The following workflow carries out a few major things:

  1) Runs when pushes or pull requests trigger it.

  2) Sets up Python on an Ubuntu virtual machine.
  
  3) Installs any dependencies in the `.yml` file and in a `requirements.txt` file if present (if not, it's skipped).

  4) Lints any Python files for issues.
  
  5) Runs the test suite named `tests.py`.

  ```yml
  name: Python application

  on: [push, pull_request]

  permissions:
    contents: read

  jobs:
    build:

      runs-on: ubuntu-latest

      steps:
      - uses: actions/checkout@v3
      - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Lint with flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
      - name: Test with Unittest
        run: |
          python tests.py
          
    # For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
  ```

The main goal of this CI workflow is to protect the main branch of the repository from errant or broken code. It accomplishes this in multiple ways:

  - Checks the code for syntax issues and errors. Any issues with the code must be fixed before creating a pull request.
  - Requires a pull request before merging a branch to the main branch.
  - Requires at least one approval from a repo collaborator.
  - Does not allow bypassing of the above settings.

Since this is a fork, the main repo's workflow history between the teammates can be found in its [Actions history][repo-actions-url].

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Function Development

The project specifications stated that the function `conv_endian` must convert integers to a hexadecimal number split into two-character bytes in either little or big endian byte orders, depending on what was specified when calling the function. My approach to solving this problem was to develop it using Test Driven Development (TDD).

The core principle of TDD is that one only writes new code if there exists at least one failing test. Thus, the basic steps of TDD are to write a test that fails, then to write code that makes that test and all other tests pass, and then to repeat that until requirements are met. 

My TDD process started off with writing tests for more simple conversions like the integers 0 and 6, then wrote code to make them pass, and moved on to more complex integers like 10, 15, and 16. This continued while slowly increasing integer size and complexity, such as integers that convert to two bytes or more of hexadecimal, adding in negative integers, and converting to little or big endian. Below is a snippet of the first few tests. The full test suite for `conv_endian` can be found in the [`tests.py`](/tests.py) file.

```python
# Verifies if the number 0 is returned correctly
def test1_conv_end(self):
    number = 0
    self.assertEqual(conv_endian(number), '00')

# Verifies if the number 6 is returned properly
def test2_conv_end(self):
    number = 6
    self.assertEqual(conv_endian(number), '06')

# Verifies if the number 9 is returned properly
def test3_conv_end(self):
    number = 9
    self.assertEqual(conv_endian(number), '09')

# Verifies if the number 10 is returned properly
def test4_conv_end(self):
    number = 10
    self.assertEqual(conv_endian(number), '0A')
```

Once the requirements for `conv_endian` were completely met by the function I developed in [`task.py`](/task.py), my TDD process was finished. This was the final version turned in for a grade. Some other testing that would have been beneficial after TDD was some form of dynamically generated randomized testing. This would have been the perfect followup because it could have potentially caught any edge cases that I missed via TDD. Any failed tests could have been logged for use in more TDD steps, which could have helped polish `conv_endian` even further.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Skills Applied -->
## Skills Applied

  - Developed unit tests and designed test suites using Python's unittest framework.

  - Implemented Test-Driven Development (TDD) methodologies to guide function implementation.

  - Configured Continuous Integration workflows using GitHub Actions to automate testing and deployment.

  - Collaborated with team members through GitHub for version control and code reviews.

  - Resolved merge conflicts and coordinated code integration in a team environment.

  - Communicated effectively with team members to ensure cohesive development and adherence to project timelines.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

Alexander Lubrano - [lubrano.alexander@gmail.com][email] - [LinkedIn][linkedin-url]

Project Link: [https://github.com/lubranoa/CS362-Portfolio-Project][repo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Acknowledgments -->
## Acknowledgments

  - [Main Group Repo][main-repo-url]
  - [Main Group Repo Actions History][repo-actions-url]
  - [GitHub Actions Workflow Documentation][github-wf-url]
  - [Python unittest Documentation][unittest-url]
  - [Test Driven Development][tdd-url]
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
[linkedin-url]: https://www.linkedin.com/in/lubrano-alexander
[repo-url]: https://github.com/lubranoa/CS362-Portfolio-Project