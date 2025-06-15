# FitHead
<img width="559" alt="image" src="https://github.com/user-attachments/assets/b2780ac3-abce-40cf-8bbf-915e10d9fb1d" />

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

### Reference API

### Get info.
```bash
curl --request GET \
  --url http://localhost:5001/about \
  --header 'User-Agent: insomnia/11.2.0'

```

<img width="875" alt="image" src="https://github.com/user-attachments/assets/1b055d28-aedc-4906-b4af-a8ac75a9f747" />


### Create an user
```bash
curl --request POST \
  --url http://localhost:5000/users/insert \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/11.2.0' \
  --data '{
	"username": "gouthamnplpok",
	"email": "plpgaok@gmail.com",
	"password": "tempKey@1234",
  "age": 30,
  "gender": "Male",
  "location": "Hyderabad",
  "interests": "Tennis, Cricket",
  "bio": "Engineer and Tennis player",
	"profile_picture": "Somepic"
}'
```

<img width="879" alt="image" src="https://github.com/user-attachments/assets/4b3347d9-af8e-4935-a452-ded78a59a245" />

### Verify User
```bash
curl --request GET \
  --url http://localhost:5000/users/gouthamnewp \
  --header 'User-Agent: insomnia/11.2.0'
```


### update user
```bash
curl --request PUT \
  --url http://localhost:5000/users/goutham \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/11.2.0' \
  --data '{
	"age": "25"
}'
```

### Generate Login Token
```bash
curl --request POST \
  --url http://localhost:5000/login \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/11.2.0' \
  --data '{
	"email": "plpgaok@gmail.com",
	"password": "tempKey@1234"
}'
```

### Verify token and API
```bash
curl --request GET \
  --url http://localhost:5000/contact \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDAwOTI0OSwianRpIjoiMDU4OWU3YTAtZGQ1Yi00MWExLTgwZDItNTRiNTI0NTUzOWYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImY3MjY2MjVhLWQ0NDEtNDhiZS1hMmZhLWRmMDE0ZWRhY2U5NSIsIm5iZiI6MTc1MDAwOTI0OSwiY3NyZiI6IjNhMTcwMDNmLTU3MzMtNDE1OS04Zjc3LWVhZDhhYWUxMjA3NCIsImV4cCI6MTc1MDAxMjg0OX0.1Zud7kT5qGyQMk_0v67ksY4bjcDBWimLl0jP16hqFwc'
```