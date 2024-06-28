# Simple Sports Betting Website
Frontend - https://github.com/arsenyeganyan/casino-sample
Backend  - https://github.com/Aren2020/Sports-Betting

This project is a simple implementation of a sports betting website backend using Django REST Framework (DRF). Users can view upcoming matches, place bets, and view their betting history.

## Features

- **Authentication and Authorization**: Users can register, log in, and log out. JWT tokens are used for authentication.
  
- **Match Management**: Admins can add new matches, update match details, and delete matches.

- **Betting**: Users can place bets on upcoming matches with specified odds.

- **User Profiles**: Users can view their profile and update their information.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Aren2020/Sports-Betting.git
   cd Sports-Betting
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Access the API at `http://localhost:8000/`.

   
