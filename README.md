# Oregon City Tax Rates & Population Data

Interactive marimo notebook displaying property tax rates and 2024 population data for 233 Oregon cities.

<!-- Replace YOUR_USERNAME with your GitHub username -->
[![Run with marimo](https://marimo.io/shield.svg)](https://marimo.io/p/@YOUR_USERNAME/oregon-city-tax-rates/explore_city_tax_data.py)

## Data Sources

- **Property Tax Data**: FY 2024-25 Property Tax Statistics Supplement
- **Population Data**: Portland State University Population Research Center - 2024 Certified Population Estimates (July 1, 2024)

## Running Locally

### Prerequisites

- Python 3.11+
- Required packages: `marimo`, `pandas`, `numpy`, `openpyxl`

### Install Dependencies

```bash
pip install marimo pandas numpy openpyxl
```

### Run the App

**Interactive mode (edit):**
```bash
python -m marimo edit explore_city_tax_data.py
```

**Read-only mode (app):**
```bash
python -m marimo run explore_city_tax_data.py --no-sandbox
```

The app will be available at `http://localhost:8080`

## Deploying to Hugging Face Spaces

### Quick Start

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose:
   - **Space name**: Choose a name (e.g., `oregon-tax-rates`)
   - **License**: Your choice
   - **SDK**: Docker
   - **Visibility**: Public or Private

4. Upload these files to your Space:
   - `explore_city_tax_data.py`
   - `FY 2024-25 Property Tax Statistics Supplement.xlsx`
   - `PSU_2024_Certified_Population_Estimates.xlsx`
   - `Dockerfile`

5. The Space will automatically build and deploy
6. Share the URL: `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

### Alternative: Git Method

```bash
# Clone your Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME

# Copy files
cp explore_city_tax_data.py .
cp "FY 2024-25 Property Tax Statistics Supplement.xlsx" .
cp "PSU_2024_Certified_Population_Estimates.xlsx" .
cp Dockerfile .

# Commit and push
git add .
git commit -m "Add Oregon tax rates app"
git push
```

## Deploying with Docker (Self-Hosted)

### Build Docker Image

```bash
docker build -t oregon-tax-rates .
```

### Run Container

```bash
docker run -p 8080:8080 oregon-tax-rates
```

Visit `http://localhost:8080`

### Deploy to Cloud

The Docker image can be deployed to:
- **Railway**: `railway up`
- **DigitalOcean App Platform**: Connect to Git repository
- **AWS ECS/Fargate**: Push to ECR and deploy
- **Google Cloud Run**: `gcloud run deploy`

## Adding Authentication

To add token-based authentication, update the `Dockerfile` CMD:

```dockerfile
CMD ["marimo", "run", "explore_city_tax_data.py", "--host", "0.0.0.0", "--port", "8080", "--token-password", "your-secret-token"]
```

Users access via: `http://your-app-url/?access_token=your-secret-token`

## Data Summary

- **Total Cities**: 233 Oregon incorporated cities
- **Match Rate**: 89.4% (207 cities with population data)
- **Total Population**: 2,751,061 residents
- **Average Tax Rate**: 16.1569 per $1,000 assessed value
- **Largest City**: Portland (639,448 population)

## Features

- Interactive data tables with sorting and filtering
- Summary statistics
- Tax rate breakdowns by:
  - County
  - City
  - School District
  - Other Districts
- 2024 population estimates
- Total assessed values by city

## File Structure

```
.
├── explore_city_tax_data.py          # Main marimo notebook
├── Dockerfile                         # Container configuration
├── .dockerignore                      # Docker ignore rules
├── FY 2024-25 Property Tax Statistics Supplement.xlsx
├── PSU_2024_Certified_Population_Estimates.xlsx
└── README.md                          # This file
```

## License

Data sources are publicly available from Oregon Department of Revenue and Portland State University Population Research Center.
