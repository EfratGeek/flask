from flask import Flask
from flask import redirect, render_template, request, send_file, session, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/download")
async def get_exe_file():
    try:
        return send_file("C:\\Users\\User\Desktop\Software and applications\Software for installation\\revosetup.exe",
                         attachment_filename='revosetup.exe')

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
