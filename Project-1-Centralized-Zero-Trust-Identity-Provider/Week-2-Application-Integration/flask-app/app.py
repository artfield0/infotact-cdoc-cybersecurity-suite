from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = "supersecret"

oauth = OAuth(app)

oauth.register(
    name='keycloak',
    client_id='flask-app',
    client_secret='z6I4GIFoo2DL0ASO6eGfgSvlvEvLHeOw',
    server_metadata_url='http://keycloak:8080/realms/infotact/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email'
    }
)

@app.route("/")
def home():
    return '<a href="/login">Login with Keycloak</a>'

@app.route("/login")
def login():
    return oauth.keycloak.authorize_redirect(
        redirect_uri=url_for("auth", _external=True)
    )

@app.route("/auth")
def auth():
    token = oauth.keycloak.authorize_access_token()
    userinfo = oauth.keycloak.userinfo()

    session['user'] = userinfo
    session['id_token'] = token['id_token']   # <-- IMPORTANT

    return redirect("/protected")

@app.route("/protected")
def protected():
    if 'user' not in session:
        return redirect("/")
    return f"""
        <h1>Protected Page</h1>
        <p>Welcome {session['user']['preferred_username']}</p>
        <a href='/logout'>Logout</a>
    """

@app.route("/logout")
def logout():
    id_token = session.get("id_token")

    session.clear()

    return redirect(
        "http://localhost:8080/realms/infotact/protocol/openid-connect/logout"
        f"?post_logout_redirect_uri=http://localhost:5000"
        f"&id_token_hint={id_token}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
