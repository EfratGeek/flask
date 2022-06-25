from flask import Flask
from flask import redirect, render_template, request, send_file, session, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/download")
async def get_exe_file():
    try:
        return send_file(r"C:\Users\User\my-proj\my-proj-0.0.1.vsix",
                         attachment_filename='Quick-design.vsix')

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
