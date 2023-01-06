<h1 align="center">
📺 TeVe Backend
</h1>

This repository is developed as a backend for [TeVe App](https://github.com/7-USH/TeVe). This backend utilizes the following tech-stack:

- [🐳 Docker](https://www.docker.com/)
- [🐍 FastAPI](https://fastapi.tiangolo.com/)

## Why above Tech-Stack?

- FastAPI is crowned as the fastest web framework for Python and thus we use it for our backend development.
- Docker is a technology that packages an application into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.

## Setup Guide

This backend application is setup with Docker. Nevertheless, you can see the full local setup without Docker.


1. Create a virtual-env

```python
pyenv virtualenv 3.11.0 any_venv_name
pyenv local any_venv_name
```

2. Install dependencies

```python
pip3 install -r requirements.txt
```

3. Test run your backend server

```python
uvicorn main:app --reload
    or
python main.py
```

## Deployment

for hosting purpose, this backend application is hosted on [Okteto](https://www.okteto.com/).

## API Reference

#### Login

```http
  POST /login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | email |
| `password` | `string` | password |

#### Sign Up

```http
  POST /user/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | username  |
| `password` | `string` | password |
| `email` | `string` | email |

### Get User

```http
  GET /user/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. your Access Token |


### Add to Favourites

```http
  POST /fav/add
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `stream_link` | `string` | **Required**. your Access Token  |
| `channel_name` | `string` | **Required**. your Access Token  |
| `category` | `string` | **Required**. your Access Token  |


### Get Favourites

```http
  GET /fav/add
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `none` | **Required**. your Access Token  |


### Delete Favourite

```http
  DELETE /fav/delete
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `stream_link` | `string` | **Required**. your Access Token  |
| `channel_name` | `string` | **Required**. your Access Token  |
| `category` | `string` | **Required**. your Access Token  |


