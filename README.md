# DOGTOR

**Short Description**: This project is a platform to manage pet owners, pets, veterinarians, procedures, and veterinary appointments. It allows administrators to manage the relationships between these elements efficiently.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)

## Description

This system was developed as part of a university project. It is designed to manage the information of pet owners, the pets themselves, available veterinarians, and the procedures they perform. Additionally, it allows for the creation and management of appointments between pets and veterinarians, ensuring that all related data is kept up to date.

It is important to note that this project does **NOT** follow a REST-based architecture as it was developed for educational purposes and does not require that complexity. Instead of REST, it uses a **traditional route-based architecture in Flask**, where functionalities are managed directly through specific routes for each resource (owners, pets, veterinarians, procedures, appointments), without adhering to RESTful service conventions.

### Project Example

This project includes features such as:

- Creating pet owners.
- Managing information about veterinary procedures.
- Registering appointments for pets with veterinarians and assigned procedures.
- Linking owners, pets, veterinarians, and procedures through their identifiers.

## Installation

### Requirements

- Python 3.x
- MongoDB or PostgreSQL (depending on the case)
- Flask

### Steps

1. Clone the repository:

   ```bash
   git clone git@github.com:LSCasas/Dogtor-Flask.git
   ```

2. Navigate to the project folder:

   ```bash
   cd
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (if needed):

   Copy the `example.env` file to `.env` and edit it with your MongoDB configurations, server port, and other required variables.

   ```bash
   cp example.env
   ```

5. Start the server:

   ```bash
   python app.py
   ```

## Usage

The system is designed to be used as an API that allows managing entities such as owners, pets, veterinarians, procedures, and appointments. Below are some examples of how to interact with the main functionalities:

### Basic Example

1. **Create an owner:**

   Make a POST request to `/owners/add` with the owner data (name, address, phone number).

   ```bash
   curl -X POST -d "name=Carlos Méndez&address=Fictitious Street 123, City A&phone=555-1111" http://localhost:5000/owners/add
   ```

2. **Create a pet:**

   Make a POST request to `/pets/add` with the pet data (name, species, age, owner_id).

   ```bash
   curl -X POST -d "name=Firulais&species=Dog&age=3&owner_id=67e5d25a46c5d4ef325adff0" http://localhost:5000/pets/add
   ```

3. **Create an appointment:**

   Make a POST request to `/appointments/add` with the appointment data (date, time, pet_id, veterinarian_id, procedure_id).

   ```bash
   curl -X POST -d "date=2025-03-27&time=10:00&pet_id=67e5d4fd10fa97975cbba72e&veterinarian_id=67e5d1cd46c5d4ef325adfeb&procedure_id=67e5d38810fa97975cbba729" http://localhost:5000/appointments/add
   ```

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
