# Loan Data Analysis Project

## Introduction

The Alternative Lending Team analyzes significant amounts of loan data that is sourced from a number of different vendor platforms. While loan data from different lending platforms is conceptually similar, there is no common format or standard terminology across platforms. Since the team's decision making is powered by this data, it is crucial that the information is normalized across sources and stored to a common format that is easily accessible for research and trading.

We’ve put together a data-centric project that focuses on building infrastructure around this information. This project is designed primarily to challenge you to understand the structure of unfamiliar datasets, implement a system for ingesting and exposing these datasets, and running some light-weight analysis.

The deliverables for this project are:

1. An implementation plan.
2. A system that loads and normalizes data from these vendor platforms.
3. Analysis that reaveal trends and anomolies in the data.
4. A presentation describing your approach to the problem, key design decisions that were made both up-front and along the way, and what you learned in executing the project.

The scope of this project is intentionally broad, we encourage you to focus on the portions that you find most interesting, and to ask for clarifications wherever they may be needed. The engineering team at Stone Ridge works collaboratively and we'd like for you to work on this project as though you are a member of the team. Please don't hesitate to reach out for guidance if you're having trouble by submitting questions and requests as 'Issues' in the GitHub interface and by submitting pull requests for code that you'd like feedback on. We’ll make a point of being available to you.

As far as the tools that you should use, we write Python code every day, but you’re welcome to use whatever language you feel most comfortable in. While you're free to develop locally or create an AWS account to leverage infrastructure in the cloud (we'll reimburse you for any costs you incur), we've provided a [Vagrantfile](https://www.vagrantup.com/intro/index.html) for building a disposable development environment based on an Ubuntu virtual machine provisioned with [Anaconda](https://www.anaconda.com/distribution/), [VS Code](https://code.visualstudio.com/docs/setup/linux), [Pycharm](https://www.jetbrains.com/pycharm/download/#section=linux), [Postgres](https://www.postgresql.org/), and [Docker](https://www.docker.com/). We also provide an Anaconda [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) file for creating an Anaconda virtual environment for python. We fully endorse adding the IDE and tools of your choice to this provisioning process if that is the route you choose to go (feel free to reach out with questions if you're committed to this and need some help getting off the ground).

Good luck!

### Part 1 – Project Planning

After you finish reviewing the requirements for this project, we'd like for you to create an outline of how you intend to approach the problem and what you would like to deliver along the way. This is mainly to ensure that we're all on the same page about the scope of this project. Please create this outline in the IMPLEMENTATION.md file and create pull request so that the team can provide guidance and feedback.

### Part 2 - Data Collection and Aggregation

There are three vendor-provided datasets for use in your analysis, one dataset is from Lending Club whose data can be loaded from their public site [here](https://www.lendingclub.com/info/download-data.action) and [here](http://additionalstatistics.lendingclub.com/), but which has been provided along with two other anonymous datasets via DropBox [here](https://stoneridgeassetmanagement.box.com/s/gnicdp5izn0cc3b4iokejl21tk9owfgt).

Based on this data, we would like you to design and implement software to acheive the following goals:

* Gather essential datapoints across each of the platforms:
  * Loan ID
  * Issue date
  * Original balance
  * Interest rate
  * Platform rating
  * Loan Status
  * Principal remaining
  * Principal paid
  * Interest paid
* Load this data (and any other you may identify as important) into database tables for which you will define a coherent schema. Note that some fields (like loan ID and issue date) are static, while others (like principal remaining) change over time.
* Identify deals with “bad” values.
* Derive values from other platform data as necessary.
Some of the platform data may have different structure.  Please use your best judgment in how to reconcile this to produce useful panel data.  A few things to note:
  * Loans are typically considered “charged off” (e.g. the borrowers aren’t expected to pay the loans off) after no payment has been made for more than 120 days.
  * It’s often useful to track loan performance metrics by “month on books” – i.e. the loan’s age in months – rather than calendar month.
  * There’s generally a “grace period” past a payment’s due date during which the borrower isn’t yet considered delinquent.

### Part 3 – Data Analytics

Once we’ve got clean data, we want to use it to answer questions about our portfolio.  We’ll focus on one particular piece of analysis here: how each platform’s underwriting changes over time.  Within a platform, we typically compare different vintages of loans – loans that are issued within the same quarter – with those loans sometimes further broken out by grade. We would like for you to investigate how deliquency rates vary across vintages for the same platform and across platforms for the same vintage.

We’d like you to put together a set of data visualizations that you think tell an interesting story about these platforms’ loans. The metrics above are a good place to start, but if there’s anything else you’d like to consider, that’s great too.

### Part 4 – Presentation

We’d like you to put together a presentation that walks us through what you did and how you reasoned about the problem.  It should include some of the visualizations you put together in Part 2 and help us understand what happened at the platforms.  It should also put special emphasis on the key decisions you made in Part 1, why you made them, and how they influenced the work you did in Part 2.

Ideally, we would like to start with an outline

### Development Environment

We provide some infrastructure to help get off the ground. You may choose not to use this at all, and you should only use these tools if you are comfortable with them. If you find that they slow you down, do not use them!

* [Vagrant](https://www.vagrantup.com/intro/index.html) is typically used to provision long-lived environments that support interactive login. Vagrant essentially starts a VM and provisions it with an operating system any software that you may want to install. At Stone Ridge, we use Vagrant along with Ansible to provision our disposable Linux development environment that can run on Windows and Mac OS.

#### Vagrantfile

The provided `Vagrantfile` creates an Ubuntu VM and the local directory synced to `/home/vagrant/development/LoanDataAnalysis`. You can provision this environment on MacOS using Homebrew:

 ```sh
 brew cask install vagrant
 brew cast install virtualbox
 vagrant plugin install vagrant-vbguest
 ```

Or on Windows using Powershell and Chocolatey:

 ```sh
 choco install virtualbox -y
 choco install vagrant -y
 choco install xming -y
 C:\HashiCorp\Vagrant\bin\vagrant plugin install --plugin-version 0.15.1 vagrant-vbguest
 ```

You can then change your current directory to the one that this README file lives in and run the commands to provision the virtual machine and log in:

```
vagrant up
vagrant ssh
```

At this point you can login as the postgres user to administer the database with the following commands:

```
vagrant@ubuntu-bionic:~$ sudo su postgres
postgres@ubuntu-bionic:/home/vagrant$ psql
psql (10.8 (Ubuntu 10.8-0ubuntu0.18.04.1))
Type "help" for help.

postgres=#
```

Or activate the anaconda python environment and run python:

```
vagrant@ubuntu-bionic:~$ conda activate loan-analysis
(loan-analysis) vagrant@ubuntu-bionic:~$ python
Python 3.7.0 | packaged by conda-forge | (default, Nov 12 2018, 20:15:55)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

Or fire up pycharm:

```
vagrant@ubuntu-bionic:~$ /home/vagrant/dev-tools/pycharm-community-2019.1.3/bin/pycharm.sh
```

Or VS Code:

```
vagrant@ubuntu-bionic:~$ code
```