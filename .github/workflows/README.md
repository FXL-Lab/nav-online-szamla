# GitHub Actions Setup

This repository includes two GitHub Actions workflows:

## 1. Test Workflow (`test.yml`)

**Triggers:**
- Manual trigger via `workflow_dispatch`
- When a Pull Request is opened, synchronized, or reopened against `main` or `develop` branches

**What it does:**
- Runs tests across multiple Python versions (3.9-3.13)
- Tests with pytest including coverage reporting
- Performs code quality checks (black formatting, flake8 linting, mypy type checking)
- Uploads coverage reports to Codecov

## 2. Publish Workflow (`publish.yml`)

**Triggers:**
- When a Pull Request is merged into the `main` branch

**What it does:**
- Checks if the version in `pyproject.toml` has been bumped
- Runs tests before publishing
- Builds and publishes the package to PyPI
- Creates a GitHub release with the new version tag
- Comments on the PR with publication details

## Required Secrets

To use these workflows, you need to set up the following secrets in your GitHub repository:

### For PyPI Publishing (`publish.yml`)

1. **`PYPI_API_TOKEN`** - Your PyPI API token
   - Go to [PyPI Account Settings](https://pypi.org/manage/account/)
   - Create a new API token with appropriate scope
   - Add it as a repository secret in GitHub

### Setting up GitHub Secrets

1. Go to your repository on GitHub
2. Navigate to `Settings` → `Secrets and variables` → `Actions`
3. Click `New repository secret`
4. Add the required secrets listed above

## Usage

### Running Tests
- Tests will automatically run on every PR
- You can also trigger tests manually from the Actions tab

### Publishing to PyPI
1. Bump the version in `pyproject.toml` using Poetry:
   ```bash
   poetry version patch  # for bug fixes
   poetry version minor  # for new features
   poetry version major  # for breaking changes
   ```
2. Create a PR with your changes
3. Once the PR is merged, the package will automatically be published to PyPI (if the version was bumped)

## Notes

- The publish workflow only runs if the version in `pyproject.toml` is different from what's already on PyPI
- All tests must pass before publishing
- A GitHub release is automatically created with each publish
- The workflows use Poetry for dependency management and packaging
