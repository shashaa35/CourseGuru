# CourseGuru

CourseGuru is a Django-based web application for discovering and reviewing online courses.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/CourseGuru.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CourseGuru
   ```

3. Create a virtual environment:

   ```bash
   # For Windows
   python -m venv venv

   # For macOS/Linux
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   # For Windows
   venv\Scripts\activate

   # For macOS/Linux
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application at http://localhost:8000/ in your web browser.

## Usage

- Browse the catalog of courses by visiting the home page.
- Use the search functionality to find courses by title.
- Click on a course to view detailed information.
- Register as a user to review and rate courses.
- Explore information about course providers and instructors.

## API Documentation

The API endpoints in CourseGuru are documented using drf-yasg, a Swagger/OpenAPI generator for Django REST Framework. To access the API documentation:

1. Start the development server if not already running:

   ```bash
   python manage.py runserver
   ```

2. Navigate to http://localhost:8000/swagger/ in your web browser.

3. You'll see the Swagger UI, where you can explore and interact with the available API endpoints.

## Contributing

Contributions are welcome! If you'd like to contribute to CourseGuru, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thank you to the Django and Django REST Framework communities for providing powerful tools for building web applications.
- Special thanks to all contributors to this project.