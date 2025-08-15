# Solve It With Code - Business Website

A professional, modern website for "Solve It With Code" - an ecosystem for creators who want to solve big problems with innovative code solutions.

## Features

- **Modern Design**: Clean, professional design with responsive layout
- **Multi-page Structure**: Home, About, Services, and Contact pages
- **Fast Performance**: Built with FastAPI and FastHTML for optimal speed
- **Responsive**: Mobile-friendly design that works on all devices
- **Professional Styling**: Modern CSS with smooth animations and hover effects
- **Contact Form**: Functional contact form for business inquiries

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: FastHTML with custom CSS
- **Styling**: Modern CSS with CSS variables and responsive design
- **Fonts**: Inter font family for professional typography

## Installation

1. **Clone or download** this repository to your local machine

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the website**:
   ```bash
   python main.py
   ```

4. **Open your browser** and navigate to `http://localhost:8000`

## Project Structure

```
SolveItWithCode/
├── main.py              # Main application file with all routes and components
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Website Pages

### Home Page (`/`)
- Hero section with compelling call-to-action
- Feature highlights showcasing business value
- Mission statement and company overview

### About Page (`/about`)
- Company history and founding story
- Core values and principles
- Team mission and vision

### Services Page (`/services`)
- Comprehensive service offerings
- Development support, deployment, education
- Community and networking opportunities

### Contact Page (`/contact`)
- Contact form for business inquiries
- Multiple contact methods
- Office location and business hours

### Live Dashboard (`/dashboard`)
- **Real-time coding statistics** with live updates every 30-45 seconds
- **Dynamic activity feed** showing community coding progress
- **Interactive stats cards** with random data generation
- **Modern dark theme** with glassmorphism design
- **HTMX-powered** for seamless updates without page refresh

## Customization

### Colors
The website uses CSS variables for easy color customization. Edit the `:root` section in the CSS to change the color scheme:

```css
:root {
    --primary-color: #2563eb;      /* Main brand color */
    --secondary-color: #1e40af;    /* Secondary brand color */
    --accent-color: #3b82f6;       /* Accent color */
    --text-color: #1f2937;         /* Main text color */
    --light-text: #6b7280;         /* Secondary text color */
    --background: #ffffff;          /* Background color */
    --light-bg: #f8fafc;           /* Light background color */
    --border: #e5e7eb;             /* Border color */
}
```

### Content
- Update business information in the respective page functions
- Modify contact details in the footer and contact page
- Customize service offerings and features

### Styling
- CSS is embedded in the main.py file for easy modification
- Responsive breakpoints are set at 768px for mobile devices
- Animations and hover effects can be customized in the CSS

## Development

### Adding New Pages
1. Create a new route function with the `@rt('/page-name')` decorator
2. Follow the existing page structure pattern
3. Include the navbar and footer components
4. Add the new page to the navigation menu

### Modifying Components
- **Navbar**: Edit the `navbar()` function
- **Footer**: Edit the `footer()` function
- **Styling**: Modify the CSS variables and styles

## Deployment

### Local Development
- Run with `python main.py`
- Access at `http://localhost:8000`

### Production Deployment
- Use a production WSGI server like Gunicorn
- Set up reverse proxy with Nginx
- Configure environment variables for production settings

## Business Information

**Company**: Solve It With Code  
**Tagline**: Empowering creators to solve big problems with code  
**Services**: Development support, deployment, education, community, funding  
**Contact**: hello@solveitwithcode.com  

## License

This project is proprietary software for Solve It With Code business use.

---

**Built with ❤️ using FastAPI and FastHTML** 