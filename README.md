# Multi User Todo Application using Django
![image](https://github.com/user-attachments/assets/dd914a0e-c9d5-4d90-aa0f-e86b0b451929)

## Project Image

![Project Image](path/to/image.png) <!-- Replace with actual image path or URL -->

## Description
This project is a multi-user todo application built using Django. It allows users to create, manage, and track their tasks in a collaborative environment.

## Features
- User registration and authentication
- Create, edit, and delete tasks
- Assign tasks to specific users
- Mark tasks as completed
- Filter tasks based on status, priority, etc.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Ayushsav/Todo_app_using_django.git
   ```
2. Navigate to the project directory:
   ```sh
   cd todo
   ```
3. Install dependencies:
   ```sh
   pip install django
   ```
4. Set up the database:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
1. Access the application through your browser at [http://localhost:8000/](http://localhost:8000/)
2. Register as a new user or log in with an existing account
3. Add and manage your todo tasks
4. Collaborate with other users by assigning tasks to them

## Contributing
If you'd like to contribute to this project, follow these steps:

1. Fork the repository
2. Create a new branch:
   ```sh
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```sh
   git push origin feature/your-feature
   ```
5. Submit a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
