# Virtual Environment Guide 🐍

This file explains what **Python virtual environments** are and why I use them.  
Written simply for beginners (and future me 😄).

---

## What is a Virtual Environment?
A virtual environment is like a **separate space** for each Python project.  
It keeps project dependencies **isolated**, so different projects don’t clash.

Think of it like having different **rooms** for different projects, each with its own setup.

---

## Why I Use Virtual Environments
- Avoid version conflicts between projects (e.g., Flask 2.3 vs Flask 3.0)
- Keep my system Python clean
- Make projects easier to share with others

---

## Creating a Virtual Environment
To create one, run:

```bash
python3 -m venv myenv
```
Here, myenv is the name of the environment.

## Activating the Virtual Environment

- linux / macos

```bash
source myenv/bin/activate
```

- windows
```bash
myenv\Scripts\activate
```

## Deactivating the Virtual Environment
When done, simply type:

```bash
activate
```

## Installing Packages Inside the Environment
Once inside, you can safely install packages:

```bash
pip install flask
```
These packages will only exist in this environment.

