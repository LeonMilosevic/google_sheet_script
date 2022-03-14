# Cyber Care Task_1

### Intro

Upload data to google sheets, each worksheet should be categorized.

### How to use it:

```
git clone https://github.com/LeonMilosevic/google_sheet_script.git
```

```
pip install -r requirements.txt
```

```
python main.py
```

### Pipeline Walkthrough:

Extract:

- Extract all transactions from source dir<br />
&darr;

Transform:

- Create additional column named category, based on week of the year and brand_id.

Load:
- Dump result in google sheets. <br />

### Expected Results:

- Google sheet with worksheets made from category.