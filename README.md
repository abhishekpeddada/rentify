# Rentify Project

In developing the Rentify application, we utilized a combination of technologies to create a robust and user-friendly platform for property management and browsing. Here's a brief overview of the technologies used:

Backend Development:

    Flask: We chose Flask as the backend web framework due to its simplicity, flexibility, and ease of integration with other Python libraries and frameworks. Flask provided a solid foundation for building RESTful APIs and handling user authentication and data management.
    SQLAlchemy: SQLAlchemy was used as the ORM (Object-Relational Mapping) tool to interact with the database. It allowed us to work with database models in an object-oriented manner and perform CRUD operations seamlessly.
    SQLite: SQLite served as the relational database management system (RDBMS) for storing application data. It provided a lightweight and self-contained solution suitable for development and testing purposes.
    Python: Python served as the primary programming language for backend development, enabling us to write clean, concise, and maintainable code.

Frontend Development:

    HTML: We used HTML (Hypertext Markup Language) for structuring the content of web pages. HTML provided the foundation for creating the layout and structure of the user interface.
    CSS: CSS (Cascading Style Sheets) was used for styling the HTML elements and defining the visual appearance of the application. We utilized CSS to create a responsive and visually appealing design.
    Jinja2: Jinja2 templating engine was used for generating dynamic content in HTML templates. It allowed us to inject Python code into HTML templates and render dynamic data from the backend.
    JavaScript: JavaScript was used for adding interactivity and dynamic behavior to the application. We employed JavaScript for client-side validation, handling form submissions, and implementing responsive features.

Session Management:

    Flask Session: Flask session management was utilized to maintain user sessions and store session data securely on the server-side. It allowed us to authenticate users, track their login status, and personalize their experience.

By leveraging these technologies, we were able to develop a feature-rich and responsive web application that meets the needs of both property sellers and buyers. The Rentify platform offers a seamless user experience, allowing users to browse, search, and manage properties effortlessly.

# Setup
Step 1: Install required Modules

```bash
pip install -r requirements.txt
```
Step 2: Create Database

```bash
python3 init_db.py 
```
Step 3: Run App

```bash
python3 app.py
```
