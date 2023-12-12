![GitHub contributors](https://img.shields.io/github/contributors/vitaliisili/job-application-django)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/vitaliisili/job-application-django)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/vitaliisili/job-application-django)
![GitHub License](https://img.shields.io/github/license/vitaliisili/job-application-django)
![Static Badge](https://img.shields.io/badge/Python-3.9%2C%203.10%2C%203.11-blue)

# Job Application Monitoring API

*Introducing the Job Application Monitoring API – an advanced solution to seamlessly integrate job application tracking into your existing applications, platforms, or workflows. This powerful API empowers developers and businesses to enhance their application tracking capabilities and provide users with a comprehensive tool for managing job applications programmatically*

***

## :hammer_and_wrench: Get Started
- Clone Project
```bash
git clone https://github.com/vitaliisili/job-application-django.git
```

- Go to project folder
```bash
cd job-application-django
```

- Create virtual environment
```Bash
python3 -m venv .venv  
```

- Activate virtual environment
```Bash
source .venv/bin/activate
```

> ### :grey_exclamation: **Note**
> - Next commands will be run with `make`. If make is not installed, just copy commands from `Makefile` 

> ### :warning: **Warning**
> - All commands with `make` must be run from root folder 
> - If you do not use `make` cd to folder `api` and run commands manually there

- Create `.env` file
```Bash
make create-env
```
> ### **Note**
> - This will create `.env` file in `api` folder fill all environment variable with valid data


- Install project dependency
```Bash
make install 
```

- Migrate Database
```Bash
make makemigration 
```

- Apply migration
```Bash
 make migrate
```

- Create `superuser`
```Bash
make createsuperuser
```

- Run server
```Bash
make runserver 
```

- Done