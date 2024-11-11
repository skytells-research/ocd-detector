# Installation Guide

## System Requirements

### Software Requirements
- Python 3.8 or higher
  - Check version: `python --version`
  - [Download Python](https://www.python.org/downloads/)
- pip package manager
  - Check version: `pip --version`
  - Upgrade pip: `python -m pip install --upgrade pip`
- Node.js 16.x or higher (for frontend)
  - Check version: `node --version`
  - [Download Node.js](https://nodejs.org/)
- Tesseract OCR 4.0+ (for screenshot analysis)
  - Check version: `tesseract --version`

### Hardware Requirements
- Minimum 4GB RAM
- 2GB free disk space
- Internet connection for package installation

## Installation Steps

### 1. Clone the Repository
```bash
# Clone the main repository
git clone https://github.com/skytells-research/ocd-detector.git

# Navigate to project directory
cd ocd-detector

# If you want a specific version
git checkout v1.0.0  # Optional
```

### 2. Python Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
.\venv\Scripts\activate
# For Linux/Mac:
source venv/bin/activate

# Verify activation
which python  # Should point to your venv
```

### 3. Install Python Dependencies
```bash
# Update pip first
python -m pip install --upgrade pip

# Install development dependencies
pip install -r requirements-dev.txt

# Install project
python setup.py install

# Verify installation
python -c "import ocd_detector; print(ocd_detector.__version__)"
```

### 4. Install Tesseract OCR

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

# Fedora
sudo dnf install tesseract
sudo dnf install tesseract-devel
```

#### macOS
```bash
# Using Homebrew
brew install tesseract

# Optional language packs
brew install tesseract-lang
```

#### Windows
1. Download installer from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run installer (select additional languages if needed)
3. Add to PATH:
   - Add `C:\Program Files\Tesseract-OCR` to system PATH
   - Verify with: `tesseract --version`

### 5. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create .env file
cp .env.example .env

# Edit .env with your settings
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname
# API_KEY=your_api_key
# OTHER_SETTINGS=value

# Initialize database
python manage.py migrate

# Start backend server
uvicorn backend.main:app --reload --port 8000
```

### 6. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend-nextjs

# Install dependencies
npm install

# Create .env.local
cp .env.example .env.local

# Edit frontend environment variables
# NEXT_PUBLIC_API_URL=http://localhost:8000
# NEXT_PUBLIC_OTHER_VAR=value

# Start development server
npm run dev
```

## Verification
1. Backend API should be available at: `http://localhost:8000`
2. Frontend should be available at: `http://localhost:3000`
3. API documentation at: `http://localhost:8000/docs`

## Common Issues and Solutions

### Tesseract Installation Issues
- **Windows**: Ensure PATH is set correctly
- **Linux**: Try `sudo ldconfig` if library not found
- **Mac**: Run `brew doctor` to check Homebrew issues

### Database Connection Issues
1. Verify PostgreSQL is running
2. Check connection string in `.env`
3. Ensure database exists
4. Verify user permissions

### Node.js Issues
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and reinstall
- Update npm: `npm install -g npm@latest`

## Updating the Application
```bash
# Pull latest changes
git pull origin main

# Update Python dependencies
pip install -r requirements.txt

# Update frontend dependencies
cd frontend-nextjs
npm install

# Restart services
```

## Support
- Report issues: [GitHub Issues](https://github.com/skytells-research/ocd-detector/issues)
- Documentation: [Project Wiki](https://github.com/skytells-research/ocd-detector/wiki)
- Community: [Discussions](https://github.com/skytells-research/ocd-detector/discussions)

