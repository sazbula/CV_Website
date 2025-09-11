from flask import Flask, render_template_string

# First, ensure Flask is installed:
# Run in your terminal: pip install flask


app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sabina Bacaoanu - CV</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }
        .container { max-width: 700px; margin: auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px #ccc; }
        h1 { color: #333; }
        h2 { color: #555; margin-top: 30px; }
        ul { padding-left: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sabina Bacaoanu</h1>
        <p>Email: sabina@example.com | Location: City, Country</p>
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
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
