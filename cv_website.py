from flask import Flask, render_template_string, url_for

app = Flask(__name__)

MENU_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sabina Bacaoanu - Menu</title>
    <style>
        body { font-family: Arial, sans-serif; background: #e0f7fa; margin: 0; }
        .menu-container { display: flex; height: 100vh; justify-content: center; align-items: center; }
        .menu { background: #fff; padding: 40px 60px; border-radius: 12px; box-shadow: 0 4px 16px #b2ebf2; }
        .menu a { display: block; font-size: 2em; color: #00796b; text-decoration: none; margin: 20px 0; transition: color 0.2s; }
        .menu a:hover { color: #004d40; }
    </style>
</head>
<body>
    <div class="menu-container">
        <div class="menu">
            <a href="{{ url_for('resume') }}">Resume</a>
        </div>
    </div>
</body>
</html>
"""

RESUME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sabina Bacaoanu - Resume</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background: linear-gradient(135deg, #ffecb3 0%, #ffe0b2 100%); }
        .container { max-width: 800px; margin: 40px auto; background: #fffde7; padding: 40px; border-radius: 16px; box-shadow: 0 6px 24px #ffd54f; }
        h1 { color: #ff9800; }
        h2 { color: #f57c00; margin-top: 30px; }
        ul { padding-left: 20px; }
        .profile-pic { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 4px solid #ffb300; margin-bottom: 20px; }
        .header { display: flex; align-items: center; gap: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Profile Picture" class="profile-pic">
            <div>
                <h1>Sabina Bacaoanu</h1>
                <p>Email: sabina@example.com | Location: City, Country</p>
            </div>
        </div>
        <h2>Profile</h2>
        <p>Motivated professional with experience in web development and a passion for learning new technologies.</p>
        <h2>Skills</h2>
        <ul>
            <li>Python</li>
            <li>Flask</li>
            <li>HTML, CSS</li>
            <li>JavaScript</li>
        </ul>
        <h2>Experience</h2>
        <ul>
            <li><strong>Web Developer</strong> - Company Name (2022-Present)</li>
            <li><strong>Intern</strong> - Another Company (2021-2022)</li>
        </ul>
        <h2>Education</h2>
        <ul>
            <li>BSc in Computer Science - University Name (2018-2022)</li>
        </ul>
    </div>
</body>
</html>
"""


@app.route("/")
def menu():
    return render_template_string(MENU_HTML)


@app.route("/resume")
def resume():
    return render_template_string(RESUME_HTML)


if __name__ == "__main__":
    app.run(debug=True)
