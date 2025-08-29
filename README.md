# Arbitrage Betting Calculator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-green.svg)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0+-38B2AC.svg)](https://tailwindcss.com/)
[![DaisyUI](https://img.shields.io/badge/DaisyUI-3.0+-5A0EF8.svg)](https://daisyui.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-000000.svg)](https://red-carpet-nine.vercel.app)

A professional-grade arbitrage betting calculator built with Flask, Tailwind CSS, and Daisy UI. This tool helps users identify profitable arbitrage opportunities in sports betting by calculating optimal stake distributions for guaranteed profits.

## 🌟 Features

- **Arbitrage Detection**: Automatically identifies when two odds present an arbitrage opportunity
- **Optimal Stake Calculation**: Determines the best stake distribution for maximum guaranteed profit
- **Profit Analysis**: Calculates guaranteed profit and Return on Investment (ROI)
- **Responsive Design**: Clean, modern UI that works seamlessly on desktop, tablet, and mobile devices
- **Real-time Calculations**: Instant results with no page refresh required
- **User-friendly Interface**: Intuitive design with clear input fields and results display

## 🚀 Live Demo

Visit the live application: **[red-carpet-nine.vercel.app](https://red-carpet-nine.vercel.app)**

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DeepanshuTIET/Arbitrage_Betting_Calculator.git
cd Arbitrage_Betting_Calculator
```

### 2. Create Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python run.py
```

The application will be available at `http://localhost:5000`

## 🎯 How It Works

### Arbitrage Betting Explained

Arbitrage betting (or "arbing") is a betting strategy that takes advantage of price differences between bookmakers. When different bookmakers offer different odds for the same event, you can place bets on all possible outcomes and guarantee a profit regardless of the result.

### Using the Calculator

1. **Enter the odds for Team A winning** (e.g., 2.50)
2. **Enter the odds for Team B winning** (e.g., 1.80)
3. **Enter your total bankroll** (e.g., $1000)
4. **Click "Calculate"** to analyze the opportunity
5. **Review the results**:
   - Whether an arbitrage opportunity exists
   - Optimal stake distribution
   - Guaranteed profit amount
   - Return on Investment percentage

### Example Calculation

| Input       | Value |
| ----------- | ----- |
| Team A Odds | 2.50  |
| Team B Odds | 1.80  |
| Bankroll    | $1000 |

**Result**:

- ✅ Arbitrage opportunity found
- Stake on Team A: $419.05
- Stake on Team B: $580.95
- Guaranteed profit: $20.00
- ROI: 2%

## 🏗️ Project Structure

```
arbitrage-betting-calculator/
├── api/
│   ├── __init__.py
│   └── index.py              # Vercel serverless entry point
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── calculator.py         # Core arbitrage calculation logic
│   ├── forms.py              # Form definitions and validation
│   ├── routes.py             # Flask routes and views
│   ├── static/               # Static assets (CSS, JS, images)
│   └── templates/            # HTML templates
├── .env                      # Environment variables
├── .gitignore               # Git ignore rules
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── run.py                   # Local development entry point
└── vercel.json             # Vercel deployment configuration
```

## 🚀 Deployment

### Deploying to Vercel

This application is pre-configured for deployment on Vercel's serverless platform.

#### Prerequisites

1. **Node.js** installed on your system
2. **Vercel CLI** installed globally

#### Deployment Steps

1. **Install Vercel CLI** (if not already installed):

   ```bash
   npm install -g vercel
   ```
2. **Login to Vercel**:

   ```bash
   vercel login
   ```
3. **Deploy the application**:

   ```bash
   vercel
   ```
4. **For production deployment**:

   ```bash
   vercel --prod
   ```

#### Important Files for Vercel Deployment

- `vercel.json`: Configures the Vercel deployment settings
- `api/index.py`: Entry point for the serverless function
- `requirements.txt`: Python dependencies for the serverless environment

### Alternative Deployment Options

- **Heroku**: Add a `Procfile` and configure buildpacks
- **PythonAnywhere**: Upload files and configure WSGI
- **DigitalOcean App Platform**: Use the provided configuration files

## 🛠️ Technology Stack

### Backend

- **Flask 3.1.0**: Lightweight web framework
- **Flask-WTF 1.2.2**: Form handling and CSRF protection
- **Python-dotenv 1.1.0**: Environment variable management
- **Werkzeug 1.1.3**: WSGI utility library

### Frontend

- **Tailwind CSS**: Utility-first CSS framework
- **DaisyUI**: Component library for Tailwind CSS
- **HTML5**: Semantic markup
- **JavaScript**: Interactive functionality

### Deployment

- **Vercel**: Serverless deployment platform
- **Python 3.8+**: Runtime environment

## 📊 Dependencies

```
flask==3.1.0
flask-wtf==1.2.2
python-dotenv==1.1.0
werkzeug==3.1.3
jinja2==3.1.6
itsdangerous==2.2.0
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. Please ensure you comply with all local laws and regulations regarding sports betting. The developers are not responsible for any financial losses incurred through the use of this calculator.

## 📞 Support

If you encounter any issues or have questions:

- **Open an Issue**: [GitHub Issues](https://github.com/DeepanshuTIET/Arbitrage_Betting_Calculator/issues)
- **Email**: [Your Email]
- **Live Demo**: [red-carpet-nine.vercel.app](https://red-carpet-nine.vercel.app)

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- Tailwind CSS team for the utility-first CSS framework
- DaisyUI for the beautiful component library
- Vercel for the seamless deployment platform

---

**Made with ❤️ by [Deepanshu Goyal](https://github.com/DeepanshuTIET)**

[![GitHub](https://img.shields.io/badge/GitHub-DeepanshuTIET-181717.svg?logo=github)](https://github.com/DeepanshuTIET)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Deepanshu%20Goyal-0077B5.svg?logo=linkedin)](https://linkedin.com/in/deepanshu-goyal)
