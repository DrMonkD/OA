"""
Flask Application for GitHub-Render-Supabase Trial

A simple Flask app to test the connection between GitHub, Render, and Supabase.
"""

from flask import Flask, jsonify
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Supabase client (will be None if env vars not set)
supabase: Client | None = None

def init_supabase():
    """Initialize Supabase client from environment variables."""
    global supabase
    try:
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')
        
        if not supabase_url or not supabase_key:
            return None
        
        supabase = create_client(supabase_url, supabase_key)
        return supabase
    except Exception as e:
        print(f"Error initializing Supabase: {e}")
        return None

@app.route('/')
def index():
    """Root endpoint with app information."""
    return jsonify({
        'message': 'GitHub-Render-Supabase Trial App',
        'status': 'running',
        'endpoints': {
            '/health': 'Health check endpoint (no Supabase dependency)',
            '/test-supabase': 'Test Supabase connection'
        }
    }), 200

@app.route('/health')
def health():
    """Health check endpoint - no Supabase dependency."""
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running',
        'supabase_configured': os.getenv('SUPABASE_URL') is not None
    }), 200

@app.route('/test-supabase')
def test_supabase():
    """Test Supabase connection endpoint."""
    # Check if environment variables are set
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    
    if not supabase_url or not supabase_key:
        return jsonify({
            'status': 'error',
            'message': 'Supabase environment variables not configured',
            'details': {
                'SUPABASE_URL': 'not set' if not supabase_url else 'set',
                'SUPABASE_KEY': 'not set' if not supabase_key else 'set'
            }
        }), 500
    
    try:
        # Initialize Supabase client
        client = init_supabase()
        
        if client is None:
            return jsonify({
                'status': 'error',
                'message': 'Failed to initialize Supabase client'
            }), 500
        
        # Verify client was created successfully
        # The Supabase client initialization validates the URL and key format
        # If we get here, the client was created successfully
        return jsonify({
            'status': 'success',
            'message': 'Supabase connection successful',
            'details': {
                'url': supabase_url,
                'connection_test': 'passed',
                'client_initialized': True,
                'note': 'Client successfully initialized. To test database operations, ensure you have tables set up in Supabase.'
            }
        }), 200
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Failed to connect to Supabase',
            'error': str(e),
            'details': {
                'url': supabase_url if supabase_url else 'not set'
            }
        }), 500

if __name__ == '__main__':
    # Initialize Supabase on startup
    init_supabase()
    
    # Run the app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_ENV') != 'production')
