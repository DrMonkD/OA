# GitHub-Render-Supabase Trial App

A minimal Flask application to test the integration between GitHub, Render, and Supabase. This project serves as a trial to verify that the deployment pipeline works correctly.

## Features

- Simple Flask web server with health check endpoint
- Supabase connection testing endpoint
- Ready for deployment on Render
- Environment variable configuration
- Clear error messages for debugging

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment configuration
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Local Development Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Supabase account and project

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your Supabase credentials:
     ```env
     SUPABASE_URL=https://your-project-id.supabase.co
     SUPABASE_KEY=your-anon-key-here
     ```

5. Run the application:
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## API Endpoints

### `GET /`
Returns basic information about the application.

**Response:**
```json
{
  "message": "GitHub-Render-Supabase Trial App",
  "status": "running",
  "endpoints": {
    "/health": "Health check endpoint (no Supabase dependency)",
    "/test-supabase": "Test Supabase connection"
  }
}
```

### `GET /health`
Health check endpoint that doesn't require Supabase connection.

**Response:**
```json
{
  "status": "healthy",
  "message": "Application is running",
  "supabase_configured": true
}
```

### `GET /test-supabase`
Tests the connection to Supabase and performs a simple query.

**Success Response:**
```json
{
  "status": "success",
  "message": "Supabase connection successful",
  "details": {
    "url": "https://your-project.supabase.co",
    "connection_test": "passed",
    "query_test": "passed"
  }
}
```

**Error Response:**
```json
{
  "status": "error",
  "message": "Failed to connect to Supabase",
  "error": "error details"
}
```

## Render Deployment

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Initialize git and push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 2: Connect to Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" and select "Web Service"
3. Connect your GitHub account if not already connected
4. Select your repository
5. Render will auto-detect the configuration from `render.yaml`

### Step 3: Configure Environment Variables

In the Render dashboard, go to your service's "Environment" tab and add:

- `SUPABASE_URL` - Your Supabase project URL (e.g., `https://xxxxx.supabase.co`)
- `SUPABASE_KEY` - Your Supabase anon/public key
- `FLASK_ENV` - Set to `production` (this is already in render.yaml, but you can override if needed)

**How to get Supabase credentials:**
1. Go to your [Supabase Dashboard](https://app.supabase.com)
2. Select your project
3. Go to Settings → API
4. Copy the "Project URL" for `SUPABASE_URL`
5. Copy the "anon public" key for `SUPABASE_KEY`

### Step 4: Deploy

1. Click "Create Web Service" or "Save Changes"
2. Render will automatically:
   - Build your application
   - Install dependencies
   - Start the service
3. Wait for the deployment to complete
4. Your app will be available at `https://your-app-name.onrender.com`

### Step 5: Test

Once deployed, test the endpoints:

- Health check: `https://your-app-name.onrender.com/health`
- Supabase test: `https://your-app-name.onrender.com/test-supabase`

## Troubleshooting

### Supabase Connection Issues

1. **Check environment variables**: Ensure `SUPABASE_URL` and `SUPABASE_KEY` are set correctly in Render
2. **Verify Supabase project**: Make sure your Supabase project is active and accessible
3. **Check logs**: View Render logs to see detailed error messages
4. **Test locally**: Run the app locally with the same environment variables to isolate issues

### Render Deployment Issues

1. **Build failures**: Check that all dependencies in `requirements.txt` are correct
2. **Start command**: Verify `gunicorn app:app` works locally
3. **Health check**: Ensure `/health` endpoint returns 200 OK
4. **Port configuration**: Render automatically sets the PORT environment variable

### Common Errors

- **"Supabase environment variables not configured"**: Add `SUPABASE_URL` and `SUPABASE_KEY` in Render dashboard
- **"Failed to initialize Supabase client"**: Check that your Supabase URL and key are correct
- **"Connection timeout"**: Verify your Supabase project is active and network connectivity

## Next Steps

Once this trial app is working:

1. Verify all endpoints respond correctly
2. Check Render logs for any warnings
3. Test Supabase connection multiple times to ensure stability
4. Use this as a template for your main application

## License

This is a trial/test project. Use as needed.
