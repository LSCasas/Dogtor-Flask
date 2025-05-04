# Dogtor

A Flask-based web app for managing pet owners, pets, vets, and appointments, built for educational purposes to demonstrate route-based entity relationships.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#how-to-use-this-project)
- [Requirements](#requirements)
- [Contribution](#contribution)
- [Learn More](#learn-more)

---

## Project Structure

```
Dogtor-Flask/
├── app.py               # Main Flask application
├── templates/           # HTML templates
├── static/              # Static assets (CSS, JS)
├── requirements.txt     # Python dependencies
├── example.env          # Environment variable example file
├── README.md            # Project documentation
```

---

## Features

- Create and manage pet owners
- Register and edit pet information
- Assign veterinarians to pets
- Schedule veterinary procedures and appointments
- Integrated with MongoDB
- Traditional route-based system without REST conventions

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LSCasas/Dogtor-Flask.git
   cd dogotor_flask_mongodb
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   Copy the example file and edit your settings:

   ```bash
   cp example.env .env
   ```

4. **Run the server:**

   ```bash
   python app.py
   ```

---

## How to Use This Project

### Example Requests

Use `curl` or Postman to test routes.

**1. Add Veterinarian:**

```bash
curl -X POST -d "nombre=Dr. Ana López&especialidad=Cardiología&telefono=555-2222" http://localhost:5000/veterinarios/agregar

```

**2. Get Veterinarian by ID:**

```bash
curl http://localhost:5000/veterinarios/obtenerPorId/YOUR_VET_ID

```

**3. Update Veterinarian:**

```bash
curl -X POST -d "nombre=Dr. Ana López&especialidad=Neurología&telefono=555-3333" http://localhost:5000/veterinarios/actualizar/YOUR_VET_ID

```

---

## Architecture Notes

It is important to note that this project does NOT follow a REST-based architecture as it was developed for educational purposes and does not require that complexity. Instead of REST, it uses a traditional route-based architecture in Flask.

---

## Requirements

- Python 3.x
- Flask
- MongoDB or PostgreSQL

---

## Contribution

If you want to contribute to this project, follow the steps below:

1. Fork the repository.

2. Create a new branch for your feature:

   ```bash
   git checkout -b feature/new-feature
   ```

3. Make your changes.

4. Commit your changes:

   ```bash
   git commit -am 'Add new feature'
   ```

5. Push your changes to your fork:

   ```bash
   git push origin feature/new-feature
   ```

6. Create a Pull Request for your changes to be reviewed and merged into the main project.

---

## 📚 Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Dotenv for Python](https://pypi.org/project/python-dotenv/)

---

Your feedback and contributions to this project are welcome!
