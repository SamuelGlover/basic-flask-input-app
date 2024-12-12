from flask import Flask, render_template, request

# Create a Flask application instance
app = Flask(__name__)

@app.route("/about")  # For about.html
def about():
    return render_template("about.html")

@app.route("/portfolio")  # For portfolio.html
def portfolio():
    return render_template("portfolio.html")

@app.route("/")  # For index.html
def index():
    return render_template("index.html")


# Define a route for the root URL ("/")
# The route handles both GET (displaying the form) and POST (handling form submissions) requests
@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize a variable to store the message to be displayed
    message = None

    # Check if the request method is POST (i.e., the form was submitted)
    if request.method == "POST":
        # Get the user input from the form (the input field named "user_input")
        user_input = request.form.get("user_input")

        # Check if the user actually entered something
        if user_input:
            # If there's input, create a success message
            message = f"You entered: {user_input}"
        else:
            # If the input is empty, create an error message
            message = "Please enter some text."

    # Render the 'index.html' template and pass the 'message' variable to it
    # This allows the HTML template to display the message dynamically
    return render_template("index.html", message=message)

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Run the Flask development server
    # debug=True enables automatic reloading on code changes
    # host='0.0.0.0' makes the server accessible from outside the container (important for Codespaces)
    # port=5000 sets the port the app runs on
    app.run(debug=True, host='0.0.0.0', port=5000)