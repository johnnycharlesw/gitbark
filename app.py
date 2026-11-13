import flask
import mariadb
import gitbark_config

# Create a Flask application instance
app = flask.Flask(__name__)
# Connect to the database
conn = mariadb.connect(
    user=gitbark_config.DB_USER,
    password=gitbark_config.DB_PASSWORD,
    host=gitbark_config.DB_HOST,
    database=gitbark_config.DB_NAME
)
# Create a cursor object using the cursor() method
cursor = conn.cursor()
# Define a route for the home page
@app.route('/')
def home():
    # Execute a query to retrieve data from the database
    cursor.execute("SELECT * FROM users")
    # Fetch all the rows from the query
    rows = cursor.fetchall()
    # Render the home page template with the data
    return flask.render_template('home.html', users=rows)