# FitHead
## Setup Instructions

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

### Steps

1. **Clone the repository:**
   ```bash
   git clone git@github.com:pratapalakshmi/fithead.git
   cd fithead
   ```

2. **Build and start the services:**
   ```bash
   docker compose up -d
   ```
   This command will build the Docker images and start all services defined in your `docker-compose.yml` file.

3. **Access the application:**
   - By default, the Flask app will be running at [http://localhost:5000](http://localhost:5000).

4. **Stopping the application:**
   ```bash
   docker compose down -v
   ```

### Additional Notes

- If you make changes to dependencies or the Dockerfile, re-run with `--build` to rebuild the images.
- Database migrations are handled automatically on container startup.
- For development, you can modify the source code and restart the containers as needed.

For any issues, please refer to the project documentation or open an issue in the repository.
