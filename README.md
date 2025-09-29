# ecommerce-app

E-commerce web app + end-to-end DevOps pipeline (Docker, GitHub Actions, Terraform, AWS ECS).

## Project Layout

- `app/` — your application source code (Django or Node)
- `docker/` — production Dockerfiles
- `docker-compose.yml` — for local development
- `infra/terraform/` — Terraform for AWS infrastructure
- `monitoring/` — configs for Prometheus, Grafana, cAdvisor
- `.github/workflows/ci-cd.yml` — CI/CD pipeline setup
- `task-definition.json` — ECS task definition template

## (Local Dev)

```bash
# using django 
docker compose up --build
# then run tests (pytest)
