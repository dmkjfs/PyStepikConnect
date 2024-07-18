<div align="center">
    <a href="https://github.com/ilkztsff/PyStepikConnect/blob/dev/LICENSE">
      <img src="https://img.shields.io/github/license/ilkztsff/PyStepikConnect?label=License&color=purple&style=for-the-badge">
    </a>
    <a href="https://github.com/ilkztsff/PyStepikConnect/blob/dev/pyproject.toml">
      <img src="https://img.shields.io/badge/python-3.7+-purple?style=for-the-badge">
    </a>
    <a href="https://github.com/ilkztsff/PyStepikConnect/actions/workflows/check.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/ilkztsff/PyStepikConnect/check.yml?branch=dev&style=for-the-badge&label=linter&color=purple">
    </a>
    <a href="https://github.com/ilkztsff/PyStepikConnect/actions/workflows/publish.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/ilkztsff/PyStepikConnect/publish.yml?branch=dev&event=push&style=for-the-badge&label=build&color=purple">
    </a>
</div>

<h1 align="center">PyStepikConnect</h1>


## ✍ About

PyStepikConnect is a python library for using Stepik REST API. You can see Stepik REST API documentation - [here](https://stepik.org/api/docs)


## ⬇️ Installation

Required to have `python` installed

```bash
pip install pystepikconnect
```


## 🧑‍💻 Usage

Quick start guide and full documentation are available on
[wiki](https://github.com/ilkztsff/PyStepikConnect/wiki) tab


## 💿 [Dependencies](https://github.com/ilkztsff/PyStepikConnect/blob/dev/setup.py)

- **[requests](https://pypi.org/project/requests) >= 2.25.1**

- **[types-requests](https://pypi.org/project/types-requests) >= 2**

- **[pydantic](https://pypi.org/project/pydantic) >= 2.5.0**

<br>


<details><summary><h1>💻 For devs</h1></summary>

## 🛠 Build commands

Required to have `git`, `make` and `python` installed

Download project from GitHub
```bash
git clone https://github.com/ilkztsff/DeliveryDetect/
```
<br>

Install dependencies
```bash
make install
```
<br>

Lint the project
```bash
make lint
```
<br>

Build project
```bash
make build
```
<br>

Publish project to PyPI
```bash
make publish
```
<br>

Run *black*
```bash
make fix
```

## 🖥 Environment

Environmental variables are only required for testing
(testing instruction below). Put them into `.env` file

- `TEST_ID` - client id of your application. Get it [here](https://stepik.org/oauth2/applications)
- `TEST_SECRET` - client secret of your application. Get it [here](https://stepik.org/oauth2/applications)


## 🧪 Testing

Clone the project
```bash
git clone https://github.com/ilkztsff/DeliveryDetect/
```
<br>

Run tests
```bash
make test
```
<br>

See test coverage
```bash
make coverage
```
</details>

