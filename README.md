# Rental Company System

A beginner project I built to practice OOP in Python. Covers movies and TV show rentals with age restriction handling

## About

I made this to keep practicing OOP concepts like abstract classes,
inheritance and encapsulation. Customers can rent movies and TV shows,
and the system handles age restrictions — minors need parental permission
to rent R-rated content.

## Project Structure

```
rental-company/
├── main.py          # Entry point
├── people.py        # People, Customer and Employee classes
├── products.py      # Product, Movie and TvShow classes
├── rental_shop.py   # RentalShop class (main system)
├── utilities.py     # Helper functions and transaction formatters
├── requirements.txt # Dependencies
├── .env.example     # Environment variables example
└── .gitignore
```

## How to Run

```bash
git clone https://github.com/tiagoalcantara7/rental-company.git
cd rental-company
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # Mac/Linux
copy .env.example .env # Windows
python main.py
```

## Stack

- Python 3.12+
- python-dotenv
- logging
- ABC

## What I practiced

- Abstract classes and inheritance
- Encapsulation with `@property` and `@setter` for data validation
- Abstract methods to enforce interface contracts
- Composition — RentalShop holds customers, employees and products
- Type hints throughout the codebase
- Docstrings on classes and functions
- Logging with different levels
- Environment variables with dotenv
