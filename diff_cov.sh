#!/usr/bin/env bash

# INSTRUCTIONS

# !!!INSTALL THIS FIRST!!!
# Script needs flake8, pytest-cov, and diff-cover packages to work - use pip install to get them.
# pip install flake8 pytest-cov diff-cover

# COMMAND LINE ARGUMENTS:

# -ft or --force-test
#   to force rerun of the test suite. To start from scratch  use -cr option).

# -nt or --no-test
#   to disable testing (if you just want to refresh previous results. If both -ft and -nt are specified we exit with an error.

# -cb <branch> or --compare-branch <branch> (i.e.: -cb upstream/master)
#   to change the default compare branch. If always using the same one just set it in the variables below.

# -lc or --last-commit
#   to run tests only if there is a diff between most recent changes and the last commit on current branch.
#   This is used to determine if tests should be rerun. By default we check between last commit on current branch and
#   the point when we diverged from the compare branch.

# -cr or --clean-run
#   to delete: diff_reports folder and .coverage, .coverage.*, coverage.xml files and rerun test suite.

# GENERAL INFO

# Use this script to run tests, generate coverage report and show lint / coverage ONLY for the diff on current branch.
# By default the diff is measured to origin/develop - USE COMPARE_BRANCH variable or -cb option to set a non standard
# comparison branch.

# ON DIFF-COVER

# The diff-cover command requires project's coverage report which is stored in coverage.xml file.
# This will be created by pytest-cov (make sure you add coverage.xml to global .gitignore - info below).

# AFTER MERGING INTO WORK BRANCH

# If you had to merge develop/master/etc. into your current branch during work,
# run diff_cov.sh -ft to measure project's coverage again (otherwise the results could be skewed - you can check though
# and let me know if it deals with merging into work branch well).

# RESULTS

# If you have 100% lint quality and 100% code coverage in your diff you should see a message in CLI and a :),
# in other cases report(s) will be opened in a browser.

# Partially covered code is also measured but all missed lines are shown as red (not combination of red/yellow).

# CHANGES TO FILE STRUCTURE

# The script will create a new folder:

# diff_reports with 2 files:
#   diff_lint_report.html (pep8 violations)
#   diff_coverage_report.html (code coverage misses for the diff on your branch)
# Feel free to change those names as you wish.

# Also coverage package itself will create files:
#   .coverage
#   .coverage.<name of your machine>
#   coverage.xml
# The .coverage* files are not needed and will get deleted after each script run (we keep coverage.xml).

# ADD STUFF TO GLOBAL .gitignore

# Add the diff_reports folder and files to global .gitignore to avoid polluting the project:
# - subl ~/.gitignore_global - to edit file, below is my global gitignore contents for now:
# .idea/
# .coverage.*
# coverage.xml
# diff_reports/

# git config --global core.excludesfile ~/.gitignore_global - to add to git


# SCRIPT - feel free to enhance it!

# Defaults & constants
COV_CONFIG_FILE=setup.cfg # Path to coverage config file if used
REPORT_DIR='diff_reports'
LINT_FILE='diff_lint_report.html'
COV_FILE='diff_coverage_report.html'
COMPARE_BRANCH=origin/master   # Change to whatever is your base branch. i.e. origin/develop etc.
                                # Make sure variable is not a string - no quotes here!!!
LINT_PATH="$REPORT_DIR/$LINT_FILE"
#FLAKE8_PATH="$REPORT_DIR/flake8_html/index.html"
COV_PATH="$REPORT_DIR/$COV_FILE"
OS=`uname`
NO_LINES_MSG='No lines with'
NO_LINT_VIOLATIONS_MSG='Violations: 0 lines'
NO_MISSING_COVERAGE_MSG='Missing: 0 lines'

# Variables
force_test=false
no_test=false
last_commit=false
lint_diff=''
coverage_diff=''
no_issues_found=true
clean_run=false
declare -A browser_commands=( ["Linux"]=google-chrome ["Darwin"]=open )
declare -A report_files=( ["lint"]=${LINT_PATH} ["coverage"]=${COV_PATH} )
#declare -A report_files=( ["lint"]=${FLAKE8_PATH} ["coverage"]=${COV_PATH} )


function display_results() {
    # Launch a browser tab for each report with errors.
    for key in ${!diffs[@]}; do
        if [[ ${diffs[$key]} != *${NO_LINES_MSG}* && ${diffs[$key]} != *${NO_LINT_VIOLATIONS_MSG}* \
            && ${diffs[$key]} != *${NO_MISSING_COVERAGE_MSG}* && ${diffs[$key]} != '' ]]; then
            no_issues_found=false
            $(${browser_commands[$OS]} ${report_files[$key]})
        fi
    done
    if [[ "$no_issues_found" == true ]]; then
        echo "No issues found to report :). Good work!"
    fi
}


function make_clean_run() {
    echo "Deleting diff reports and coverage files..."
    rm -rf htmlcov/
    rm -rf diff_reports/
    rm -rf coverage.xml
    rm -rf .coverage.*
    rm -rf .coverage
}


function initial_setup() {
    clear
#    source /usr/local/bin/virtualenvwrapper.sh
#    workon platform
#    cd ~/dev/platform
}

initial_setup

# Parse CLI arguments
while [[ "$#" > 0 ]]; do case $1 in
  -ft|--force-test) force_test=true;;
  -nt|--no-test) no_test=true;;
  -cb|--compare-branch) COMPARE_BRANCH="$2"; shift;;
  -lc|--last-commit) last_commit=true;;
  -cr|--clean-run) clean_run=true;;
  *) echo "Unknown parameter passed: $1"; exit 1;;
esac; shift; done

if [[ "$clean_run" == true ]]; then
    make_clean_run
fi

# Sanity checks.
if [[ "$force_test" == true && "$no_test" == true ]]; then
    echo "You have specified mutually exclusive arguments: force-test == true and no-test == true."
    echo "Unable to continue."
    exit 1
fi

#Set git command as per CLI arguments used.
if [[ "$last_commit" == true ]]; then
    diff_cmd=(git diff)
else
    diff_cmd=(git diff ${COMPARE_BRANCH})
fi

# Find if there is a diff on current branch.
diff=$(${diff_cmd[@]}) || error=$?
if [[ ${error} ]]; then
    echo "Error: ${error}"
    exit 1
fi

if [[ ${#diff} > 0 ]]; then
    echo "Found diff on current branch."
else
    echo "No diff found on current branch."
fi

# Create reports folder if not present.
if [[ ! -d "$REPORT_DIR" ]]; then
    mkdir "$REPORT_DIR"
fi

# Create coverage.xml - project's coverage report if not present or files were modified/added/deleted in the branch.
# IMPORTANT: rerun the script with -ft option after any merge into your work branch to have the newest report.
if [[ "$no_test" == true ]]; then
    if [[ ! -f coverage.xml ]]; then
        echo "You have disabled testing but coverage.xml file is missing and is required for generating reports."
        echo "Consider running this script with -ft option to create coverage.xml file."
        echo "Unable to continue."
        exit 1
    fi
    echo "Testing disabled. Not running test suite. Using existing coverage.xml report."
elif [[ (! -f coverage.xml  || ${#diff} > 0  || "$force_test" == true) ]]; then
    echo "Running pytest and generating project's coverage report against branch: $COMPARE_BRANCH..."
    pytest --cov-config ${COV_CONFIG_FILE} --cov --cov-report term-missing --cov-report xml
fi

echo "Running diff lint check..."
#changed_files=$(git diff ${COMPARE_BRANCH} --name-only | grep -E '\.py$')
#lint_diff=$(flake8 ${changed_files} --format=html --htmldir=${REPORT_DIR}/flake8_html)
lint_diff=$(diff-quality --violations=flake8 --compare-branch="$COMPARE_BRANCH" --html-report "$LINT_PATH")
echo "${lint_diff}"

echo "Running diff coverage check..."
coverage_diff=$(diff-cover coverage.xml --compare-branch="$COMPARE_BRANCH" --html-report "$COV_PATH")
echo "${coverage_diff}"

echo "Deleting .coverage.* and .coverage files..."
rm -rf .coverage.*
rm -rf .coverage

declare -A diffs=( ["lint"]=${lint_diff} ["coverage"]=${coverage_diff} )
display_results
