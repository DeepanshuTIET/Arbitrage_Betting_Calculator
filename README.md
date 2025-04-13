# Arbitrage Betting Calculator

A professional-grade arbitrage betting calculator built with Flask, Tailwind CSS, and Daisy UI.

## Features

- Calculate whether two odds present an arbitrage opportunity
- Determine optimal stake distribution for maximum profit
- Calculate guaranteed profit and ROI
- Clean, responsive UI that works on all devices

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python run.py
   ```
   
## Deploying to Vercel

This application is configured for deployment on Vercel's serverless platform.

### Deployment Steps

1. Install Vercel CLI (if you haven't already):
   ```
   npm install -g vercel
   ```

2. Login to Vercel:
   ```
   vercel login
   ```

3. Deploy the application:
   ```
   vercel
   ```

4. For production deployment:
   ```
   vercel --prod
   ```

### Important Files for Vercel Deployment

- `vercel.json`: Configures the Vercel deployment
- `api/index.py`: Entry point for the serverless function
- `requirements.txt`: Python dependencies

## Project Structure

```
arb-calculator/
├── api/
│   ├── __init__.py
│   └── index.py        # Vercel serverless entry point
├── app/
│   ├── __init__.py
│   ├── calculator.py   # Core calculation logic
│   ├── forms.py        # Form definitions
│   ├── static/         # Static assets
│   └── templates/      # HTML templates
├── .env                # Environment variables
├── .gitignore
├── README.md
├── requirements.txt    # Python dependencies
├── run.py              # Local development entry point
└── vercel.json         # Vercel configuration
```

## How It Works

1. Enter the odds for if a team wins
2. Enter the odds for if a team loses
3. Enter your total bankroll
4. The calculator will determine if there's an arbitrage opportunity
5. If an opportunity exists, it will show you how to distribute your stakes for guaranteed profit
