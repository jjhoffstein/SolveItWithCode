from fasthtml.common import *
from fasthtml import EventStream
import json
import random
import time

app, rt = fast_app()

@rt('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Solve It With Code - Empowering Creators with Code Solutions</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #1f2937;
                background: #ffffff;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 1rem;
            }
            
            .navbar {
                background: #ffffff;
                border-bottom: 1px solid #e5e7eb;
                position: sticky;
                top: 0;
                z-index: 100;
                padding: 1rem 0;
            }
            
            .nav-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .logo {
                font-size: 1.5rem;
                font-weight: 700;
                color: #2563eb;
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
                list-style: none;
            }
            
            .nav-links a {
                text-decoration: none;
                color: #1f2937;
                font-weight: 500;
                transition: color 0.2s;
            }
            
            .nav-links a:hover {
                color: #2563eb;
            }
            
            .hero {
                background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
                color: white;
                padding: 6rem 0;
                text-align: center;
            }
            
            .hero h1 {
                font-size: 3.5rem;
                font-weight: 800;
                margin-bottom: 1.5rem;
                line-height: 1.2;
            }
            
            .hero p {
                font-size: 1.25rem;
                margin-bottom: 2rem;
                opacity: 0.9;
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
            }
            
            .cta-button {
                display: inline-block;
                background: white;
                color: #2563eb;
                padding: 1rem 2rem;
                border-radius: 0.5rem;
                text-decoration: none;
                font-weight: 600;
                font-size: 1.1rem;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            .cta-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            }
            
            .section {
                padding: 5rem 0;
            }
            
            .section:nth-child(even) {
                background: #f8fafc;
            }
            
            .section h2 {
                font-size: 2.5rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 3rem;
                color: #1f2937;
            }
            
            .section p {
                font-size: 1.1rem;
                color: #6b7280;
                max-width: 800px;
                margin: 0 auto 2rem;
                text-align: center;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .feature-card {
                background: white;
                padding: 2rem;
                border-radius: 1rem;
                border: 1px solid #e5e7eb;
                text-align: center;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            }
            
            .feature-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            
            .feature-card h3 {
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                color: #1f2937;
            }
            
            .feature-card p {
                color: #6b7280;
                text-align: left;
            }
            
            .footer {
                background: #1f2937;
                color: white;
                padding: 3rem 0;
                text-align: center;
            }
            
            .footer-content {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                margin-bottom: 2rem;
            }
            
            .footer-section h3 {
                margin-bottom: 1rem;
                color: #3b82f6;
            }
            
            .footer-section p, .footer-section a {
                color: #9ca3af;
                text-decoration: none;
                line-height: 1.8;
            }
            
            .footer-section a:hover {
                color: white;
            }
            
            .footer-bottom {
                border-top: 1px solid #374151;
                padding-top: 2rem;
                color: #9ca3af;
            }
            
            @media (max-width: 768px) {
                .hero h1 {
                    font-size: 2.5rem;
                }
                
                .nav-links {
                    display: none;
                }
                
                .features-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div class="container">
                <div class="nav-content">
                    <a href="/" class="logo">Solve It With Code</a>
                    <ul class="nav-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/services">Services</a></li>
                        <li><a href="/contact">Contact</a></li>
                        <li><a href="/dashboard">Dashboard</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <section class="hero">
            <div class="container">
                <h1>Solve Big Problems</h1>
                <p>Join the ecosystem for creators who want to solve big problems with code. Build, innovate, and make a difference.</p>
                <a href="/contact" class="cta-button">Get Started</a>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <h2>Why Choose Solve It With Code?</h2>
                <p>We're building the future where every creator has the tools, community, and support they need to tackle the world's biggest challenges through code.</p>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🚀</div>
                        <h3>Innovation First</h3>
                        <p>We believe in pushing boundaries and thinking outside the box. Our platform encourages creative problem-solving approaches.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🤝</div>
                        <h3>Community Driven</h3>
                        <p>Connect with like-minded creators, share knowledge, and collaborate on groundbreaking projects.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">💡</div>
                        <h3>Expert Support</h3>
                        <p>Access to industry experts, mentors, and resources to help you succeed in your coding journey.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <h2>Our Mission</h2>
                <p>To democratize problem-solving through code, making advanced technology accessible to creators everywhere. We envision a world where anyone with a great idea can build the solution.</p>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🎯</div>
                        <h3>Accessibility</h3>
                        <p>Breaking down barriers to entry in the tech world, making coding and problem-solving accessible to all.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🌍</div>
                        <h3>Global Impact</h3>
                        <p>Supporting creators worldwide to solve local and global challenges through innovative code solutions.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔬</div>
                        <h3>Research & Development</h3>
                        <p>Investing in cutting-edge technologies and methodologies to stay ahead of the curve.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>Solve It With Code</h3>
                        <p>Empowering creators to solve big problems with innovative code solutions.</p>
                    </div>
                    <div class="footer-section">
                        <h3>Quick Links</h3>
                        <p><a href="/">Home</a></p>
                        <p><a href="/about">About</a></p>
                        <p><a href="/services">Services</a></p>
                        <p><a href="/contact">Contact</a></p>
                    </div>
                    <div class="footer-section">
                        <h3>Contact Info</h3>
                        <p>Email: hello@solveitwithcode.com</p>
                        <p>Phone: +1 (555) 123-4567</p>
                        <p>Location: San Francisco, CA</p>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>© 2024 Solve It With Code. All rights reserved.</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """

@rt('/about')
def about():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us - Solve It With Code</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #1f2937;
                background: #ffffff;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 1rem;
            }
            
            .navbar {
                background: #ffffff;
                border-bottom: 1px solid #e5e7eb;
                position: sticky;
                top: 0;
                z-index: 100;
                padding: 1rem 0;
            }
            
            .nav-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .logo {
                font-size: 1.5rem;
                font-weight: 700;
                color: #2563eb;
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
                list-style: none;
            }
            
            .nav-links a {
                text-decoration: none;
                color: #1f2937;
                font-weight: 500;
                transition: color 0.2s;
            }
            
            .nav-links a:hover {
                color: #2563eb;
            }
            
            .section {
                padding: 5rem 0;
            }
            
            .section:nth-child(even) {
                background: #f8fafc;
            }
            
            .section h1 {
                font-size: 3rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 2rem;
                color: #2563eb;
            }
            
            .section h2 {
                font-size: 2.5rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 3rem;
                color: #1f2937;
            }
            
            .section p {
                font-size: 1.1rem;
                color: #6b7280;
                max-width: 800px;
                margin: 0 auto 2rem;
                text-align: center;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .feature-card {
                background: white;
                padding: 2rem;
                border-radius: 1rem;
                border: 1px solid #e5e7eb;
                text-align: center;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            }
            
            .feature-card h3 {
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                color: #1f2937;
            }
            
            .feature-card p {
                color: #6b7280;
                text-align: left;
            }
            
            .footer {
                background: #1f2937;
                color: white;
                padding: 3rem 0;
                text-align: center;
            }
            
            .footer-content {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                margin-bottom: 2rem;
            }
            
            .footer-section h3 {
                margin-bottom: 1rem;
                color: #3b82f6;
            }
            
            .footer-section p, .footer-section a {
                color: #9ca3af;
                text-decoration: none;
                line-height: 1.8;
            }
            
            .footer-section a:hover {
                color: white;
            }
            
            .footer-bottom {
                border-top: 1px solid #374151;
                padding-top: 2rem;
                color: #9ca3af;
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div class="container">
                <div class="nav-content">
                    <a href="/" class="logo">Solve It With Code</a>
                    <ul class="nav-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/services">Services</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <section class="section">
            <div class="container">
                <h1>About Solve It With Code</h1>
                <p>Founded in 2024, Solve It With Code emerged from a simple yet powerful belief: that the world's biggest problems can be solved through innovative code and the collective creativity of passionate developers.</p>
                <p>Our journey began when our founders recognized that while technology was advancing rapidly, many brilliant creators lacked the ecosystem, resources, and community support needed to turn their ideas into impactful solutions.</p>
                <p>Today, we're proud to serve as a comprehensive platform that bridges this gap, offering everything from educational resources and mentorship to collaborative tools and funding opportunities.</p>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <h2>Our Values</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>Innovation</h3>
                        <p>We constantly push the boundaries of what's possible, encouraging our community to think beyond conventional solutions.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Collaboration</h3>
                        <p>We believe that the best solutions come from diverse teams working together towards a common goal.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Impact</h3>
                        <p>Every project we support must have the potential to create meaningful, positive change in the world.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Learning</h3>
                        <p>We foster a culture of continuous learning and knowledge sharing among our community members.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>Solve It With Code</h3>
                        <p>Empowering creators to solve big problems with innovative code solutions.</p>
                    </div>
                    <div class="footer-section">
                        <h3>Quick Links</h3>
                        <p><a href="/">Home</a></p>
                        <p><a href="/about">About</a></p>
                        <p><a href="/services">Services</a></p>
                        <p><a href="/contact">Contact</a></p>
                    </div>
                    <div class="footer-section">
                        <h3>Contact Info</h3>
                        <p>Email: hello@solveitwithcode.com</p>
                        <p>Phone: +1 (555) 123-4567</p>
                        <p>Location: San Francisco, CA</p>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>© 2024 Solve It With Code. All rights reserved.</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """

@rt('/services')
def services():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Our Services - Solve It With Code</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #1f2937;
                background: #ffffff;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 1rem;
            }
            
            .navbar {
                background: #ffffff;
                border-bottom: 1px solid #e5e7eb;
                position: sticky;
                top: 0;
                z-index: 100;
                padding: 1rem 0;
            }
            
            .nav-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .logo {
                font-size: 1.5rem;
                font-weight: 700;
                color: #2563eb;
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
                list-style: none;
            }
            
            .nav-links a {
                text-decoration: none;
                color: #1f2937;
                font-weight: 500;
                transition: color 0.2s;
            }
            
            .nav-links a:hover {
                color: #2563eb;
            }
            
            .section {
                padding: 5rem 0;
            }
            
            .section:nth-child(even) {
                background: #f8fafc;
            }
            
            .section h1 {
                font-size: 3rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 2rem;
                color: #2563eb;
            }
            
            .section h2 {
                font-size: 2.5rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 3rem;
                color: #1f2937;
            }
            
            .section p {
                font-size: 1.1rem;
                color: #6b7280;
                max-width: 800px;
                margin: 0 auto 2rem;
                text-align: center;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .feature-card {
                background: white;
                padding: 2rem;
                border-radius: 1rem;
                border: 1px solid #e5e7eb;
                text-align: center;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            }
            
            .feature-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            
            .feature-card h3 {
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                color: #1f2937;
            }
            
            .feature-card p {
                color: #6b7280;
                text-align: left;
            }
            
            .footer {
                background: #1f2937;
                color: white;
                padding: 3rem 0;
                text-align: center;
            }
            
            .footer-content {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                margin-bottom: 2rem;
            }
            
            .footer-section h3 {
                margin-bottom: 1rem;
                color: #3b82f6;
            }
            
            .footer-section p, .footer-section a {
                color: #9ca3af;
                text-decoration: none;
                line-height: 1.8;
            }
            
            .footer-section a:hover {
                color: white;
            }
            
            .footer-bottom {
                border-top: 1px solid #374151;
                padding-top: 2rem;
                color: #9ca3af;
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div class="container">
                <div class="nav-content">
                    <a href="/" class="logo">Solve It With Code</a>
                    <ul class="nav-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/services">Services</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <section class="section">
            <div class="container">
                <h1>Our Services</h1>
                <p>We provide a comprehensive suite of services designed to support creators at every stage of their journey, from initial concept to global deployment.</p>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <h2>Core Services</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">💻</div>
                        <h3>Development Support</h3>
                        <p>Expert guidance, code reviews, and technical mentorship to help you build robust, scalable solutions.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🚀</div>
                        <h3>Deployment & Scaling</h3>
                        <p>Infrastructure support, cloud deployment, and scaling strategies to ensure your solution reaches its full potential.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">📚</div>
                        <h3>Educational Resources</h3>
                        <p>Comprehensive learning materials, workshops, and training programs to enhance your technical skills.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🤝</div>
                        <h3>Community & Networking</h3>
                        <p>Connect with fellow creators, industry experts, and potential collaborators through our vibrant community.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">💰</div>
                        <h3>Funding & Resources</h3>
                        <p>Access to funding opportunities, grants, and resources to help bring your ideas to life.</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">📊</div>
                        <h3>Analytics & Insights</h3>
                        <p>Data-driven insights and analytics to help you understand your solution's impact and optimize performance.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>Solve It With Code</h3>
                        <p>Empowering creators to solve big problems with innovative code solutions.</p>
                    </div>
                    <div class="footer-section">
                        <h3>Quick Links</h3>
                        <p><a href="/">Home</a></p>
                        <p><a href="/about">About</a></p>
                        <p><a href="/services">Services</a></p>
                        <p><a href="/contact">Contact</a></p>
                    </div>
                    <div class="footer-section">
                        <h3>Contact Info</h3>
                        <p>Email: hello@solveitwithcode.com</p>
                        <p>Phone: +1 (555) 123-4567</p>
                        <p>Location: San Francisco, CA</p>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>© 2024 Solve It With Code. All rights reserved.</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """

@rt('/contact')
def contact():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us - Solve It With Code</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #1f2937;
                background: #ffffff;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 1rem;
            }
            
            .navbar {
                background: #ffffff;
                border-bottom: 1px solid #e5e7eb;
                position: sticky;
                top: 0;
                z-index: 100;
                padding: 1rem 0;
            }
            
            .nav-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .logo {
                font-size: 1.5rem;
                font-weight: 700;
                color: #2563eb;
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
                list-style: none;
            }
            
            .nav-links a {
                text-decoration: none;
                color: #1f2937;
                font-weight: 500;
                transition: color 0.2s;
            }
            
            .nav-links a:hover {
                color: #2563eb;
            }
            
            .section {
                padding: 5rem 0;
            }
            
            .section:nth-child(even) {
                background: #f8fafc;
            }
            
            .section h1 {
                font-size: 3rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 2rem;
                color: #2563eb;
            }
            
            .section h2 {
                font-size: 2.5rem;
                font-weight: 700;
                text-align: center;
                margin-bottom: 3rem;
                color: #1f2937;
            }
            
            .section p {
                font-size: 1.1rem;
                color: #6b7280;
                max-width: 800px;
                margin: 0 auto 2rem;
                text-align: center;
            }
            
            .contact-form {
                max-width: 600px;
                margin: 0 auto;
                background: white;
                padding: 2rem;
                border-radius: 1rem;
                border: 1px solid #e5e7eb;
            }
            
            .form-group {
                margin-bottom: 1.5rem;
            }
            
            .form-group label {
                display: block;
                margin-bottom: 0.5rem;
                font-weight: 500;
                color: #1f2937;
            }
            
            .form-group input,
            .form-group textarea {
                width: 100%;
                padding: 0.75rem;
                border: 1px solid #e5e7eb;
                border-radius: 0.5rem;
                font-size: 1rem;
                font-family: inherit;
            }
            
            .form-group textarea {
                resize: vertical;
                min-height: 120px;
            }
            
            .submit-btn {
                background: #2563eb;
                color: white;
                padding: 1rem 2rem;
                border: none;
                border-radius: 0.5rem;
                font-size: 1.1rem;
                font-weight: 600;
                cursor: pointer;
                width: 100%;
                transition: background-color 0.2s;
            }
            
            .submit-btn:hover {
                background: #1e40af;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .feature-card {
                background: white;
                padding: 2rem;
                border-radius: 1rem;
                border: 1px solid #e5e7eb;
                text-align: center;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            }
            
            .feature-card h3 {
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
                color: #1f2937;
            }
            
            .feature-card p {
                color: #6b7280;
                text-align: left;
            }
            
            .footer {
                background: #1f2937;
                color: white;
                padding: 3rem 0;
                text-align: center;
            }
            
            .footer-content {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                margin-bottom: 2rem;
            }
            
            .footer-section h3 {
                margin-bottom: 1rem;
                color: #3b82f6;
            }
            
            .footer-section p, .footer-section a {
                color: #9ca3af;
                text-decoration: none;
                line-height: 1.8;
            }
            
            .footer-section a:hover {
                color: white;
            }
            
            .footer-bottom {
                border-top: 1px solid #374151;
                padding-top: 2rem;
                color: #9ca3af;
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div class="container">
                <div class="nav-content">
                    <a href="/" class="logo">Solve It With Code</a>
                    <ul class="nav-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/services">Services</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <section class="section">
            <div class="container">
                <h1>Get In Touch</h1>
                <p>Ready to start solving big problems with code? We'd love to hear from you and help you get started on your journey.</p>
                <form class="contact-form">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="submit-btn">Send Message</button>
                </form>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <h2>Other Ways to Connect</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>Email</h3>
                        <p>hello@solveitwithcode.com</p>
                        <p>We typically respond within 24 hours.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Phone</h3>
                        <p>+1 (555) 123-4567</p>
                        <p>Available Monday-Friday, 9 AM - 6 PM PST.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Office</h3>
                        <p>123 Innovation Drive</p>
                        <p>San Francisco, CA 94105</p>
                    </div>
                </div>
            </div>
        </section>
        
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>Solve It With Code</h3>
                        <p>Empowering creators to solve big problems with innovative code solutions.</p>
                    </div>
                    <div class="footer-section">
                        <h3>Quick Links</h3>
                        <p><a href="/">Home</a></p>
                        <p><a href="/about">About</a></p>
                        <p><a href="/services">Services</a></p>
                        <p><a href="/contact">Contact</a></p>
                    </div>
                    <div class="footer-section">
                        <h3>Contact Info</h3>
                        <p>Email: hello@solveitwithcode.com</p>
                        <p>Phone: +1 (555) 123-4567</p>
                        <p>Location: San Francisco, CA</p>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>© 2024 Solve It With Code. All rights reserved.</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """

@rt('/dashboard')
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Live Coding Dashboard - Solve It With Code</title>
        <script src="https://unpkg.com/htmx.org@1.9.10"></script>
        <script src="https://cdn.jsdelivr.net/npm/htmx-ext-loading-states@2.0.1/loading-states.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/htmx-ext-class-tools@2.0.1/class-tools.js"></script>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #1f2937;
                background: #0f172a;
                color: white;
            }
            
            .container {
                max-width: 1400px;
                margin: 0 auto;
                padding: 0 1rem;
            }
            
            .navbar {
                background: rgba(15, 23, 42, 0.9);
                border-bottom: 1px solid #334155;
                position: sticky;
                top: 0;
                z-index: 100;
                padding: 1rem 0;
                backdrop-filter: blur(10px);
            }
            
            .nav-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .logo {
                font-size: 1.5rem;
                font-weight: 700;
                color: #3b82f6;
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
                list-style: none;
            }
            
            .nav-links a {
                text-decoration: none;
                color: #e2e8f0;
                font-weight: 500;
                transition: color 0.2s;
            }
            
            .nav-links a:hover {
                color: #3b82f6;
            }
            
            .dashboard-header {
                text-align: center;
                padding: 3rem 0;
                background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
                margin-bottom: 2rem;
            }
            
            .dashboard-header h1 {
                font-size: 3rem;
                font-weight: 800;
                margin-bottom: 1rem;
            }
            
            .dashboard-header p {
                font-size: 1.2rem;
                opacity: 0.9;
            }
            
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-bottom: 3rem;
            }
            
            .stat-card {
                background: rgba(30, 41, 59, 0.8);
                border: 1px solid #475569;
                border-radius: 1rem;
                padding: 2rem;
                text-align: center;
                transition: transform 0.2s, box-shadow 0.2s;
                backdrop-filter: blur(10px);
            }
            
            .stat-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
                border-color: #3b82f6;
            }
            
            .stat-number {
                font-size: 3rem;
                font-weight: 800;
                color: #3b82f6;
                margin-bottom: 0.5rem;
                font-family: 'Courier New', monospace;
            }
            
            .stat-label {
                font-size: 1.1rem;
                color: #cbd5e1;
                margin-bottom: 1rem;
            }
            
            .stat-change {
                font-size: 0.9rem;
                padding: 0.25rem 0.75rem;
                border-radius: 1rem;
                display: inline-block;
            }
            
            .stat-change.positive {
                background: rgba(34, 197, 94, 0.2);
                color: #22c55e;
                border: 1px solid rgba(34, 197, 94, 0.3);
            }
            
            .stat-change.negative {
                background: rgba(239, 68, 68, 0.2);
                color: #ef4444;
                border: 1px solid rgba(239, 68, 68, 0.3);
            }
            
            .live-activity {
                background: rgba(30, 41, 59, 0.8);
                border: 1px solid #475569;
                border-radius: 1rem;
                padding: 2rem;
                margin-bottom: 2rem;
                backdrop-filter: blur(10px);
            }
            
            .live-activity h2 {
                font-size: 1.8rem;
                margin-bottom: 1.5rem;
                color: #3b82f6;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            
            .activity-item {
                display: flex;
                align-items: center;
                gap: 1rem;
                padding: 1rem;
                background: rgba(51, 65, 85, 0.5);
                border-radius: 0.5rem;
                margin-bottom: 0.5rem;
                border-left: 4px solid #3b82f6;
                animation: slideIn 0.3s ease-out;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateX(-20px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
            
            .activity-icon {
                font-size: 1.5rem;
                width: 40px;
                text-align: center;
            }
            
            .activity-content {
                flex: 1;
            }
            
            .activity-text {
                color: #e2e8f0;
                margin-bottom: 0.25rem;
            }
            
            .activity-time {
                font-size: 0.8rem;
                color: #94a3b8;
            }
            
            .pulse {
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            .footer {
                background: rgba(15, 23, 42, 0.9);
                border-top: 1px solid #334155;
                padding: 2rem 0;
                text-align: center;
                margin-top: 3rem;
            }
            
            .footer-content {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                margin-bottom: 2rem;
            }
            
            .footer-section h3 {
                margin-bottom: 1rem;
                color: #3b82f6;
            }
            
            .footer-section p, .footer-section a {
                color: #94a3b8;
                text-decoration: none;
                line-height: 1.8;
            }
            
            .footer-section a:hover {
                color: #3b82f6;
            }
            
            .footer-bottom {
                border-top: 1px solid #334155;
                padding-top: 2rem;
                color: #94a3b8;
            }
            
            .refresh-btn {
                background: #3b82f6;
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 0.5rem;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: background-color 0.2s;
                margin-bottom: 2rem;
            }
            
            .refresh-btn:hover {
                background: #2563eb;
            }
            
            .refresh-btn:disabled {
                background: #64748b;
                cursor: not-allowed;
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div class="container">
                <div class="nav-content">
                    <a href="/" class="logo">Solve It With Code</a>
                    <ul class="nav-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/services">Services</a></li>
                        <li><a href="/contact">Contact</a></li>
                        <li><a href="/dashboard" style="color: #3b82f6;">Dashboard</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        
                    <div class="dashboard-header">
                <div class="container">
                    <h1>🚀 Live Coding Dashboard</h1>
                    <p>Real-time insights into our community's coding activity and problem-solving progress</p>
                    <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.8;">
                        <span class="pulse">🔴</span> Live updates every 30-45 seconds
                    </div>
                </div>
            </div>
        
        <div class="container">
            <button class="refresh-btn" hx-get="/live-stats" hx-target="#stats-container" hx-swap="innerHTML">
                🔄 Refresh Stats
            </button>
            
            <script>
                // Auto-refresh stats every 30 seconds
                setInterval(function() {
                    htmx.ajax('GET', '/live-stats', {target: '#stats-container', swap: 'innerHTML'});
                }, 30000);
                
                // Auto-refresh activity every 45 seconds
                setInterval(function() {
                    htmx.ajax('GET', '/live-activity', {target: '#activity-feed', swap: 'innerHTML'});
                }, 45000);
            </script>
            
            <div id="stats-container" class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">1,247</div>
                    <div class="stat-label">Active Coders</div>
                    <div class="stat-change positive">+23 today</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">89</div>
                    <div class="stat-label">Problems Solved</div>
                    <div class="stat-change positive">+5 this week</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">2.4M</div>
                    <div class="stat-label">Lines of Code</div>
                    <div class="stat-change positive">+156K today</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">47</div>
                    <div class="stat-label">Active Projects</div>
                    <div class="stat-change positive">+3 new</div>
                </div>
            </div>
            
            <div class="live-activity">
                <h2>
                    <span class="pulse">🔴</span>
                    Live Activity Feed
                </h2>
                <div id="activity-feed">
                    <div class="activity-item">
                        <div class="activity-icon">💻</div>
                        <div class="activity-content">
                            <div class="activity-text">Sarah M. deployed solution for climate data analysis</div>
                            <div class="activity-time">2 minutes ago</div>
                        </div>
                    </div>
                    <div class="activity-item">
                        <div class="activity-icon">🚀</div>
                        <div class="activity-content">
                            <div class="activity-text">Team Alpha completed blockchain verification system</div>
                            <div class="activity-time">5 minutes ago</div>
                        </div>
                    </div>
                    <div class="activity-item">
                        <div class="activity-icon">🔬</div>
                        <div class="activity-content">
                            <div class="activity-text">New AI model trained for medical diagnosis</div>
                            <div class="activity-time">8 minutes ago</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>Solve It With Code</h3>
                        <p>Empowering creators to solve big problems with innovative code solutions.</p>
                    </div>
                    <div class="footer-section">
                        <h3>Quick Links</h3>
                        <p><a href="/">Home</a></p>
                        <p><a href="/about">About</a></p>
                        <p><a href="/services">Services</a></p>
                        <p><a href="/contact">Contact</a></p>
                        <p><a href="/dashboard">Dashboard</a></p>
                    </div>
                    <div class="footer-section">
                        <h3>Contact Info</h3>
                        <p>Email: hello@solveitwithcode.com</p>
                        <p>Phone: +1 (555) 123-4567</p>
                        <p>Location: San Francisco, CA</p>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>© 2024 Solve It With Code. All rights reserved.</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """

@rt('/live-stats')
def live_stats():
    """Generate live, dynamic statistics for the dashboard"""
    # Simulate real-time data updates
    active_coders = random.randint(1200, 1300)
    problems_solved = random.randint(85, 95)
    lines_of_code = random.randint(2400000, 2500000)
    active_projects = random.randint(45, 55)
    
    return f"""
    <div class="stat-card">
        <div class="stat-number">{active_coders:,}</div>
        <div class="stat-label">Active Coders</div>
        <div class="stat-change positive">+{random.randint(15, 30)} today</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{problems_solved}</div>
        <div class="stat-label">Problems Solved</div>
        <div class="stat-change positive">+{random.randint(3, 8)} this week</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{lines_of_code:,}</div>
        <div class="stat-label">Lines of Code</div>
        <div class="stat-change positive">+{random.randint(100000, 200000):,} today</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{active_projects}</div>
        <div class="stat-label">Active Projects</div>
        <div class="stat-change positive">+{random.randint(1, 5)} new</div>
    </div>
    """

@rt('/live-activity')
def live_activity():
    """Stream live activity updates"""
    activities = [
        ("💻", "Alex K. optimized quantum algorithm", "1 minute ago"),
        ("🚀", "Team Beta launched ML pipeline", "3 minutes ago"),
        ("🔬", "New neural network architecture created", "6 minutes ago"),
        ("🌍", "Global data visualization project completed", "9 minutes ago"),
        ("⚡", "Performance optimization breakthrough", "12 minutes ago"),
        ("🔒", "Security protocol implementation finished", "15 minutes ago"),
        ("📱", "Mobile app beta testing started", "18 minutes ago"),
        ("☁️", "Cloud infrastructure scaled successfully", "21 minutes ago")
    ]
    
    # Randomly select 3-4 activities
    selected = random.sample(activities, random.randint(3, 4))
    
    activity_html = ""
    for icon, text, time in selected:
        activity_html += f"""
        <div class="activity-item">
            <div class="activity-icon">{icon}</div>
            <div class="activity-content">
                <div class="activity-text">{text}</div>
                <div class="activity-time">{time}</div>
            </div>
        </div>
        """
    
    return activity_html

if __name__ == "__main__":
    serve()