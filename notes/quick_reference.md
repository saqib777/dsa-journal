# QA Quick Reference Card

Commands and patterns used every single day.
Print this and keep it on your desk.

---

## pytest Commands

```bash
pytest -v                          # verbose
pytest -s                          # show print output
pytest -x                          # stop on first failure
pytest -k "login"                  # filter by name
pytest -m smoke                    # run marked tests
pytest --tb=short                  # short traceback
pytest --durations=5               # show 5 slowest
pytest --html=report.html          # HTML report
pytest --cov=src                   # coverage
pytest -n auto                     # parallel
pytest solutions/arrays/ -v        # specific folder
pytest test_login.py::TestLogin    # specific class
pytest test_login.py::TestLogin::test_valid_login  # specific test
```

---

## Git Commands

```bash
git status                         # what changed
git diff                           # see changes
git add .                          # stage all
git commit -m "message"            # commit
git push origin main               # push
git pull origin main               # pull latest
git log --oneline --graph          # history
git checkout -b feature/name       # new branch
git stash                          # save work temporarily
git stash pop                      # restore saved work
```

---

## Python Virtual Environment

```bash
python -m venv .venv               # create
.venv\Scripts\activate             # activate Windows
source .venv/bin/activate          # activate Mac/Linux
pip install -r requirements.txt    # install deps
pip freeze > requirements.txt      # save deps
deactivate                         # exit venv
```

---

## Requests Quick Syntax

```python
import requests

r = requests.get(url, params={"key": "val"}, headers=h)
r = requests.post(url, json={"key": "val"})
r = requests.put(url, json=payload)
r = requests.patch(url, json=partial)
r = requests.delete(url)

r.status_code      # 200
r.json()           # dict
r.text             # string
r.headers          # dict
r.elapsed.total_seconds()  # float
```

---

## Selenium Quick Syntax

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locators
By.ID, By.NAME, By.CLASS_NAME, By.CSS_SELECTOR, By.XPATH

# Actions
driver.get(url)
driver.find_element(By.ID, "id").click()
driver.find_element(By.ID, "id").send_keys("text")
driver.find_element(By.ID, "id").text
driver.save_screenshot("ss.png")
driver.quit()

# Explicit wait
wait = WebDriverWait(driver, 10)
el = wait.until(EC.element_to_be_clickable((By.ID, "btn")))
```

---

## Commit Message Prefixes

```
add:      new solution or file
test:     test file
docs:     documentation
fix:      bug fix
refactor: code improvement
chore:    config, deps
ci:       CI/CD
```
